<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# 🤖 Агенты и оркестрация

> Среда, из которой всё запускается. Агент читает задачу и сам дёргает нужные инструменты.

[← Ко всему каталогу](../README.md)

---

## [Activepieces](https://www.activepieces.com/)

Открытая замена Zapier с MCP на борту. Автоматизации живут на своём сервере.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/activepieces/activepieces |

`automation` `self-hosted` `mcp`

---

## [Aider](https://aider.chat/)

Открытый агент, работающий через git-коммиты. Каждая правка откатывается одной командой.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **API-ключ** | нужен |
| **Исходники** | https://github.com/Aider-AI/aider |

`cli` `git` `open-source`

---

## [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview)

Собрать своего агента с тем же циклом инструментов, что у Claude Code.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен — [получить](https://console.anthropic.com/) |

---

## [Claude Code](https://claude.com/product/claude-code) ⭐

Агент в терминале, десктопе, вебе и IDE. Точка входа во весь остальной стек.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔴 платно |
| **Из агента** | — |
| **Документация** | https://docs.claude.com/en/docs/claude-code/overview |

Всё в этом каталоге так или иначе подключается сюда: MCP-серверы через `claude mcp add`,
повторяемые процессы — через skills, многоагентные прогоны — через workflows.

---

## [Codex CLI](https://github.com/openai/codex)

Терминальный агент OpenAI. Тоже понимает MCP — те же серверы из этого каталога подключаются и к нему.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔴 платно |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |
| **Исходники** | https://github.com/openai/codex |

`cli` `mcp`

---

## [ComfyUI API](https://docs.comfy.org/)

У локального ComfyUI есть HTTP-эндпоинт: агент кидает граф в очередь и забирает готовый файл.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |

`local` `automation`

---

## [Composio](https://composio.dev/)

Сотни готовых интеграций как инструменты агента, с решённой авторизацией. Не писать свой MCP под каждый сервис.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |

`mcp` `integrations` `auth`

---

## [Cursor](https://cursor.com/)

Редактор кода с агентом внутри. Понимает MCP, поэтому тот же Palmier или Blender цепляются и сюда.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |

`ide` `mcp`

---

## [Gemini CLI](https://github.com/google-gemini/gemini-cli)

Агент Google в терминале, с MCP и щедрым бесплатным лимитом.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |
| **Исходники** | https://github.com/google-gemini/gemini-cli |

`cli` `mcp`

---

## [Make](https://www.make.com/)

То же, что n8n, но как сервис и без своего сервера. Дороже на объёме, дешевле на старте.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |

`automation` `pipeline`

---

## [MCP Registry](https://github.com/modelcontextprotocol/registry)

Официальный реестр MCP-серверов. В отличие от сторонних каталогов — источник, а не витрина.

| | |
|---|---|
| **Тип** | справочник |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/modelcontextprotocol/registry |

`mcp` `registry`

---

## [Model Context Protocol](https://modelcontextprotocol.io/) ⭐

Открытый протокол, по которому агент получает чужие инструменты. Причина, по которой этот каталог вообще имеет смысл.

| | |
|---|---|
| **Тип** | протокол |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/modelcontextprotocol |

---

## [n8n](https://n8n.io/)

Визуальные автоматизации, которые можно хостить у себя. Держит контент-конвейер: вышел ролик — разошлось по площадкам.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **Исходники** | https://github.com/n8n-io/n8n |

`automation` `self-hosted` `pipeline`

---

## [Smithery](https://smithery.ai/)

Каталог MCP-серверов с установкой в одну команду. Первое место, куда идти за «а есть ли MCP для...».

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `MCP` |

`mcp` `registry`

---

## [Zapier MCP](https://zapier.com/mcp)

Тысячи приложений Zapier открываются агенту как инструменты. Самый широкий охват из существующих.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |

`mcp` `integrations`

---

