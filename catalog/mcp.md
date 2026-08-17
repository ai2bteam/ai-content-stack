<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# 🔌 MCP-серверы

> Инструменты, подключаемые к агенту по протоколу MCP. Агент управляет ими напрямую — без копипасты и ручного клика.

[← Ко всему каталогу](../README.md)

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

