#!/usr/bin/env python3
"""Проверяет, что ссылки из data/tools.yaml ещё живые.

    python3 scripts/check_links.py              # упасть, если ссылка мертва
    python3 scripts/check_links.py --strict     # падать ещё и на «не удалось проверить»

Ссылки делятся на три группы, и это принципиально:

  живые       2xx или редирект на осмысленный адрес
  закрытые    403 / 405 / 429 или ошибка TLS — сайт отбивает автоматику.
              Это не значит, что страница мертва, поэтому CI на таких не падает.
  мёртвые     404 / 410, домен не резолвится, соединение отвергнуто.

Из зависимостей — только pyyaml.
"""
import argparse
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
TIMEOUT = 20
LINK_FIELDS = ("url", "docs", "repo", "key_url")
BLOCKING_CODES = {401, 403, 405, 406, 429, 503}
CTX = ssl.create_default_context()

ALIVE, BLOCKED, DEAD = "alive", "blocked", "dead"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Редирект — это живая ссылка. Не идём по цепочке, просто фиксируем факт."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def probe(url, method, follow):
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(NoRedirect)
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    with opener.open(req, timeout=TIMEOUT) as r:
        return r.status


def check(item):
    tool_id, field, url = item
    last = "не удалось получить ответ"
    for method, follow in (("HEAD", True), ("GET", True), ("GET", False)):
        try:
            code = probe(url, method, follow)
            if 200 <= code < 400:
                return (tool_id, field, url, ALIVE, code)
        except urllib.error.HTTPError as e:
            if 300 <= e.code < 400:
                return (tool_id, field, url, ALIVE, e.code)
            if e.code in BLOCKING_CODES:
                return (tool_id, field, url, BLOCKED, "HTTP {}".format(e.code))
            last = "HTTP {}".format(e.code)
            if e.code in (404, 410):
                return (tool_id, field, url, DEAD, last)
        except urllib.error.URLError as e:
            reason = str(getattr(e, "reason", e))
            if "SSL" in reason or "CERTIFICATE" in reason.upper():
                return (tool_id, field, url, BLOCKED, "TLS: " + reason[:70])
            last = reason[:90]
        except Exception as e:  # noqa: BLE001
            last = type(e).__name__ + ": " + str(e)[:80]
    return (tool_id, field, url, DEAD, last)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="падать и на ссылках, которые не удалось проверить")
    args = ap.parse_args()

    doc = yaml.safe_load((ROOT / "data" / "tools.yaml").read_text(encoding="utf-8"))
    targets = [(t["id"], f, t[f]) for t in doc["tools"] for f in LINK_FIELDS if t.get(f)]

    print("Проверяю {} ссылок...\n".format(len(targets)))
    with ThreadPoolExecutor(max_workers=12) as pool:
        results = list(pool.map(check, targets))

    dead = sorted(r for r in results if r[3] == DEAD)
    blocked = sorted(r for r in results if r[3] == BLOCKED)
    alive = [r for r in results if r[3] == ALIVE]

    if dead:
        print("МЁРТВЫЕ — их надо чинить:")
        for tool_id, field, url, _s, info in dead:
            print("  ✗ {:<24} {:<8} {}\n      {}".format(tool_id, field, url, info))
        print()
    if blocked:
        print("Не удалось проверить (сайт отбивает автоматику — проверь глазами):")
        for tool_id, field, url, _s, info in blocked:
            print("  ? {:<24} {:<8} {}  → {}".format(tool_id, field, url, info))
        print()

    print("{} живых · {} непроверяемых · {} мёртвых из {}".format(
        len(alive), len(blocked), len(dead), len(results)))

    if dead or (args.strict and blocked):
        sys.exit(1)


if __name__ == "__main__":
    main()
