<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# 🧩 Сборка, монтаж, рендер

> Где всё склеивается в готовый файл.

[← Ко всему каталогу](../README.md)

---

## [CapCut](https://www.capcut.com/)

Быстрый монтаж вертикалок с готовыми эффектами и автосубтитрами. Читай лицензию, если ролик коммерческий.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`shorts` `mobile`

---

## [Creatomate](https://creatomate.com/)

Шаблоны с подстановкой данных через API. Для сотни однотипных роликов, различающихся текстом и картинкой.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`cloud-render` `templates` `api`

---

## [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve)

Профессиональный монтаж и цветокоррекция, бесплатная версия покрывает почти всё. Есть Python-скриптинг.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`editing` `color-grading`

---

## [Editly](https://github.com/mifi/editly)

Видео описывается JSON-конфигом и собирается одной командой. Слайд-шоу и нарезки без единой строки кода.

| | |
|---|---|
| **Тип** | CLI |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/mifi/editly |

`declarative` `json` `cli`

---

## [FFmpeg](https://ffmpeg.org/) ⭐

Фундамент под всем остальным: конвертация, обрезка, склейка, сведение звука, проверка файлов через ffprobe.

| | |
|---|---|
| **Тип** | CLI |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Документация** | https://ffmpeg.org/documentation.html |

`encoding` `editing`

---

## [ffmpeg.wasm](https://ffmpegwasm.netlify.app/)

FFmpeg прямо в браузере. Обрезать и перекодировать без загрузки файла на сервер.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/ffmpegwasm/ffmpeg.wasm |

`browser` `encoding`

---

## [HandBrake](https://handbrake.fr/)

Перекодирование с вменяемыми пресетами. Когда ffmpeg хочется, но не хочется вспоминать флаги.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |

`encoding`

---

## [Kdenlive](https://kdenlive.org/)

Полностью открытый нелинейный монтажёр. Без облака, аккаунта и подписки.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | — |

`editing` `local`

---

## [MediaInfo](https://mediaarea.net/en/MediaInfo)

Разбор контейнера и кодеков файла. Первое, что запускаешь, когда сток не встал в таймлайн.

| | |
|---|---|
| **Тип** | CLI |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |

`inspection` `debugging`

---

## [MoviePy](https://zulko.github.io/moviepy/)

Монтаж на Python, когда React-сцена — избыточно, а голый ffmpeg — уже больно.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/Zulko/moviepy |

`python` `editing`

---

## [OpenShot](https://www.openshot.org/)

Простой открытый монтажёр с Python-библиотекой под капотом — её можно дёргать отдельно.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |

`editing` `python`

---

## [Playwright](https://playwright.dev/) ⭐

Запись HTML/Canvas-сцены в видео через headless-браузер. Мост между веб-анимацией и монтажом.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |

`recording` `headless`

---

## [Remotion](https://www.remotion.dev/) ⭐

Видео как React-компонент. Кадр — чистая функция от номера кадра, поэтому результат детерминирован и его можно ревьюить как код.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🟡 freemium |
| **Из агента** | `CLI` |
| **Документация** | https://www.remotion.dev/docs |
| **Исходники** | https://github.com/remotion-dev/remotion |

Опорный инструмент сборки. Вся анимация идёт через `useCurrentFrame()` + `interpolate()`
или `spring()` — CSS-переходы и CSS-анимации не работают, потому что рендер идёт покадрово,
а не в реальном времени.

Лицензия: бесплатно для физлиц и небольших команд, для компаний нужна платная.
Проверь условия до того, как встроишь в коммерческий пайплайн.

`react` `typescript` `programmatic-video`

---

## [Revideo](https://re.video/)

Форк Motion Canvas, доведённый до программного видео с параметрами. Альтернатива Remotion без его лицензии.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/redotvideo/revideo |

`programmatic` `typescript`

---

## [Shotcut](https://shotcut.org/)

Открытый монтажёр на всех платформах, без установки кодеков.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | — |

`editing` `local`

---

## [Shotstack](https://shotstack.io/)

Рендер видео как облачный API: отправил JSON-таймлайн — получил ссылку на mp4. Своё железо не нужно.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`cloud-render` `json` `api`

---

