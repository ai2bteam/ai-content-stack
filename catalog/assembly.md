<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# 🧩 Сборка, монтаж, рендер

> Где всё склеивается в готовый файл.

[← Ко всему каталогу](../README.md)

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

