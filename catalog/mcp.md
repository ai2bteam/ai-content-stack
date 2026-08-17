<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# 🔌 MCP-серверы

> Инструменты, подключаемые к агенту по протоколу MCP. Агент управляет ими напрямую — без копипасты и ручного клика.

[← Ко всему каталогу](../README.md)

---

## [Ableton MCP](https://github.com/ahujasid/ableton-mcp)

Агент собирает аранжировку в Ableton Live. Звуковой аналог того, что Palmier делает с видео.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/ahujasid/ableton-mcp |

`music` `daw`

---

## [AntV Chart MCP](https://github.com/antvis/mcp-server-chart)

Агент строит готовый график по данным — двадцать с лишним типов. Картинка для ролика прямо из чата.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/antvis/mcp-server-chart |

`charts` `dataviz`

---

## [Apify MCP](https://apify.com/)

Тысячи готовых скрейперов под соцсети и маркетплейсы, дёргаются как инструменты агента.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |

`scraping` `social`

---

## [Blender MCP](https://github.com/ahujasid/blender-mcp)

Агент строит и рендерит 3D-сцену прямо в Blender. Тот же приём, что у Palmier, только для трёхмерки.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/ahujasid/blender-mcp |

`3d` `blender`

---

## [Brandfetch MCP](https://brandfetch.com/) ⭐

