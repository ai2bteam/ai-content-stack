#!/usr/bin/env python3
"""Собирает README.md и страницы catalog/ из data/*.yaml.

    python3 scripts/build.py            # перегенерировать файлы
    python3 scripts/build.py --check    # ничего не писать, упасть если файлы разошлись с данными

Единственный источник правды — data/tools.yaml и data/routing.yaml.
Всё, что этот скрипт пишет, начинается с маркера GENERATED и правится только через YAML.
"""
import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CATALOG = ROOT / "catalog"

BANNER = (
    "<!-- GENERATED — не правь руками. Источник: data/*.yaml. "
    "Пересобрать: python3 scripts/build.py -->"
)

PRICING = {
    "free": "🟢 бесплатно",
    "freemium": "🟡 freemium",
    "paid": "🔴 платно",
    "oss": "🔵 open source",
}

AGENT = {
    "mcp": "`MCP`",
    "api": "`API`",
    "cli": "`CLI`",
    "native": "—",
    "none": "—",
}

KEY = {"none": "—", "optional": "опц.", "required": "нужен"}

CATEGORY_FIELDS = {"id", "name", "emoji", "blurb"}

TOOL_FIELDS = {
    "id", "name", "category", "kind", "pricing", "url", "tagline", "status",
    "agent", "key", "key_url", "install", "env", "docs", "repo", "platforms",
    "tags", "note", "guide",
}

KIND = {
    "app": "приложение",
    "mcp": "MCP-сервер",
    "library": "библиотека",
    "api": "API",
    "service": "сервис",
    "model": "модель",
    "cli": "CLI",
    "spec": "протокол",
    "format": "формат",
    "reference": "справочник",
}


# ─────────────────────────── загрузка и проверка ───────────────────────────

def load():
    tools_doc = yaml.safe_load((DATA / "tools.yaml").read_text(encoding="utf-8"))
    routing_doc = yaml.safe_load((DATA / "routing.yaml").read_text(encoding="utf-8"))
    validate(tools_doc, routing_doc)
    return tools_doc, routing_doc


def validate(tools_doc, routing_doc):
    errors = []
    cats = [c["id"] for c in tools_doc["categories"]]
    if len(cats) != len(set(cats)):
        errors.append("повторяющиеся id категорий")

    for c in tools_doc["categories"]:
        for field in ("id", "name", "emoji", "blurb"):
            if not c.get(field):
                errors.append("категория {}: не заполнено поле «{}»".format(c.get("id"), field))
        extra = set(c) - CATEGORY_FIELDS
        if extra:
            errors.append("категория {}: лишние поля {} — опечатка или запись уехала не в тот блок"
                          .format(c.get("id"), sorted(extra)))

    seen = set()
    for t in tools_doc["tools"]:
        tid = t.get("id", "<без id>")
        for field in ("id", "name", "category", "kind", "pricing", "url", "tagline", "status"):
            if not t.get(field):
                errors.append(f"{tid}: не заполнено поле «{field}»")
        if tid in seen:
            errors.append(f"{tid}: id встречается больше одного раза")
        seen.add(tid)
        extra = set(t) - TOOL_FIELDS
        if extra:
            errors.append(f"{tid}: лишние поля {sorted(extra)} — опечатка в названии поля?")
        if t.get("category") not in cats:
            errors.append(f"{tid}: неизвестная категория «{t.get('category')}»")
        if t.get("pricing") not in PRICING:
            errors.append(f"{tid}: неизвестная цена «{t.get('pricing')}»")
        if t.get("agent", "none") not in AGENT:
            errors.append(f"{tid}: неизвестный способ вызова «{t.get('agent')}»")
        if t.get("key", "none") not in KEY:
            errors.append(f"{tid}: неизвестное значение key «{t.get('key')}»")
        if t.get("status") not in ("verified", "listed"):
            errors.append(f"{tid}: status должен быть verified или listed")
        if t.get("guide") and not (ROOT / t["guide"]).exists():
            errors.append(f"{tid}: разбор «{t['guide']}» не найден")

    for group in routing_doc["routing"]:
        for row in group["rows"]:
            for ref in row["tools"]:
                if ref not in seen:
                    errors.append(f"routing «{row['task']}»: нет инструмента с id «{ref}»")

    if errors:
        print("Данные не прошли проверку:", file=sys.stderr)
        for e in errors:
            print("  ✗ " + e, file=sys.stderr)
        sys.exit(1)


# ─────────────────────────── рендер ───────────────────────────

