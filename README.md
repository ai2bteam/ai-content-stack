<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# 🧰 AI Content Stack

> Каталог инструментов для производства контента с помощью ИИ — что берём, чем управляем из агента, как ставится.

**192 инструментов · 12 категорий · 28 подключаются к агенту по MCP · 114 бесплатны или open source**

---

## Как этим пользоваться

Каталог отвечает не на вопрос «какие бывают ИИ-инструменты», а на вопрос **«мне нужно вот это — чем делать»**. Поэтому начинай с таблицы [Задача → инструмент](#задача--инструмент), а не с оглавления.

Три правила, которые экономят больше всего времени:

1. **Сначала сток, потом генерация.** Готовый кадр находится за секунды и не ест лимиты. Генерация — это когда стока действительно нет.
2. **Видеоряд важнее статики.** На сцену длиннее трёх секунд ищи MP4 или GIF, а не фотографию с ken burns.
3. **Смотри на колонку «Из агента».** Инструмент с `MCP` встраивается в рабочий чат и не требует переключения контекста — это чаще всего важнее, чем разница в качестве.

## Разборы

Таблицы отвечают на вопрос «чем делать». Там, где важнее понять устройство, есть отдельный разбор:

- **[Motion](guides/motion.md)** — Бывший Framer Motion. Анимации для React, ванильного JS и Vue — пружины, жесты, layout-переходы, скролл.
- **[Palmier Pro](guides/palmier-pro.md)** — Видеоредактор для macOS, у которого таймлайн выставлен наружу как MCP-сервер — агент правит монтаж сам.
- **[Voicebox](guides/voicebox.md)** — Локальная голосовая студия: 7 TTS-движков, 23 языка, клонирование голоса с нескольких секунд записи.

## Задача → инструмент

### Найти готовое

| Задача | Чем делать | Комментарий |
|---|---|---|
| Фото — реальное, живое, generic | [Pexels MCP](https://www.pexels.com/api/) · [Openverse MCP](https://openverse.org/) · [Unsplash MCP](https://unsplash.com/developers) | Сначала Pexels. Openverse — если нужна CC-лицензия с атрибуцией. |
| Фото известной компании, человека, продукта | [Wikipedia MCP](https://www.wikipedia.org/) · [Wikimedia Commons](https://commons.wikimedia.org/) · [Tavily MCP](https://tavily.com/) | Сток тут промахивается. Иди в Wikipedia за lead-изображением статьи. |
| Видео B-roll в MP4 | [Coverr MCP](https://coverr.co/) · [Pexels MCP](https://www.pexels.com/api/) | На каждую сцену длиннее 3 секунд ищи видео, а не статичное фото. |
| GIF | [Klipy MCP](https://klipy.com/) |  |
| Логотип бренда | [Brandfetch MCP](https://brandfetch.com/) | Отдаёт SVG отдельно под светлый и тёмный фон. |
| Космос, наука, съёмка Земли | [NASA MCP](https://api.nasa.gov/) |  |
| Шрифты и иконки | [Google Fonts](https://fonts.google.com/) · [Lucide](https://lucide.dev/) |  |
| 3D-модель | [Sketchfab](https://sketchfab.com/) |  |
| Историческая и архивная фактура | [Internet Archive](https://archive.org/) · [Library of Congress](https://www.loc.gov/) · [Europeana](https://www.europeana.eu/) · [Smithsonian Open Access](https://www.si.edu/openaccess) · [Met Museum Open Access](https://www.metmuseum.org/art/collection) | Большая часть в public domain — то, чего на стоках нет в принципе. |
| Иллюстрации вместо фото | [unDraw](https://undraw.co/) · [Storyset](https://storyset.com/) | У обоих настраивается акцентный цвет — подгоняются под палитру ролика. |

### Сгенерировать, если готового нет

| Задача | Чем делать | Комментарий |
|---|---|---|
| Картинка по тексту | [FLUX](https://blackforestlabs.ai/) · [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) · [NVIDIA NIM](https://build.nvidia.com/) · [Pollinations](https://pollinations.ai/) | Выстраивай в цепочку с фолбэком — бесплатные лимиты кончаются в самый неподходящий момент. |
| Картинка по референсу, инпейнт, локальный контроль | [ComfyUI](https://www.comfy.org/) |  |
| Убрать фон / увеличить разрешение | [rembg](https://github.com/danielgatis/rembg) · [Upscayl](https://github.com/upscayl/upscayl) · [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) · [Magnific](https://magnific.ai/) | Локально — rembg и Upscayl. Magnific дорисовывает детали, но платный. |
| Убрать со стока водяной знак или лишний объект | [IOPaint](https://github.com/Sanster/IOPaint) · [Clipdrop](https://clipdrop.co/) |  |
| Запустить открытую модель, не разворачивая железо | [Replicate](https://replicate.com/) · [fal.ai](https://fal.ai/) | Оплата за секунды инференса. Дешевле, чем поднимать GPU ради одного ролика. |
| Видео по тексту или по картинке | [LTX-Video](https://www.lightricks.com/ltxv) · [Kling AI](https://klingai.com/) · [Runway](https://runwayml.com/) · [ModelsLab Video](https://modelslab.com/) | LTX-Video — если хочется без подписки. Kling — если нужна убедительная физика движения. |
| Говорящий аватар | [HeyGen](https://www.heygen.com/) |  |
| Озвучка — локально и бесплатно | [Voicebox](https://voicebox.sh/) · [Kokoro TTS](https://huggingface.co/hexgrad/Kokoro-82M) · [Chatterbox TTS](https://github.com/resemble-ai/chatterbox) |  |
| Озвучка — максимальное качество | [ElevenLabs](https://elevenlabs.io/) |  |
| Фоновая музыка | [Suno](https://suno.com/) · [ACE-Step](https://github.com/ace-step/ACE-Step) |  |
| Звуковые эффекты | [Freesound](https://freesound.org/) |  |
| Субтитры и тайминги | [Whisper](https://github.com/openai/whisper) |  |

### Собрать ролик

| Задача | Чем делать | Комментарий |
|---|---|---|
| Программная сборка видео | [Remotion](https://www.remotion.dev/) | Кадр — функция от номера кадра. Диффы читаемые, рендер воспроизводимый. |
| Монтаж из чата, руками агента | [Palmier Pro](https://palmierai.pro/) | Единственный в списке редактор, который отдаёт таймлайн наружу по MCP. |
| Нарезка, конвертация, сведение звука | [FFmpeg](https://ffmpeg.org/) · [MoviePy](https://zulko.github.io/moviepy/) |  |
| Записать HTML/Canvas-сцену в видео | [Playwright](https://playwright.dev/) |  |
| Анимация в вебе — лендинг, интерфейс, HTML-сцена | [Motion](https://motion.dev/) · [GSAP](https://gsap.com/) | Для Remotion не подходит: там время идёт по кадрам, а не по часам. |
| Готовая векторная анимация | [Lottie](https://lottiefiles.com/) · [Rive](https://rive.app/) |  |
| 3D в кадре | [Three.js](https://threejs.org/) · [React Three Fiber](https://github.com/pmndrs/react-three-fiber) · [drei](https://github.com/pmndrs/drei) · [Blender](https://www.blender.org/) |  |
| Рендер видео в облаке по API | [Shotstack](https://shotstack.io/) · [Creatomate](https://creatomate.com/) | Когда роликов сотня и они различаются только текстом и картинкой. |
| Объясняющий ролик со схемами и формулами | [Manim](https://www.manim.community/) · [Motion Canvas](https://motioncanvas.io/) |  |

### Переупаковать снятое

| Задача | Чем делать | Комментарий |
|---|---|---|
| Нарезать длинное видео на вертикальные клипы | [OpusClip](https://www.opus.pro/) · [Klap](https://klap.app/) · [Vizard](https://vizard.ai/) | У Klap есть API — только он встраивается в конвейер без ручного захода на сайт. |
| Убрать паузы и слова-паразиты | [auto-editor](https://github.com/WyattBlue/auto-editor) · [Descript](https://www.descript.com/) | auto-editor делает это бесплатно и одной командой. |
| Субтитры с пословным таймингом | [WhisperX](https://github.com/m-bain/whisperX) · [faster-whisper](https://github.com/SYSTRAN/faster-whisper) · [Subtitle Edit](https://www.nikse.dk/subtitleedit) |  |
| Понять, кто из говорящих сказал реплику | [pyannote.audio](https://github.com/pyannote/pyannote-audio) |  |
| Вычистить звук: эхо, шум, разная громкость | [Adobe Podcast Enhance](https://podcast.adobe.com/) · [Auphonic](https://auphonic.com/) · [Demucs](https://github.com/adefossez/demucs) |  |

### Сделать превью

| Задача | Чем делать | Комментарий |
|---|---|---|
| Собрать обложку руками | [Canva](https://www.canva.com/) · [Figma](https://www.figma.com/) · [Photopea](https://www.photopea.com/) |  |
| Нужен читаемый текст внутри картинки | [Ideogram](https://ideogram.ai/) · [Recraft](https://www.recraft.ai/) | Остальные генераторы на тексте до сих пор ломаются. |
| Пачка однотипных обложек из данных | [Satori](https://github.com/vercel/satori) · [ImageMagick](https://imagemagick.org/) · [Photoroom](https://www.photoroom.com/) | Satori рисует превью из JSX — значит, оно генерится из тех же данных, что и ролик. |
| Подобрать палитру | [Coolors](https://coolors.co/) · [Realtime Colors](https://www.realtimecolors.com/) |  |

### Понять, что снимать

| Задача | Чем делать | Комментарий |
|---|---|---|
| Ниши, конкуренты, ключевые слова | [vidIQ](https://vidiq.com/) · [Nexlev](https://nexlev.io/) |  |
| Статистика видео и каналов из первоисточника | [YouTube Data API](https://developers.google.com/youtube/v3) |  |
| Живые данные в кадр — курсы, погода, новости | [Public APIs](https://github.com/public-apis/public-apis) · [CoinGecko API](https://www.coingecko.com/en/api) · [Open-Meteo](https://open-meteo.com/) |  |
| Графики из этих данных | [Recharts](https://recharts.org/) · [Chart.js](https://www.chartjs.org/) · [visx](https://airbnb.io/visx/) · [Apache ECharts](https://echarts.apache.org/) | Recharts — дефолт для React. ECharts — если нужны карты или десятки тысяч точек. |
| Проверить, не поздно ли снимать тему | [Google Trends](https://trends.google.com/) · [Exploding Topics](https://explodingtopics.com/) |  |
| Вопросы, которые люди реально задают | [AnswerThePublic](https://answerthepublic.com/) | Прямой источник заголовков и структуры сценария. |

## Категории

- 🤖 **[Агенты и оркестрация](#cat-agents)** — Среда, из которой всё запускается. Агент читает задачу и сам дёргает нужные инструменты. _(9)_
- 🔌 **[MCP-серверы](#cat-mcp)** — Инструменты, подключаемые к агенту по протоколу MCP. Агент управляет ими напрямую — без копипасты и ручного клика. _(20)_
- 🎬 **[Генерация видео](#cat-video)** — text→video и image→video. Основной расходник — деньги и время рендера, поэтому сначала смотри, нет ли готового стока. _(19)_
- 🖼️ **[Картинки: генерация и редактирование](#cat-image)** — Генерация с нуля, img2img, инпейнт, удаление фона, апскейл. _(22)_
- 🔊 **[Голос, музыка, звук](#cat-audio)** — Озвучка, клонирование голоса, фоновая музыка, SFX, транскрипция. _(27)_
- ✨ **[Моушн и анимация](#cat-motion)** — Движение в кадре: анимационные библиотеки, Lottie/Rive, процедурная графика. _(17)_
- 🧩 **[Сборка, монтаж, рендер](#cat-assembly)** — Где всё склеивается в готовый файл. _(13)_
- ✂️ **[Переупаковка и субтитры](#cat-repurpose)** — Длинное видео в короткие, автонарезка, субтитры, чистка речи. Самый дешёвый способ получить больше контента из уже снятого. _(8)_
- 🎨 **[Превью, обложки, статика](#cat-thumbnail)** — Кадр, который решает, посмотрят ролик или нет. Плюс всё остальное, что не двигается. _(9)_
- 📦 **[Стоки и готовые ассеты](#cat-assets)** — Фото, видео, GIF, шрифты, иконки, логотипы. Правило: сначала сток, потом генерация — быстрее и без лимитов. _(23)_
- 📊 **[Данные для контента](#cat-data)** — Живые цифры для data-driven роликов: курсы, погода, новости, статистика. _(17)_
- 🔍 **[Research и аналитика](#cat-research)** — Что снимать: ниши, конкуренты, ключевики, выбросы по просмотрам. _(8)_

---

<a id="cat-agents"></a>

## 🤖 Агенты и оркестрация

> Среда, из которой всё запускается. Агент читает задачу и сам дёргает нужные инструменты.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview)** | Собрать своего агента с тем же циклом инструментов, что у Claude Code. | библиотека | 🔴 платно | `API` | нужен |
| **[Claude Code](https://claude.com/product/claude-code)** ⭐ | Агент в терминале, десктопе, вебе и IDE. Точка входа во весь остальной стек. | приложение | 🔴 платно | — | — |
| **[ComfyUI API](https://docs.comfy.org/)** | У локального ComfyUI есть HTTP-эндпоинт: агент кидает граф в очередь и забирает готовый файл. | API | 🔵 open source | `API` | — |
| **[Cursor](https://cursor.com/)** | Редактор кода с агентом внутри. Понимает MCP, поэтому тот же Palmier или Blender цепляются и сюда. | приложение | 🟡 freemium | `MCP` | — |
| **[Make](https://www.make.com/)** | То же, что n8n, но как сервис и без своего сервера. Дороже на объёме, дешевле на старте. | сервис | 🟡 freemium | `API` | — |
| **[MCP Registry](https://github.com/modelcontextprotocol/registry)** | Официальный реестр MCP-серверов. В отличие от сторонних каталогов — источник, а не витрина. | справочник | 🔵 open source | — | — |
| **[Model Context Protocol](https://modelcontextprotocol.io/)** ⭐ | Открытый протокол, по которому агент получает чужие инструменты. Причина, по которой этот каталог вообще имеет смысл. | протокол | 🔵 open source | — | — |
| **[n8n](https://n8n.io/)** | Визуальные автоматизации, которые можно хостить у себя. Держит контент-конвейер: вышел ролик — разошлось по площадкам. | приложение | 🟡 freemium | `API` | — |
| **[Smithery](https://smithery.ai/)** | Каталог MCP-серверов с установкой в одну команду. Первое место, куда идти за «а есть ли MCP для...». | сервис | 🟢 бесплатно | `MCP` | — |

→ [Подробные карточки: установка, ключи, заметки](catalog/agents.md)

<a id="cat-mcp"></a>

## 🔌 MCP-серверы

> Инструменты, подключаемые к агенту по протоколу MCP. Агент управляет ими напрямую — без копипасты и ручного клика.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[Apify MCP](https://apify.com/)** | Тысячи готовых скрейперов под соцсети и маркетплейсы, дёргаются как инструменты агента. | MCP-сервер | 🟡 freemium | `MCP` | нужен |
| **[Blender MCP](https://github.com/ahujasid/blender-mcp)** | Агент строит и рендерит 3D-сцену прямо в Blender. Тот же приём, что у Palmier, только для трёхмерки. | MCP-сервер | 🔵 open source | `MCP` | — |
| **[Brandfetch MCP](https://brandfetch.com/)** ⭐ | Логотипы брендов в SVG (light/dark) плюс фирменные цвета и шрифты по одному домену. | MCP-сервер | 🟡 freemium | `MCP` | нужен |
| **[Brave Search MCP](https://brave.com/search/api/)** | Поиск по вебу и картинкам без Google. Есть бесплатный тариф. | MCP-сервер | 🟡 freemium | `MCP` | нужен |
| **[Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)** | Консоль, сеть и профайлер живой страницы для агента. Полезно, когда Remotion-превью тормозит и непонятно где. | MCP-сервер | 🔵 open source | `MCP` | — |
| **[Context7](https://context7.com/)** | Подсовывает агенту актуальную документацию библиотеки. Лечит выдуманные API у Remotion и three.js. | MCP-сервер | 🟡 freemium | `MCP` | опц. |
| **[Coverr MCP](https://coverr.co/)** ⭐ | B-roll в MP4 прямо из чата: `get_videos` → `get_video(id)` → готовый 1080p-линк. | MCP-сервер | 🟢 бесплатно | `MCP` | нужен |
| **[ElevenLabs MCP](https://github.com/elevenlabs/elevenlabs-mcp)** | Официальный сервер: озвучка, звуковые эффекты и клонирование голоса прямо из чата. | MCP-сервер | 🟡 freemium | `MCP` | нужен |
| **[Fetch MCP](https://github.com/modelcontextprotocol/servers)** ⭐ | Достать и распарсить произвольную страницу. Спасает, когда нужны фото с /press или /newsroom компании. | MCP-сервер | 🟢 бесплатно | `MCP` | — |
| **[Filesystem MCP](https://github.com/modelcontextprotocol/servers)** | Доступ к папке проекта с явными границами. Базовый кирпич, о котором забывают. | MCP-сервер | 🔵 open source | `MCP` | — |
| **[Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server)** | Превращает сайт в чистый markdown. Когда нужен фактурный материал для сценария, а не десять вкладок. | MCP-сервер | 🟡 freemium | `MCP` | нужен |
| **[Klipy MCP](https://klipy.com/)** ⭐ | GIF-поиск. Неожиданно хорошо находит поп-культуру и свежую технику. | MCP-сервер | 🟡 freemium | `MCP` | нужен |
| **[NASA MCP](https://api.nasa.gov/)** ⭐ | Космос и наука в высоком разрешении. Public domain. | MCP-сервер | 🟢 бесплатно | `MCP` | нужен |
| **[Openverse MCP](https://openverse.org/)** ⭐ | CC-лицензированные картинки: Flickr, rawpixel, Wikimedia в одном поиске. Ключ не нужен. | MCP-сервер | 🟢 бесплатно | `MCP` | — |
| **[Palmier Pro](https://palmierai.pro/)** | Видеоредактор для macOS, у которого таймлайн выставлен наружу как MCP-сервер — агент правит монтаж сам. | приложение | 🔴 платно | `MCP` | — |
| **[Pexels MCP](https://www.pexels.com/api/)** ⭐ | Стоковые фото и видео. Рабочая лошадка для generic-кадров. | MCP-сервер | 🟢 бесплатно | `MCP` | нужен |
| **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** | Браузер под управлением агента. Забрать то, к чему нет API, или записать HTML-сцену в кадры. | MCP-сервер | 🔵 open source | `MCP` | — |
| **[Tavily MCP](https://tavily.com/)** | Веб-поиск, заточенный под агентов. С `include_images` вытаскивает реальные фото из новостных статей. | MCP-сервер | 🟡 freemium | `MCP` | нужен |
| **[Unsplash MCP](https://unsplash.com/developers)** ⭐ | Фото-сток номер два. Картинки красивее, релевантность к запросу слабее, чем у Pexels. | MCP-сервер | 🟢 бесплатно | `MCP` | нужен |
| **[Wikipedia MCP](https://www.wikipedia.org/)** ⭐ | Лучший первый источник фото для известных сущностей — компаний, людей, продуктов. | MCP-сервер | 🟢 бесплатно | `MCP` | — |

→ [Подробные карточки: установка, ключи, заметки](catalog/mcp.md)

<a id="cat-video"></a>

## 🎬 Генерация видео

> text→video и image→video. Основной расходник — деньги и время рендера, поэтому сначала смотри, нет ли готового стока.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[CogVideoX](https://github.com/THUDM/CogVideo)** | Открытая модель, которая заводится на потребительской видеокарте. Порог входа ниже, чем у остальных. | модель | 🔵 open source | `CLI` | — |
| **[fal.ai](https://fal.ai/)** | Быстрый инференс десятков видео- и картиночных моделей под одним API. Не надо разворачивать своё железо. | API | 🔴 платно | `API` | нужен |
| **[Google Veo](https://deepmind.google/models/veo/)** | Генерирует видео сразу со звуком — редкость среди моделей. Доступна через Gemini API и Vertex AI. | сервис | 🔴 платно | `API` | нужен |
| **[Hailuo (MiniMax)](https://hailuoai.video/)** | Заметно дешевле западных аналогов при сопоставимом движении. Считается по кредитам. | сервис | 🟡 freemium | `API` | нужен |
| **[Hedra](https://www.hedra.com/)** | Оживляет статичный портрет под звуковую дорожку. Дешевле полноценного аватара, если нужен один говорящий персонаж. | сервис | 🟡 freemium | `API` | нужен |
| **[HeyGen](https://www.heygen.com/)** | Говорящие аватары и липсинк. Для форматов, где нужен «человек в кадре» без съёмки. | сервис | 🔴 платно | `API` | нужен |
| **[HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo)** | Открытые веса от Tencent. Крутится локально, если есть видеокарта, и не считает кредиты. | модель | 🔵 open source | `CLI` | — |
| **[Kling AI](https://klingai.com/)** | Сильная физика движения и длинные планы. Один из лучших вариантов для реалистичного B-roll. | сервис | 🔴 платно | `API` | нужен |
| **[LTX-Video](https://www.lightricks.com/ltxv)** | Открытая модель text→video и image→video от Lightricks. Гоняется локально или в облаке. | модель | 🔵 open source | `API` | — |
| **[Luma Dream Machine](https://lumalabs.ai/dream-machine)** | Хорошо держит движение камеры: наезды, облёты, проходы. Есть бесплатный тариф на попробовать. | сервис | 🟡 freemium | `API` | нужен |
| **[Mochi 1](https://github.com/genmoai/mochi)** | Apache-2.0 и сильная физика движения. Один из немногих открытых вариантов с честно свободной лицензией. | модель | 🔵 open source | `CLI` | — |
| **[ModelsLab Video](https://modelslab.com/)** | Один API поверх пачки видеомоделей — удобно, когда не хочешь заводить пять аккаунтов. | API | 🔴 платно | `API` | нужен |
| **[Pika](https://pika.art/)** | Ставка на эффекты и трансформации объектов, а не на фотореализм. Для роликов с характером. | сервис | 🟡 freemium | — | — |
| **[Replicate](https://replicate.com/)** | Запуск почти любой открытой модели по HTTP с оплатой за секунды. Удобно, когда модель нужна разово. | API | 🔴 платно | `API` | нужен |
| **[Runway](https://runwayml.com/)** | Генерация и редактирование видео уровня продакшена. Есть API. | сервис | 🔴 платно | `API` | нужен |
| **[Sora](https://openai.com/sora/)** | Модель OpenAI. Сильна в связности длинного плана — объекты не расползаются к концу клипа. | сервис | 🔴 платно | `API` | нужен |
| **[Synthesia](https://www.synthesia.io/)** | Корпоративные аватары для обучающих роликов. Дорого, зато предсказуемо и с лицензионной чистотой. | сервис | 🔴 платно | `API` | нужен |
| **[Topaz Video AI](https://www.topazlabs.com/topaz-video-ai)** | Апскейл и интерполяция кадров. Вытягивает архивные и низкобитрейтные исходники до 4K. | приложение | 🔴 платно | `CLI` | — |
| **[Wan](https://github.com/Wan-Video/Wan2.1)** | Открытая видеомодель Alibaba. Одна из немногих, что сносно рисует текст в кадре. | модель | 🔵 open source | `CLI` | — |

→ [Подробные карточки: установка, ключи, заметки](catalog/video.md)

<a id="cat-image"></a>

## 🖼️ Картинки: генерация и редактирование

> Генерация с нуля, img2img, инпейнт, удаление фона, апскейл.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[AUTOMATIC1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)** | Классический локальный интерфейс к Stable Diffusion. Расширений больше, чем у всех остальных вместе. | приложение | 🔵 open source | `API` | — |
| **[Clipdrop](https://clipdrop.co/)** | Набор операций одним API: убрать фон, убрать объект, расширить кадр, перерисовать освещение. | сервис | 🟡 freemium | `API` | нужен |
| **[Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/)** ⭐ | Flux Schnell и SD 1.5 по HTTP с щедрым бесплатным лимитом. Ответ приходит base64-PNG. | API | 🟡 freemium | `API` | нужен |
| **[ComfyUI](https://www.comfy.org/)** | Нодовый пайплайн для диффузии локально. Когда нужен контроль, которого нет в чужом API. | приложение | 🔵 open source | `API` | — |
| **[FLUX](https://blackforestlabs.ai/)** ⭐ | Текущий рабочий дефолт для text→image. Schnell — быстрый и бесплатный на большинстве хостингов. | модель | 🟡 freemium | `API` | опц. |
| **[Fooocus](https://github.com/lllyasviel/Fooocus)** | Локальная генерация без настройки сорока параметров. Когда ComfyUI — это перебор. | приложение | 🔵 open source | — | — |
| **[Google AI Studio](https://aistudio.google.com/)** | Доступ к картиночным моделям Gemini, включая редактирование по текстовой инструкции. Есть бесплатный лимит. | API | 🟡 freemium | `API` | нужен |
| **[Ideogram](https://ideogram.ai/)** | Единственный, кто уверенно рисует читаемый текст внутри картинки. Для превью и плашек — незаменим. | сервис | 🟡 freemium | `API` | нужен |
| **[InvokeAI](https://github.com/invoke-ai/InvokeAI)** | Локальная студия с нормальным холстом для инпейнта. Удобнее нодов, когда правишь конкретный кусок кадра. | приложение | 🔵 open source | `API` | — |
| **[IOPaint](https://github.com/Sanster/IOPaint)** | Убрать со стока водяной знак, лишнего человека или логотип. Локально, пакетно, бесплатно. | приложение | 🔵 open source | `CLI` | — |
| **[Krea](https://www.krea.ai/)** | Генерация в реальном времени: правишь промпт — картинка меняется на глазах. Быстрый подбор направления. | сервис | 🟡 freemium | `API` | нужен |
| **[Leonardo AI](https://leonardo.ai/)** | Обучение своих стилей и щедрый бесплатный лимит. Полезно, когда нужна единая эстетика на весь сезон роликов. | сервис | 🟡 freemium | `API` | нужен |
| **[Magnific](https://magnific.ai/)** | Апскейл, который дорисовывает детали, а не просто растягивает. Лучший результат в категории и самая высокая цена. | сервис | 🔴 платно | `API` | нужен |
| **[Midjourney](https://www.midjourney.com/)** | До сих пор эталон по художественности кадра. Официального API нет — в пайплайн автоматом не вставить. | сервис | 🔴 платно | — | — |
| **[NVIDIA NIM](https://build.nvidia.com/)** ⭐ | Бесплатные кредиты на генеративные модели. Хорош как первое звено фолбэк-цепочки. | API | 🟡 freemium | `API` | нужен |
| **[Pollinations](https://pollinations.ai/)** ⭐ | Генерация картинки обычным GET-запросом, без ключа вообще. Последний рубеж фолбэка. | API | 🟢 бесплатно | `API` | — |
| **[Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)** | Апскейл картинок. Спасает сток низкого разрешения перед укладкой в 4K-таймлайн. | модель | 🔵 open source | `CLI` | — |
| **[Recraft](https://www.recraft.ai/)** | Генерирует настоящий вектор в SVG, а не растр. Иконки и иллюстрации масштабируются без потерь. | сервис | 🟡 freemium | `API` | нужен |
| **[rembg](https://github.com/danielgatis/rembg)** | Удаление фона одной командой, локально и бесплатно. | библиотека | 🔵 open source | `CLI` | — |
| **[remove.bg](https://www.remove.bg/)** | Удаление фона одним запросом. Дороже локального rembg, но по краям волос заметно аккуратнее. | API | 🟡 freemium | `API` | нужен |
| **[Stability AI](https://stability.ai/)** | Stable Diffusion от первоисточника: API плюс открытые веса, которые можно унести к себе. | API | 🟡 freemium | `API` | нужен |
| **[Upscayl](https://github.com/upscayl/upscayl)** | Апскейл с человеческим интерфейсом поверх Real-ESRGAN. Готовое приложение вместо возни с командной строкой. | приложение | 🔵 open source | `CLI` | — |

→ [Подробные карточки: установка, ключи, заметки](catalog/image.md)

<a id="cat-audio"></a>

## 🔊 Голос, музыка, звук

> Озвучка, клонирование голоса, фоновая музыка, SFX, транскрипция.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[ACE-Step](https://github.com/ace-step/ACE-Step)** | Открытая модель генерации музыки. Фоновые треки без роялти и без подписки. | модель | 🔵 open source | `CLI` | — |
| **[Adobe Podcast Enhance](https://podcast.adobe.com/)** | Превращает запись из комнаты с эхом в студийную. Иногда переусердствует — слушай результат. | сервис | 🟡 freemium | — | — |
| **[AudioCraft / MusicGen](https://github.com/facebookresearch/audiocraft)** | Открытая генерация музыки и звуков от Meta. Локально, без лимитов и вопросов о правах на результат. | модель | 🔵 open source | `CLI` | — |
| **[Auphonic](https://auphonic.com/)** | Автоматическое выравнивание громкости, шумодав и приведение к вещательным нормам. Есть API. | сервис | 🟡 freemium | `API` | нужен |
| **[Bark](https://github.com/suno-ai/bark)** | Генерирует не только речь, но и смех, вздохи, музыкальный фон. Непредсказуем — зато живой. | модель | 🔵 open source | `CLI` | — |
| **[Cartesia](https://cartesia.ai/)** | Ставка на низкую задержку синтеза. Берут, когда озвучка нужна в реальном времени, а не файлом. | сервис | 🟡 freemium | `API` | нужен |
| **[Chatterbox TTS](https://github.com/resemble-ai/chatterbox)** ⭐ | MIT-лицензия и управление эмоцией. Локальная альтернатива, когда Kokoro звучит слишком ровно. | модель | 🔵 open source | `CLI` | — |
| **[Coqui TTS](https://github.com/coqui-ai/TTS)** | Библиотека с десятками моделей и рецептами обучения. Компания закрылась, код остался и работает. | библиотека | 🔵 open source | `CLI` | — |
| **[Demucs](https://github.com/adefossez/demucs)** | Разбирает трек на голос, барабаны, бас и остальное. Вытащить чистую речь из записи с музыкой. | модель | 🔵 open source | `CLI` | — |
| **[ElevenLabs](https://elevenlabs.io/)** ⭐ | Эталон качества синтеза речи. Дорого, но по интонации пока никто не догнал. | сервис | 🟡 freemium | `API` | нужен |
| **[F5-TTS](https://github.com/SWivid/F5-TTS)** | Клонирование голоса по короткому сэмплу с внятной интонацией. Держится в топе открытых моделей. | модель | 🔵 open source | `CLI` | — |
| **[faster-whisper](https://github.com/SYSTRAN/faster-whisper)** | Тот же Whisper, но в разы быстрее и экономнее по памяти. На длинных роликах разница в десятки минут. | библиотека | 🔵 open source | `CLI` | — |
| **[Fish Speech](https://github.com/fishaudio/fish-speech)** | Открытый многоязычный TTS с клонированием. Один из лучших вариантов для русского среди локальных. | модель | 🔵 open source | `CLI` | — |
| **[Freesound](https://freesound.org/)** | Библиотека SFX под Creative Commons. Есть API. | API | 🟢 бесплатно | `API` | нужен |
| **[Kokoro TTS](https://huggingface.co/hexgrad/Kokoro-82M)** ⭐ | 82M параметров, Apache-2.0, крутится на CPU. Лучшее соотношение «качество / вес» для локальной озвучки. | модель | 🔵 open source | `CLI` | — |
| **[OpenVoice](https://github.com/myshell-ai/OpenVoice)** | Переносит тембр и эмоцию на другой язык. Один диктор — и русская, и английская версия ролика. | модель | 🔵 open source | `CLI` | — |
| **[Piper](https://github.com/OHF-Voice/piper1-gpl)** | Очень быстрый TTS, работает даже на Raspberry Pi. Голос простоватый, зато синтез почти мгновенный. | модель | 🔵 open source | `CLI` | — |
| **[PlayAI](https://www.playht.com/)** | Большая библиотека готовых голосов и клонирование. Основной конкурент ElevenLabs по цене. | сервис | 🟡 freemium | `API` | нужен |
| **[Resemble AI](https://www.resemble.ai/)** | Клонирование голоса с упором на юридическую чистоту и водяные знаки в синтезе. | сервис | 🔴 платно | `API` | нужен |
| **[Stable Audio](https://stableaudio.com/)** | Инструментальные треки и звуковые текстуры под заданный хронометраж — важно, когда музыка ложится в тайминг сцены. | сервис | 🟡 freemium | `API` | нужен |
| **[Suno](https://suno.com/)** | Генерация музыки с вокалом по текстовому описанию. | сервис | 🟡 freemium | — | — |
| **[Udio](https://www.udio.com/)** | Генерация музыки с вокалом. Главный конкурент Suno, местами чище сводит. | сервис | 🟡 freemium | — | — |
| **[Voicebox](https://voicebox.sh/)** | Локальная голосовая студия: 7 TTS-движков, 23 языка, клонирование голоса с нескольких секунд записи. | приложение | 🔵 open source | — | — |
| **[Whisper](https://github.com/openai/whisper)** ⭐ | Транскрипция и тайминги. Из него же получаются субтитры под автоматическую нарезку. | модель | 🔵 open source | `CLI` | — |
| **[whisper.cpp](https://github.com/ggml-org/whisper.cpp)** | Whisper на C++ без Python и CUDA. На Apple Silicon летает через Metal. | библиотека | 🔵 open source | `CLI` | — |
| **[WhisperX](https://github.com/m-bain/whisperX)** | Whisper с пословными таймингами и разделением говорящих. То, из чего собираются караоке-субтитры. | библиотека | 🔵 open source | `CLI` | — |
| **[Zapsplat](https://www.zapsplat.com/)** | Большая библиотека SFX с бесплатным тарифом при указании авторства. | сервис | 🟡 freemium | — | — |

→ [Подробные карточки: установка, ключи, заметки](catalog/audio.md)

<a id="cat-motion"></a>

## ✨ Моушн и анимация

> Движение в кадре: анимационные библиотеки, Lottie/Rive, процедурная графика.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[Anime.js](https://animejs.com/)** | Лёгкая библиотека без привязки к фреймворку. Когда Motion избыточен, а голый CSS уже не тянет. | библиотека | 🔵 open source | — | — |
| **[Blender](https://www.blender.org/)** | Бесплатный 3D-пакет промышленного уровня. Рендерится из командной строки, значит встраивается в конвейер. | приложение | 🔵 open source | `CLI` | — |
| **[drei](https://github.com/pmndrs/drei)** ⭐ | Готовые хелперы к React Three Fiber: камеры, свет, окружение, текст. Экономит сотни строк. | библиотека | 🔵 open source | — | — |
| **[GSAP](https://gsap.com/)** | Ветеран веб-анимации. Таймлайны, морфинг SVG, сложная хореография. | библиотека | 🟢 бесплатно | — | — |
| **[Lordicon](https://lordicon.com/)** | Анимированные иконки в формате Lottie. Оживляют перечисления, где обычно висит статичный список. | сервис | 🟡 freemium | — | — |
| **[Lottie](https://lottiefiles.com/)** ⭐ | Векторная анимация в JSON. Готовых файлов — сотни тысяч, вставляются в Remotion через @remotion/lottie. | формат | 🔵 open source | — | — |
| **[Manim](https://www.manim.community/)** | Движок математических анимаций, тот самый из 3Blue1Brown. Формулы и графы, а не общая моушн-графика. | библиотека | 🔵 open source | `CLI` | — |
| **[Motion](https://motion.dev/)** | Бывший Framer Motion. Анимации для React, ванильного JS и Vue — пружины, жесты, layout-переходы, скролл. | библиотека | 🔵 open source | — | — |
| **[Motion Canvas](https://motioncanvas.io/)** | Анимация кодом с редактором для тонкой настройки таймингов. Заточен под объясняющие ролики. | библиотека | 🔵 open source | `CLI` | — |
| **[p5.js](https://p5js.org/)** | Процедурная графика с минимумом обвязки. Быстрый способ получить уникальный анимированный фон. | библиотека | 🔵 open source | — | — |
| **[React Spring](https://www.react-spring.dev/)** | Анимации на физике пружин для React. Альтернатива Motion со своим взглядом на API. | библиотека | 🔵 open source | — | — |
| **[React Three Fiber](https://github.com/pmndrs/react-three-fiber)** ⭐ | Three.js как React-компоненты. Именно через него 3D попадает в Remotion-композицию. | библиотека | 🔵 open source | — | — |
| **[Rive](https://rive.app/)** | Интерактивная анимация с машиной состояний. Тяжелее Lottie, зато реагирует на события. | приложение | 🟡 freemium | — | — |
| **[Sketchfab](https://sketchfab.com/)** | Готовые 3D-модели в .glb/.gltf, много бесплатных. | сервис | 🟡 freemium | — | — |
| **[Spline](https://spline.design/)** | 3D-сцены в браузере без порога входа Blender. Экспортируется в React-компонент. | приложение | 🟡 freemium | — | — |
| **[Theatre.js](https://www.theatrejs.com/)** | Настоящий таймлайн с ключевыми кадрами прямо в браузере. Анимация настраивается мышкой, а сохраняется в JSON. | библиотека | 🔵 open source | — | — |
| **[Three.js](https://threejs.org/)** ⭐ | 3D в браузере. В связке с @remotion/three рендерится покадрово в готовое видео. | библиотека | 🔵 open source | — | — |

→ [Подробные карточки: установка, ключи, заметки](catalog/motion.md)

<a id="cat-assembly"></a>

## 🧩 Сборка, монтаж, рендер

> Где всё склеивается в готовый файл.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[CapCut](https://www.capcut.com/)** | Быстрый монтаж вертикалок с готовыми эффектами и автосубтитрами. Читай лицензию, если ролик коммерческий. | приложение | 🟡 freemium | — | — |
| **[Creatomate](https://creatomate.com/)** | Шаблоны с подстановкой данных через API. Для сотни однотипных роликов, различающихся текстом и картинкой. | API | 🔴 платно | `API` | нужен |
| **[DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve)** | Профессиональный монтаж и цветокоррекция, бесплатная версия покрывает почти всё. Есть Python-скриптинг. | приложение | 🟡 freemium | — | — |
| **[Editly](https://github.com/mifi/editly)** | Видео описывается JSON-конфигом и собирается одной командой. Слайд-шоу и нарезки без единой строки кода. | CLI | 🔵 open source | `CLI` | — |
| **[FFmpeg](https://ffmpeg.org/)** ⭐ | Фундамент под всем остальным: конвертация, обрезка, склейка, сведение звука, проверка файлов через ffprobe. | CLI | 🔵 open source | `CLI` | — |
| **[HandBrake](https://handbrake.fr/)** | Перекодирование с вменяемыми пресетами. Когда ffmpeg хочется, но не хочется вспоминать флаги. | приложение | 🔵 open source | `CLI` | — |
| **[Kdenlive](https://kdenlive.org/)** | Полностью открытый нелинейный монтажёр. Без облака, аккаунта и подписки. | приложение | 🔵 open source | — | — |
| **[MediaInfo](https://mediaarea.net/en/MediaInfo)** | Разбор контейнера и кодеков файла. Первое, что запускаешь, когда сток не встал в таймлайн. | CLI | 🔵 open source | `CLI` | — |
| **[MoviePy](https://zulko.github.io/moviepy/)** | Монтаж на Python, когда React-сцена — избыточно, а голый ffmpeg — уже больно. | библиотека | 🔵 open source | `CLI` | — |
| **[Playwright](https://playwright.dev/)** ⭐ | Запись HTML/Canvas-сцены в видео через headless-браузер. Мост между веб-анимацией и монтажом. | библиотека | 🔵 open source | `CLI` | — |
| **[Remotion](https://www.remotion.dev/)** ⭐ | Видео как React-компонент. Кадр — чистая функция от номера кадра, поэтому результат детерминирован и его можно ревьюить как код. | библиотека | 🟡 freemium | `CLI` | — |
| **[Revideo](https://re.video/)** | Форк Motion Canvas, доведённый до программного видео с параметрами. Альтернатива Remotion без его лицензии. | библиотека | 🔵 open source | `CLI` | — |
| **[Shotstack](https://shotstack.io/)** | Рендер видео как облачный API: отправил JSON-таймлайн — получил ссылку на mp4. Своё железо не нужно. | API | 🔴 платно | `API` | нужен |

→ [Подробные карточки: установка, ключи, заметки](catalog/assembly.md)

<a id="cat-repurpose"></a>

## ✂️ Переупаковка и субтитры

> Длинное видео в короткие, автонарезка, субтитры, чистка речи. Самый дешёвый способ получить больше контента из уже снятого.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[auto-editor](https://github.com/WyattBlue/auto-editor)** | Вырезает тишину и паузы одной командой. Бесплатно делает то, за что подписочные сервисы берут деньги. | CLI | 🔵 open source | `CLI` | — |
| **[Captions](https://www.captions.ai/)** | Субтитры, коррекция взгляда в камеру и дубляж в одном приложении. Заточен под говорящую голову. | сервис | 🟡 freemium | — | — |
| **[Descript](https://www.descript.com/)** | Монтаж правкой текста расшифровки: удалил слово — исчезло из видео. Плюс вычистка «эээ» одной кнопкой. | приложение | 🟡 freemium | — | — |
| **[Klap](https://klap.app/)** | То же, что OpusClip, но с API — встраивается в конвейер, а не требует захода на сайт. | сервис | 🔴 платно | `API` | нужен |
| **[OpusClip](https://www.opus.pro/)** | Режет длинное видео на вертикальные клипы и сам выбирает сильные моменты. Самый известный в категории. | сервис | 🟡 freemium | — | — |
| **[pyannote.audio](https://github.com/pyannote/pyannote-audio)** | Определяет, кто и когда говорит. Нужно, если в кадре двое и субтитры должны различать реплики. | библиотека | 🔵 open source | `CLI` | — |
| **[Subtitle Edit](https://www.nikse.dk/subtitleedit)** | Открытый редактор субтитров: синхронизация, конвертация форматов, вычитка после Whisper. | приложение | 🔵 open source | — | — |
| **[Vizard](https://vizard.ai/)** | Нарезка на клипы с уклоном в многоязычные субтитры. | сервис | 🟡 freemium | — | — |

→ [Подробные карточки: установка, ключи, заметки](catalog/repurpose.md)

<a id="cat-thumbnail"></a>

## 🎨 Превью, обложки, статика

> Кадр, который решает, посмотрят ролик или нет. Плюс всё остальное, что не двигается.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[Canva](https://www.canva.com/)** | Быстрая сборка превью по шаблону. Есть MCP-сервер, так что часть работы уходит агенту. | сервис | 🟡 freemium | `MCP` | — |
| **[Coolors](https://coolors.co/)** | Подбор палитры за полминуты. Помогает удержать правило «один акцентный цвет на ролик». | сервис | 🟡 freemium | — | — |
| **[Figma](https://www.figma.com/)** | Если превью делается по жёсткой сетке, здесь она живёт как компонент — и не разъезжается от ролика к ролику. | сервис | 🟡 freemium | `MCP` | — |
| **[GIMP](https://www.gimp.org/)** | Открытый редактор со скриптовым движком. Пакетная обработка обложек без подписки. | приложение | 🔵 open source | `CLI` | — |
| **[ImageMagick](https://imagemagick.org/)** ⭐ | Ресайз, кроп, наложение текста и композиция из терминала. То же, чем ffmpeg является для видео. | CLI | 🔵 open source | `CLI` | — |
| **[Photopea](https://www.photopea.com/)** | Photoshop в браузере, бесплатно и с поддержкой PSD. Открыть чужой макет, ничего не покупая. | приложение | 🟢 бесплатно | — | — |
| **[Photoroom](https://www.photoroom.com/)** | Вырезать объект и посадить на новый фон — пакетно, через API. Конвейер для однотипных обложек. | сервис | 🟡 freemium | `API` | нужен |
| **[Realtime Colors](https://www.realtimecolors.com/)** | Примеряет палитру сразу на макет, а не на голые квадратики. Сразу видно, читается ли текст. | сервис | 🟢 бесплатно | — | — |
| **[Satori](https://github.com/vercel/satori)** | Превращает JSX в SVG и дальше в PNG. Превью описывается кодом — значит, генерится пачками из данных ролика. | библиотека | 🔵 open source | `CLI` | — |

→ [Подробные карточки: установка, ключи, заметки](catalog/thumbnail.md)

<a id="cat-assets"></a>

## 📦 Стоки и готовые ассеты

> Фото, видео, GIF, шрифты, иконки, логотипы. Правило: сначала сток, потом генерация — быстрее и без лимитов.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[Coverr](https://coverr.co/)** ⭐ | Только видео, только B-roll. 1080p MP4 без водяных знаков. | API | 🟢 бесплатно | `MCP` | нужен |
| **[Europeana](https://www.europeana.eu/)** | Оцифрованные коллекции европейских музеев и библиотек. Историческая фактура с понятными лицензиями. | API | 🟢 бесплатно | `API` | нужен |
| **[Fontshare](https://www.fontshare.com/)** | Качественные шрифты бесплатно для коммерческого использования. Выглядит дороже Google Fonts. | сервис | 🟢 бесплатно | — | — |
| **[Fontsource](https://fontsource.org/)** | Открытые шрифты как npm-пакеты. Ставятся в проект и не зависят от чужого CDN при рендере. | библиотека | 🔵 open source | `CLI` | — |
| **[GDELT](https://www.gdeltproject.org/)** | Глобальный индекс новостных изображений. Ключ не нужен, но жёсткий лимит — 1 запрос в 5 секунд. | API | 🟢 бесплатно | `API` | — |
| **[Google Fonts](https://fonts.google.com/)** ⭐ | Шрифты под любой проект. В Remotion подключаются через @remotion/google-fonts без возни с загрузкой. | сервис | 🟢 бесплатно | `API` | — |
| **[Heroicons](https://heroicons.com/)** | Аккуратный небольшой набор иконок от авторов Tailwind. Два начертания, ничего лишнего. | библиотека | 🔵 open source | — | — |
| **[Internet Archive](https://archive.org/)** | Архивное видео, аудио и печать, огромный пласт в public domain. Источник фактуры, которой нет на стоках. | API | 🟢 бесплатно | `API` | — |
| **[Library of Congress](https://www.loc.gov/)** | Исторические фото, карты, газеты и киноплёнка. Большая часть — public domain. | API | 🟢 бесплатно | `API` | — |
| **[Lucide](https://lucide.dev/)** ⭐ | Чистый набор иконок с React-компонентами из коробки. | библиотека | 🔵 open source | — | — |
| **[Met Museum Open Access](https://www.metmuseum.org/art/collection)** | Коллекция Метрополитен в открытом доступе. API без ключа. | API | 🟢 бесплатно | `API` | — |
| **[Mixkit](https://mixkit.co/)** | Видео, музыка и SFX бесплатно и без атрибуции. Каталог небольшой, но отобранный. | сервис | 🟢 бесплатно | — | — |
| **[Openverse](https://openverse.org/)** ⭐ | Метапоиск по CC-контенту: Flickr, Wikimedia, rawpixel и ещё десяток источников. | API | 🟢 бесплатно | `MCP` | — |
| **[Pexels](https://www.pexels.com/)** ⭐ | Фото и видео без атрибуции. Первый заход за generic-кадрами. | API | 🟢 бесплатно | `API` | нужен |
| **[Phosphor Icons](https://phosphoricons.com/)** | Больше девяти тысяч иконок в шести начертаниях. Берут, когда Lucide не хватает. | библиотека | 🔵 open source | — | — |
| **[Pixabay](https://pixabay.com/)** | Фото, видео, музыка и SFX в одном месте под свободной лицензией. Качество плавает, зато охват широкий. | API | 🟢 бесплатно | `API` | нужен |
| **[Simple Icons](https://simpleicons.org/)** | Логотипы брендов в SVG с фирменными цветами. Бесплатная замена Brandfetch, если нужен только значок. | библиотека | 🔵 open source | `API` | — |
| **[Smithsonian Open Access](https://www.si.edu/openaccess)** | Миллионы изображений в CC0 — предметы, экспонаты, научные съёмки. | API | 🟢 бесплатно | `API` | нужен |
| **[Storyset](https://storyset.com/)** | Иллюстрации, у которых можно менять цвет и композицию, а часть идёт сразу анимированными. | сервис | 🟢 бесплатно | — | — |
| **[Tenor](https://tenor.com/gifapi)** | GIF-API от Google с большим индексом. Альтернатива Klipy, если тот не нашёл. | API | 🟢 бесплатно | `API` | нужен |
| **[unDraw](https://undraw.co/)** | Иллюстрации с настраиваемым акцентным цветом. Подгоняются под палитру ролика прямо на сайте. | сервис | 🟢 бесплатно | — | — |
| **[Videvo](https://www.videvo.net/)** | B-roll и моушн-графика, часть бесплатно. Лицензии разные — смотри у каждого файла. | сервис | 🟡 freemium | — | — |
| **[Wikimedia Commons](https://commons.wikimedia.org/)** ⭐ | Настоящие фотографии реальных объектов и событий. Без ключа, лицензии открытые. | API | 🟢 бесплатно | `API` | — |

→ [Подробные карточки: установка, ключи, заметки](catalog/assets.md)

<a id="cat-data"></a>

## 📊 Данные для контента

> Живые цифры для data-driven роликов: курсы, погода, новости, статистика.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[Alpha Vantage](https://www.alphavantage.co/)** | Котировки акций и индексов с историей. Бесплатный тариф покрывает нужды одного ролика. | API | 🟡 freemium | `API` | нужен |
| **[Apache ECharts](https://echarts.apache.org/)** | Тяжёлая артиллерия: карты, сложные комбинированные графики, большие объёмы точек. | библиотека | 🔵 open source | — | — |
| **[Chart.js](https://www.chartjs.org/)** | Простые графики на canvas. Когда Recharts тянет за собой лишний React-слой. | библиотека | 🔵 open source | — | — |
| **[CoinGecko API](https://www.coingecko.com/en/api)** | Курсы криптовалют. Базовые эндпоинты работают без ключа. | API | 🟡 freemium | `API` | опц. |
| **[D3](https://d3js.org/)** ⭐ | Когда нужен график, которого нет в готовых библиотеках. | библиотека | 🔵 open source | — | — |
| **[Frankfurter](https://frankfurter.dev/)** | Курсы валют по данным ЕЦБ, включая исторические ряды. Без ключа и без лимитов. | API | 🟢 бесплатно | `API` | — |
| **[FRED](https://fred.stlouisfed.org/)** | Экономические ряды ФРБ Сент-Луиса: инфляция, безработица, ставки. Первоисточник, а не пересказ. | API | 🟢 бесплатно | `API` | нужен |
| **[Observable Plot](https://observablehq.com/plot/)** | График описывается одной строкой вместо тридцати. Быстрая разведка данных перед сборкой сцены. | библиотека | 🔵 open source | — | — |
| **[Open-Meteo](https://open-meteo.com/)** | Погода и климатические ряды вообще без регистрации. | API | 🟢 бесплатно | `API` | — |
| **[Our World in Data](https://ourworldindata.org/)** | Готовые выверенные датасеты почти по любой глобальной теме, со ссылками на первоисточники. | справочник | 🟢 бесплатно | `API` | — |
| **[Public APIs](https://github.com/public-apis/public-apis)** ⭐ | Каталог тысяч открытых API. Отсюда берутся живые цифры для data-driven роликов. | справочник | 🟢 бесплатно | — | — |
| **[Recharts](https://recharts.org/)** ⭐ | Графики на React. Внутри Remotion анимируются покадрово — числа растут вместе с кадром. | библиотека | 🔵 open source | — | — |
| **[REST Countries](https://restcountries.com/)** | Флаги, население, площадь, валюты по всем странам. Без ключа, отвечает мгновенно. | API | 🟢 бесплатно | `API` | — |
| **[The Guardian API](https://open-platform.theguardian.com/)** | Полные тексты статей с 1999 года. Один из немногих новостных API, отдающих текст целиком. | API | 🟢 бесплатно | `API` | нужен |
| **[visx](https://airbnb.io/visx/)** | Примитивы D3, обёрнутые в React-компоненты. Полный контроль без ручной возни с DOM. | библиотека | 🔵 open source | — | — |
| **[Wikidata](https://www.wikidata.org/)** | Структурированные факты обо всём, с запросами на SPARQL. Даты, связи, цифры — машиночитаемо. | API | 🟢 бесплатно | `API` | — |
| **[World Bank Data](https://data.worldbank.org/)** | Показатели по странам за десятилетия. Без ключа — годится для сравнительных графиков. | API | 🟢 бесплатно | `API` | — |

→ [Подробные карточки: установка, ключи, заметки](catalog/data.md)

<a id="cat-research"></a>

## 🔍 Research и аналитика

> Что снимать: ниши, конкуренты, ключевики, выбросы по просмотрам.

| Инструмент | Что делает | Тип | Цена | Из агента | Ключ |
|---|---|---|---|---|---|
| **[AnswerThePublic](https://answerthepublic.com/)** | Реальные вопросы людей вокруг темы. Прямой источник заголовков и структуры сценария. | сервис | 🟡 freemium | — | — |
| **[Exploding Topics](https://explodingtopics.com/)** | Темы на подъёме, пока они ещё не в мейнстриме. Ловит волну раньше, чем Trends её покажет. | сервис | 🟡 freemium | — | — |
| **[Google Trends](https://trends.google.com/)** | Сезонность и всплески интереса к теме. Проверить, не поздно ли снимать, до того как писать сценарий. | сервис | 🟢 бесплатно | — | — |
| **[Nexlev](https://nexlev.io/)** ⭐ | База каналов с оценкой дохода, RPM и outlier-скором. Заточен под поиск faceless-ниш. | сервис | 🔴 платно | `MCP` | нужен |
| **[Social Blade](https://socialblade.com/)** | Публичная история роста любого канала. Смотреть чужую динамику, не имея доступа к их аналитике. | сервис | 🟡 freemium | — | — |
| **[TubeBuddy](https://www.tubebuddy.com/)** | Расширение к YouTube Studio: теги, A/B-тесты превью, массовые правки. Основной конкурент vidIQ. | сервис | 🟡 freemium | — | — |
| **[vidIQ](https://vidiq.com/)** ⭐ | Ключевики, конкуренты, оценка заголовков и превью. Есть MCP — research идёт прямо из чата. | сервис | 🟡 freemium | `MCP` | нужен |
| **[YouTube Data API](https://developers.google.com/youtube/v3)** | Первоисточник по статистике видео и каналов. Квоты жёсткие, зато данные не оценочные. | API | 🟢 бесплатно | `API` | нужен |

→ [Подробные карточки: установка, ключи, заметки](catalog/research.md)

---

## Легенда

| Обозначение | Значение |
|---|---|
| ⭐ | Проверено на реальных проектах, а не только внесено в список |
| `MCP` | Подключается к агенту по Model Context Protocol — команды идут из чата |
| `API` | Есть HTTP API, агент дёргает его скриптом |
| `CLI` | Ставится локально, агент вызывает через терминал |
| 🟢 🟡 🔴 🔵 | бесплатно · freemium · платно · open source |

## Что-то отсутствует или устарело

Каталог живёт в двух YAML-файлах, README собирается из них скриптом. Как добавить инструмент — в [CONTRIBUTING.md](CONTRIBUTING.md). Если лень возиться с YAML, просто [заведи issue](https://github.com/ai2bteam/ai-content-stack/issues/new?template=add-tool.yml).