Логотипы брендов в SVG (light/dark) плюс фирменные цвета и шрифты по одному домену.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | нужен — [получить](https://developers.brandfetch.com/) |

```bash
uvx --from git+https://github.com/djmoore711/brandfetch-mcp mcp-brandfetch
```

Переменные окружения: `BRANDFETCH_API_KEY`. Держи их в конфиге агента, не в репозитории.

`logo` `branding`

---

## [Brave Search MCP](https://brave.com/search/api/)

Поиск по вебу и картинкам без Google. Есть бесплатный тариф.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | нужен — [получить](https://api-dashboard.search.brave.com/app/keys) |

```bash
npx -y @brave/brave-search-mcp-server@latest
```

Переменные окружения: `BRAVE_API_KEY`. Держи их в конфиге агента, не в репозитории.

`search`

---

## [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)

Консоль, сеть и профайлер живой страницы для агента. Полезно, когда Remotion-превью тормозит и непонятно где.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/ChromeDevTools/chrome-devtools-mcp |

`debugging` `browser`

---

## [Context7](https://context7.com/)

Подсовывает агенту актуальную документацию библиотеки. Лечит выдуманные API у Remotion и three.js.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | необязателен |

`docs` `coding`

---

## [Coverr MCP](https://coverr.co/) ⭐

B-roll в MP4 прямо из чата: `get_videos` → `get_video(id)` → готовый 1080p-линк.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `MCP` |
| **API-ключ** | нужен — [получить](https://coverr.co/) |

```bash
claude mcp add --transport http coverr https://mcp.coverr.co/mcp
```

`b-roll` `video` `stock`

---

## [Docker MCP Catalog](https://hub.docker.com/mcp)

MCP-серверы в контейнерах: ставятся без npm и uv и не тащат зависимости в систему.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `MCP` |

`mcp` `docker` `registry`

---

## [ElevenLabs MCP](https://github.com/elevenlabs/elevenlabs-mcp)

Официальный сервер: озвучка, звуковые эффекты и клонирование голоса прямо из чата.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | нужен — [получить](https://elevenlabs.io/app/settings/api-keys) |
| **Исходники** | https://github.com/elevenlabs/elevenlabs-mcp |

Переменные окружения: `ELEVENLABS_API_KEY`. Держи их в конфиге агента, не в репозитории.

`tts` `sfx`

---

## [Fetch MCP](https://github.com/modelcontextprotocol/servers) ⭐

Достать и распарсить произвольную страницу. Спасает, когда нужны фото с /press или /newsroom компании.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/modelcontextprotocol/servers |

```bash
uvx mcp-server-fetch
```

`scraping`

---

## [Filesystem MCP](https://github.com/modelcontextprotocol/servers)

Доступ к папке проекта с явными границами. Базовый кирпич, о котором забывают.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/modelcontextprotocol/servers |

```bash
npx -y @modelcontextprotocol/server-filesystem /path/to/project
```

`files`

---

## [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server)

Превращает сайт в чистый markdown. Когда нужен фактурный материал для сценария, а не десять вкладок.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |
| **Исходники** | https://github.com/firecrawl/firecrawl-mcp-server |

Переменные окружения: `FIRECRAWL_API_KEY`. Держи их в конфиге агента, не в репозитории.

`scraping` `research`

---

## [GitHub MCP](https://github.com/github/github-mcp-server)

Официальный сервер: issues, PR, файлы репозитория как инструменты агента.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |
| **Исходники** | https://github.com/github/github-mcp-server |

`github` `workflow`

---

## [HuggingFace Space MCP](https://github.com/evalstate/mcp-hfspace)

Любой Space с Hugging Face становится инструментом агента. Тысячи демо-моделей без своего хостинга.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/evalstate/mcp-hfspace |

`huggingface` `models` `bridge`

---

## [ImageSorcery MCP](https://github.com/sunriseapps/imagesorcery-mcp)

Обрезка, ресайз, детекция объектов на картинке средствами компьютерного зрения — локально.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/sunriseapps/imagesorcery-mcp |

`image-processing` `computer-vision` `local`

---

## [Klipy MCP](https://klipy.com/) ⭐

GIF-поиск. Неожиданно хорошо находит поп-культуру и свежую технику.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | нужен — [получить](https://klipy.com/) |

Переменные окружения: `KLIPY_API_KEY`. Держи их в конфиге агента, не в репозитории.

`gif`

---

## [Memory MCP](https://github.com/modelcontextprotocol/servers)

Граф знаний, переживающий перезапуск сессии. Стиль канала и решения не приходится объяснять заново.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/modelcontextprotocol/servers |

```bash
npx -y @modelcontextprotocol/server-memory
```

`memory` `knowledge-graph`

---

## [Mermaid MCP](https://github.com/hustcc/mcp-mermaid)

Схема по описанию сразу в картинку. Объясняющий кадр без ручного рисования.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/hustcc/mcp-mermaid |

`diagrams` `charts`

---

## [NASA MCP](https://api.nasa.gov/) ⭐

Космос и наука в высоком разрешении. Public domain.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `MCP` |
| **API-ключ** | нужен — [получить](https://api.nasa.gov/) |

```bash
npx -y @programcomputer/nasa-mcp-server@latest
```

Переменные окружения: `NASA_API_KEY`. Держи их в конфиге агента, не в репозитории.

`space` `science` `public-domain`

---

## [Notion MCP](https://developers.notion.com/docs/mcp)

Контент-план и база сценариев в Notion становятся доступны агенту напрямую.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |

`notion` `planning`

---

## [Openverse MCP](https://openverse.org/) ⭐

CC-лицензированные картинки: Flickr, rawpixel, Wikimedia в одном поиске. Ключ не нужен.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `MCP` |

```bash
npx -y mcp-openverse@latest
```

Сохраняй `creator` и `license` вместе с файлом — они понадобятся для атрибуции.

`stock` `creative-commons`

---

## [Palmier Pro](https://palmierai.pro/)

Видеоредактор для macOS, у которого таймлайн выставлен наружу как MCP-сервер — агент правит монтаж сам.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔴 платно |
| **Из агента** | `MCP` |
| **Платформы** | macos |
| **Разбор** | [читать](../guides/palmier-pro.md) |

Поднимает локальный MCP на `http://127.0.0.1:19789/mcp`. Подключаешь Claude Code / Claude Desktop /
Cursor / Codex — и агент видит весь проект: какие клипы на каких дорожках, их длительность,
исходные промпты. Дальше умеет читать таймлайн, добавлять и подрезать клипы, менять порядок,
генерировать новый материал по промпту и перегенерировать уже сделанный.

Ключевая разница с обычным редактором: контекст проекта живёт в том же чате, что и остальные
MCP-серверы. То есть в одном разговоре можно найти сток через Pexels, сгенерировать озвучку
и тут же положить это на таймлайн.

`video-editing` `timeline` `macos`

---

## [Pexels MCP](https://www.pexels.com/api/) ⭐

Стоковые фото и видео. Рабочая лошадка для generic-кадров.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `MCP` |
| **API-ключ** | нужен — [получить](https://www.pexels.com/api/) |

```bash
uvx pexels-mcp-server
```

Переменные окружения: `PEXELS_API_KEY`. Держи их в конфиге агента, не в репозитории.

Для картинок бери размер `large2x` (до ~1880px), а не `original` — иначе упрёшься
в потолок API при массовой выгрузке.

`stock` `photo` `video`

---

## [PiAPI MCP](https://github.com/apinetwork/piapi-mcp-server)

Мост к Midjourney, Kling, Suno и другим закрытым сервисам. Обходит отсутствие у них официального API.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔴 платно |
| **Из агента** | `MCP` |
| **API-ключ** | нужен |
| **Исходники** | https://github.com/apinetwork/piapi-mcp-server |

`bridge` `midjourney` `aggregator`

---

## [Playwright MCP](https://github.com/microsoft/playwright-mcp)

Браузер под управлением агента. Забрать то, к чему нет API, или записать HTML-сцену в кадры.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/microsoft/playwright-mcp |

```bash
npx -y @playwright/mcp@latest
```

`browser` `scraping` `recording`

---

## [Sequential Thinking MCP](https://github.com/modelcontextprotocol/servers)

Заставляет агента разложить задачу по шагам вслух. Заметно помогает на длинных структурах вроде сценария.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/modelcontextprotocol/servers |

```bash
npx -y @modelcontextprotocol/server-sequential-thinking
```

`reasoning` `planning`

---

## [Tavily MCP](https://tavily.com/)

Веб-поиск, заточенный под агентов. С `include_images` вытаскивает реальные фото из новостных статей.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟡 freemium |
| **Из агента** | `MCP` |
| **API-ключ** | нужен — [получить](https://app.tavily.com/) |

```bash
npx -y tavily-mcp@latest
```

Переменные окружения: `TAVILY_API_KEY`. Держи их в конфиге агента, не в репозитории.

`search` `news-photo`

---

## [Unsplash MCP](https://unsplash.com/developers) ⭐

Фото-сток номер два. Картинки красивее, релевантность к запросу слабее, чем у Pexels.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `MCP` |
| **API-ключ** | нужен — [получить](https://unsplash.com/developers) |

```bash
npx -y @violent-madman/unsplash-mcp@latest
```

Переменные окружения: `UNSPLASH_ACCESS_KEY`. Держи их в конфиге агента, не в репозитории.

`stock` `photo`

---

## [Video Editing MCP](https://github.com/burningion/video-editing-mcp)

Поиск по своей видеотеке и сборка нарезки силами агента.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/burningion/video-editing-mcp |

`video` `editing` `search`

---

## [Wikipedia MCP](https://www.wikipedia.org/) ⭐

Лучший первый источник фото для известных сущностей — компаний, людей, продуктов.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `MCP` |

```bash
uvx wikipedia-mcp
```

Сток систематически промахивается по именованным сущностям: на запрос «Liquid Death»
Pexels отдаст абстрактную банку. Wikipedia отдаёт настоящее lead-изображение статьи.

`reference` `photo`

---

## [YouTube MCP](https://github.com/anaisbetts/mcp-youtube)

Скачивает субтитры ролика через yt-dlp. Разбор чужого видео без просмотра.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/anaisbetts/mcp-youtube |

`youtube` `transcript` `research`

---

## [YouTube Transcript MCP](https://github.com/jkawamoto/mcp-youtube-transcript)

Расшифровка чужого ролика в контекст агента. Разбор конкурента без ручного просмотра.

| | |
|---|---|
| **Тип** | MCP-сервер |
| **Цена** | 🔵 open source |
| **Из агента** | `MCP` |
| **Исходники** | https://github.com/jkawamoto/mcp-youtube-transcript |

`youtube` `research` `transcript`

---