def by_category(tools_doc):
    out = {}
    for t in tools_doc["tools"]:
        out.setdefault(t["category"], []).append(t)
    return out


def link(tool):
    return "[{}]({})".format(tool["name"], tool["url"])


def render_readme(tools_doc, routing_doc):
    meta = tools_doc["meta"]
    tools = tools_doc["tools"]
    cats = tools_doc["categories"]
    grouped = by_category(tools_doc)
    index = {t["id"]: t for t in tools}
    via_mcp = [t for t in tools if t.get("agent") == "mcp"]
    free = [t for t in tools if t["pricing"] in ("free", "oss")]

    L = [BANNER, ""]
    L.append("# 🧰 " + meta["title"])
    L.append("")
    L.append("> " + meta["tagline"])
    L.append("")
    L.append(
        "**{} инструментов · {} категорий · {} подключаются к агенту по MCP · "
        "{} бесплатны или open source**".format(
            len(tools), len(cats), len(via_mcp), len(free)
        )
    )
    L.append("")
    L.append("---")
    L.append("")

    L.append("## Как этим пользоваться")
    L.append("")
    L.append(
        "Каталог отвечает не на вопрос «какие бывают ИИ-инструменты», а на вопрос "
        "**«мне нужно вот это — чем делать»**. Поэтому начинай с таблицы "
        "[Задача → инструмент](#задача--инструмент), а не с оглавления."
    )
    L.append("")
    L.append("Три правила, которые экономят больше всего времени:")
    L.append("")
    L.append(
        "1. **Сначала сток, потом генерация.** Готовый кадр находится за секунды и не ест лимиты. "
        "Генерация — это когда стока действительно нет."
    )
    L.append(
        "2. **Видеоряд важнее статики.** На сцену длиннее трёх секунд ищи MP4 или GIF, "
        "а не фотографию с ken burns."
    )
    L.append(
        "3. **Смотри на колонку «Из агента».** Инструмент с `MCP` встраивается в рабочий чат "
        "и не требует переключения контекста — это чаще всего важнее, чем разница в качестве."
    )
    L.append("")

    guided = [t for t in tools if t.get("guide")]
    if guided:
        L.append("## Разборы")
        L.append("")
        L.append(
            "Таблицы отвечают на вопрос «чем делать». Там, где важнее понять устройство, "
            "есть отдельный разбор:"
        )
        L.append("")
        for t in sorted(guided, key=lambda x: x["name"].lower()):
            L.append("- **[{}]({})** — {}".format(t["name"], t["guide"], t["tagline"]))
        L.append("")

    # маршрутизация
    L.append("## Задача → инструмент")
    L.append("")
    for group in routing_doc["routing"]:
        L.append("### " + group["group"])
        L.append("")
        L.append("| Задача | Чем делать | Комментарий |")
        L.append("|---|---|---|")
        for row in group["rows"]:
            names = " · ".join(link(index[r]) for r in row["tools"])
            L.append("| {} | {} | {} |".format(row["task"], names, row.get("note", "")))
        L.append("")

    # оглавление
    L.append("## Категории")
    L.append("")
    for c in cats:
        n = len(grouped.get(c["id"], []))
        L.append(
            "- {} **[{}](#cat-{})** — {} _({})_".format(
                c["emoji"], c["name"], c["id"], c["blurb"], n
            )
        )
    L.append("")
    L.append("---")
    L.append("")

    # категории
    for c in cats:
        items = sorted(grouped.get(c["id"], []), key=lambda t: t["name"].lower())
        L.append('<a id="cat-{}"></a>'.format(c["id"]))
        L.append("")
        L.append("## {} {}".format(c["emoji"], c["name"]))
        L.append("")
        L.append("> " + c["blurb"])
        L.append("")
        L.append("| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |")
        L.append("|---|---|---|---|---|---|")
        for t in items:
            star = " ⭐" if t["status"] == "verified" else ""
            L.append(
                "| **[{}]({})**{} | {} | {} | {} | {} | {} |".format(
                    t["name"],
                    t["url"],
                    star,
                    t["tagline"],
                    KIND.get(t["kind"], t["kind"]),
                    PRICING[t["pricing"]],
                    AGENT[t.get("agent", "none")],
                    KEY[t.get("key", "none")],
                )
            )
        L.append("")
        L.append(
            "→ [Подробные карточки: установка, ключи, заметки](catalog/{}.md)".format(c["id"])
        )
        L.append("")

    L.append("---")
    L.append("")
    L.append("## Легенда")
    L.append("")
    L.append("| Обозначение | Значение |")
    L.append("|---|---|")
    L.append("| ⭐ | Проверено на реальных проектах, а не только внесено в список |")
    L.append("| `MCP` | Подключается к агенту по Model Context Protocol — команды идут из чата |")
    L.append("| `API` | Есть HTTP API, агент дёргает его скриптом |")
    L.append("| `CLI` | Ставится локально, агент вызывает через терминал |")
    L.append("| 🟢 🟡 🔴 🔵 | бесплатно · freemium · платно · open source |")
    L.append("")
    L.append("## Что-то отсутствует или устарело")
    L.append("")
    L.append(
        "Каталог живёт в двух YAML-файлах, README собирается из них скриптом. "
        "Как добавить инструмент — в [CONTRIBUTING.md](CONTRIBUTING.md). "
        "Если лень возиться с YAML, просто "
        "[заведи issue]({}/issues/new?template=add-tool.yml).".format(meta["repo"])
    )
    L.append("")
    return "\n".join(L) + "\n"


