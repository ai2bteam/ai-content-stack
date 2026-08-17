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

## [AutoGen](https://microsoft.github.io/autogen/)

Каркас Microsoft для разговаривающих между собой агентов. Сильная сторона — проверка работы друг друга.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/microsoft/autogen |

`framework` `multi-agent` `microsoft`

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

## [Claude Desktop](https://claude.ai/download) ⭐

Настольное приложение с поддержкой MCP. Для тех, кому терминал не нужен, а Palmier и Blender подключить хочется.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |

`desktop` `mcp`

---

## [Cline](https://cline.bot/)

Открытый агент внутри VS Code со своим ключом от любой модели. Умеет ставить MCP-серверы сам.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |
| **Исходники** | https://github.com/cline/cline |

`vscode` `mcp` `open-source`

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

## [Continue](https://continue.dev/)

Открытый ассистент для VS Code и JetBrains, работает и с локальными моделями через Ollama.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **API-ключ** | необязателен |
| **Исходники** | https://github.com/continuedev/continue |

`ide` `local-models` `open-source`

---

## [CrewAI](https://www.crewai.com/)

Команда агентов с ролями и задачами. Ложится на производство ролика: сценарист, ресёрчер, редактор.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/crewAIInc/crewAI |

`framework` `multi-agent` `roles`

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

## [Dify](https://dify.ai/)

Визуальный конструктор AI-приложений, который ставится на свой сервер. Пайплайн собирается мышкой.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/langgenius/dify |

`low-code` `self-hosted` `workflow`

---

## [FastMCP](https://github.com/jlowin/fastmcp)

Свой MCP-сервер на Python в несколько десятков строк. Так закрывают дыру, когда готового сервера нет.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/jlowin/fastmcp |

```bash
pip install fastmcp
```

`mcp` `development` `python`

---

## [Flowise](https://flowiseai.com/)

Нодовый редактор цепочек и агентов. Быстро проверить идею до того, как писать код.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/FlowiseAI/Flowise |

`low-code` `nodes` `self-hosted`

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

## [Glama MCP Directory](https://glama.ai/mcp/servers)

Каталог MCP-серверов с оценкой качества и безопасности. Полезнее голого списка на GitHub.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟢 бесплатно |
| **Из агента** | — |

`mcp` `registry` `quality`

---

## [Goose](https://block.github.io/goose/)

Открытый агент от Block с расширениями поверх MCP. Работает и в терминале, и с интерфейсом.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |
| **Исходники** | https://github.com/block/goose |

`cli` `mcp` `open-source`

---

## [Langflow](https://www.langflow.org/)

Визуальная сборка потоков с экспортом в код. Мостик между прототипом на мышке и рабочим скриптом.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/langflow-ai/langflow |

`low-code` `nodes` `export`

---

## [Langfuse](https://langfuse.com/)

Видно, что агент реально делал, сколько потратил и где сломался. Без этого длинный пайплайн отлаживается вслепую.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **API-ключ** | необязателен |
| **Исходники** | https://github.com/langfuse/langfuse |

`observability` `tracing` `self-hosted`

---

## [LangGraph](https://www.langchain.com/langgraph)

Агент как граф состояний с циклами и ветвлениями. Когда пайплайн должен уметь возвращаться на шаг назад.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/langchain-ai/langgraph |

`framework` `graph` `python`

---

## [LlamaIndex](https://www.llamaindex.ai/)

Подключает агента к своим документам и базам. Отсюда берётся ответ по архиву сценариев, а не по интернету.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/run-llama/llama_index |

`framework` `rag` `retrieval`

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

## [Mastra](https://mastra.ai/)

Каркас агентов на TypeScript. Тот же язык, что у Remotion — пайплайн не разъезжается по двум экосистемам.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/mastra-ai/mastra |

`framework` `typescript`

---

## [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

Отладчик MCP-серверов: видно инструменты, аргументы и ответы. Первое, что запускаешь, когда сервер молчит.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/modelcontextprotocol/inspector |

```bash
npx @modelcontextprotocol/inspector
```

`mcp` `debugging`

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

## [Node-RED](https://nodered.org/)

Проводной редактор потоков, живущий с 2013 года. Крутится хоть на Raspberry Pi рядом со студией.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |

`automation` `nodes` `self-hosted`

---

## [OpenCode](https://opencode.ai/)

Открытый терминальный агент, не привязанный к одному провайдеру моделей.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |
| **Исходники** | https://github.com/sst/opencode |

`cli` `open-source` `multi-provider`

---

## [Pipedream](https://pipedream.com/)

Интеграции со вставками своего кода между шагами. Гибче Zapier там, где нужна логика.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`automation` `code-steps`

---

## [PulseMCP](https://www.pulsemcp.com/)

Новости и свежие MCP-серверы с рассылкой. Способ не пропустить появление нужного сервера.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟢 бесплатно |
| **Из агента** | — |

`mcp` `registry` `news`

---

## [Pydantic AI](https://ai.pydantic.dev/)

Агенты с типизированным ответом, который валидируется. Модель не может вернуть мусор вместо структуры.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/pydantic/pydantic-ai |

`framework` `python` `typed`

---

## [Roo Code](https://roocode.com/)

Форк Cline с режимами под разные роли. Полезно, когда один агент пишет сценарий, а другой — код сцены.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |
| **Исходники** | https://github.com/RooCodeInc/Roo-Code |

`vscode` `mcp` `modes`

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

## [Trigger.dev](https://trigger.dev/)

Долгие фоновые задачи без таймаутов и с ретраями. Под рендер, который идёт полчаса.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **API-ключ** | необязателен |
| **Исходники** | https://github.com/triggerdotdev/trigger.dev |

`background-jobs` `long-running` `typescript`

---

## [Windmill](https://www.windmill.dev/)

Свои скрипты на Python или TypeScript превращаются в задачи с расписанием и интерфейсом. Самохостится.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/windmill-labs/windmill |

`automation` `self-hosted` `scripts`

---

## [Windsurf](https://windsurf.com/)

Редактор с агентом, конкурент Cursor. Тоже понимает MCP — серверы из каталога подключаются и сюда.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |

`ide` `mcp`

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

## [Zed](https://zed.dev/)

Очень быстрый открытый редактор на Rust с агентом и MCP. Заметно легче Electron-собратьев.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | необязателен |
| **Исходники** | https://github.com/zed-industries/zed |

`ide` `rust` `mcp` `open-source`

---

