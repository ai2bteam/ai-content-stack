#!/usr/bin/env python3
"""Проверяет, что ссылки из data/tools.yaml ещё живые.

    python3 scripts/check_links.py              # упасть, если ссылка мертва
    python3 scripts/check_links.py --strict     # падать ещё и на «не удалось проверить»

Ссылки делятся на три группы, и это принципиально:

  живые       2xx или редирект
  закрытые    сайт не дал ответа по существу: 403 / 429 / 5xx, ошибка TLS,
              таймаут. Это НЕ доказательство того, что страница мертва —
              крупные сайты режут автоматику, а медленные просто не успевают.
              CI на таких не падает.
  мёртвые     GET вернул 404 или 410, либо домена не существует. Только это
              считается поломкой — и только по ответу на GET: HEAD у многих
              серверов реализован кое-как и отдаёт 404 на живую страницу.

Разделение принципиальное: если считать таймаут поломкой, CI начнёт падать
на живых ссылках, и его перестанут читать.

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
TIMEOUT = 25
LINK_FIELDS = ("url", "docs", "repo", "key_url")
# определённое «такой страницы нет» — только это считаем поломкой
DEAD_CODES = {404, 410}
DEAD_DNS = ("nodename nor servname", "name or service not known",
            "no address associated", "getaddrinfo failed")
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
    last = "ответа не получено"
    # HEAD дешевле, но многие его не любят; GET без редиректов — на случай,
    # когда сервер отдаёт 3xx и обрывает соединение
    for method, follow in (("HEAD", True), ("GET", True), ("GET", False)):
        try:
            code = probe(url, method, follow)
            if 200 <= code < 400:
                return (tool_id, field, url, ALIVE, code)
        except urllib.error.HTTPError as e:
            if 300 <= e.code < 400:
                return (tool_id, field, url, ALIVE, e.code)
            if e.code in DEAD_CODES:
                # HEAD многие реализуют кое-как и отдают 404 на живую страницу
                # (Kaggle — ровно такой случай). Верим только ответу на GET.
                if method == "GET":
                    return (tool_id, field, url, DEAD, "HTTP {}".format(e.code))
                last = "HTTP {} на HEAD".format(e.code)
            # 403, 429, 5xx и прочее — сервер жив, но говорить не хочет
            last = "HTTP {}".format(e.code)
        except urllib.error.URLError as e:
            reason = str(getattr(e, "reason", e))
            low = reason.lower()
            if any(m in low for m in DEAD_DNS):
                return (tool_id, field, url, DEAD, "домен не существует")
            if "ssl" in low or "certificate" in low:
                return (tool_id, field, url, BLOCKED, "TLS: " + reason[:70])
            last = reason[:90]
        except Exception as e:  # noqa: BLE001 — сеть, прилететь может что угодно
            last = type(e).__name__ + ": " + str(e)[:80]
    # сюда попадают таймауты и всё, что не дало определённого ответа
    return (tool_id, field, url, BLOCKED, last)


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
        print("Не удалось проверить — сайт режет автоматику, медленно отвечает")
        print("или отдал 5xx. Проверь глазами, но на поломку это не тянет:")
        for tool_id, field, url, _s, info in blocked:
            print("  ? {:<24} {:<8} {}  → {}".format(tool_id, field, url, info))
        print()

    print("{} живых · {} непроверяемых · {} мёртвых из {}".format(
        len(alive), len(blocked), len(dead), len(results)))

    if dead or (args.strict and blocked):
        sys.exit(1)


if __name__ == "__main__":
    main()