def render_category(cat, items, meta):
    items = sorted(items, key=lambda t: t["name"].lower())
    L = [BANNER, ""]
    L.append("# {} {}".format(cat["emoji"], cat["name"]))
    L.append("")
    L.append("> " + cat["blurb"])
    L.append("")
    L.append("[← Ко всему каталогу](../README.md)")
    L.append("")
    L.append("---")
    L.append("")
    for t in items:
        star = " ⭐" if t["status"] == "verified" else ""
        L.append("## [{}]({}){}".format(t["name"], t["url"], star))
        L.append("")
        L.append(t["tagline"])
        L.append("")

        facts = [
            ("Тип", KIND.get(t["kind"], t["kind"])),
            ("Цена", PRICING[t["pricing"]]),
            ("Из агента", AGENT[t.get("agent", "none")]),
        ]
        key = t.get("key", "none")
        if key == "required":
            kv = "нужен"
            if t.get("key_url"):
                kv = "нужен — [получить]({})".format(t["key_url"])
            facts.append(("API-ключ", kv))
        elif key == "optional":
            facts.append(("API-ключ", "необязателен"))
        if t.get("platforms"):
            facts.append(("Платформы", ", ".join(t["platforms"])))
        if t.get("docs"):
            facts.append(("Документация", t["docs"]))
        if t.get("repo"):
            facts.append(("Исходники", t["repo"]))
        if t.get("guide"):
            facts.append(("Разбор", "[читать](../{})".format(t["guide"])))

        L.append("| | |")
        L.append("|---|---|")
        for k, v in facts:
            L.append("| **{}** | {} |".format(k, v))
        L.append("")

        if t.get("install"):
            L.append("```bash")
            L.append(t["install"])
            L.append("```")
            L.append("")
        if t.get("env"):
            L.append(
                "Переменные окружения: "
                + ", ".join("`{}`".format(e) for e in t["env"])
                + ". Держи их в конфиге агента, не в репозитории."
            )
            L.append("")
        if t.get("note"):
            L.append(t["note"].rstrip())
            L.append("")
        if t.get("tags"):
            L.append(" ".join("`{}`".format(x) for x in t["tags"]))
            L.append("")
        L.append("---")
        L.append("")
    return "\n".join(L) + "\n"


# ─────────────────────────── точка входа ───────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="только проверить, что файлы актуальны")
    args = ap.parse_args()

    tools_doc, routing_doc = load()
    grouped = by_category(tools_doc)

    targets = {ROOT / "README.md": render_readme(tools_doc, routing_doc)}
    for c in tools_doc["categories"]:
        targets[CATALOG / (c["id"] + ".md")] = render_category(
            c, grouped.get(c["id"], []), tools_doc["meta"]
        )

    if args.check:
        stale = []
        for path, content in targets.items():
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT))
        if stale:
            print("Эти файлы разошлись с data/*.yaml:", file=sys.stderr)
            for s in stale:
                print("  ✗ " + str(s), file=sys.stderr)
            print("\nЗапусти: python3 scripts/build.py", file=sys.stderr)
            sys.exit(1)
        print("✓ README и catalog/ соответствуют данным")
        return

    CATALOG.mkdir(exist_ok=True)
    for path, content in targets.items():
        path.write_text(content, encoding="utf-8")
    print(
        "✓ собрано: README.md и {} страниц в catalog/ ({} инструментов)".format(
            len(targets) - 1, len(tools_doc["tools"])
        )
    )


if __name__ == "__main__":
    main()
