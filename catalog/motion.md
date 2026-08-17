<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# ✨ Моушн и анимация

> Движение в кадре: анимационные библиотеки, Lottie/Rive, процедурная графика.

[← Ко всему каталогу](../README.md)

---

## [After Effects](https://www.adobe.com/products/aftereffects.html)

Индустриальный стандарт моушн-графики. Отсюда экспортируется большая часть Lottie-файлов.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔴 платно |
| **Из агента** | — |

`motion-design` `industry-standard`

---

## [ambientCG](https://ambientcg.com/)

Тысячи PBR-текстур в CC0. Дополняет Poly Haven там, где не хватило материала.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `API` |

`3d` `textures` `cc0`

---

## [Anime.js](https://animejs.com/)

Лёгкая библиотека без привязки к фреймворку. Когда Motion избыточен, а голый CSS уже не тянет.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/juliangarnier/anime |

`animation` `javascript`

---

## [Blender](https://www.blender.org/)

Бесплатный 3D-пакет промышленного уровня. Рендерится из командной строки, значит встраивается в конвейер.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |

`3d` `rendering` `cli`

---

## [drei](https://github.com/pmndrs/drei) ⭐

Готовые хелперы к React Three Fiber: камеры, свет, окружение, текст. Экономит сотни строк.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/pmndrs/drei |

`3d` `react` `helpers`

---

## [GSAP](https://gsap.com/)

Ветеран веб-анимации. Таймлайны, морфинг SVG, сложная хореография.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🟢 бесплатно |
| **Из агента** | — |
| **Документация** | https://gsap.com/docs/v3/ |

`animation` `javascript` `timeline`

---

## [Jitter](https://jitter.video/)

Моушн-дизайн в браузере с логикой Figma. Порог входа сильно ниже After Effects.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`motion-design` `browser`

---

## [Konva](https://konvajs.org/)

Canvas со сценой из объектов вместо ручного рисования. Есть готовая обвязка под React.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |

`2d` `canvas` `react`

---

## [Lordicon](https://lordicon.com/)

Анимированные иконки в формате Lottie. Оживляют перечисления, где обычно висит статичный список.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`icons` `lottie`

---

## [Lottie](https://lottiefiles.com/) ⭐

Векторная анимация в JSON. Готовых файлов — сотни тысяч, вставляются в Remotion через @remotion/lottie.

| | |
|---|---|
| **Тип** | формат |
| **Цена** | 🔵 open source |
| **Из агента** | — |

`animation` `vector` `json`

---

## [Manim](https://www.manim.community/)

Движок математических анимаций, тот самый из 3Blue1Brown. Формулы и графы, а не общая моушн-графика.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/ManimCommunity/manim |

`math` `explainer` `python`

---

## [Matter.js](https://brm.io/matter-js/)

Физика 2D: падение, столкновения, гравитация. Движение выглядит естественным без ручных ключей.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/liabru/matter-js |

`physics` `2d`

---

## [Mixamo](https://www.mixamo.com/)

Готовые анимации персонажей с автоматическим риггингом. Бесплатно, от Adobe.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟢 бесплатно |
| **Из агента** | — |

`3d` `character-animation` `free`

---

## [Motion](https://motion.dev/)

Бывший Framer Motion. Анимации для React, ванильного JS и Vue — пружины, жесты, layout-переходы, скролл.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Документация** | https://motion.dev/docs |
| **Исходники** | https://github.com/motiondivision/motion |
| **Разбор** | [читать](../guides/motion.md) |

Гибридный движок: часть работы отдаёт нативным браузерным API, поэтому вывозит 120fps
с GPU-ускорением. Мини-версия `animate()` для HTML/SVG весит 2.3kb, API в среднем
заметно компактнее, чем у GSAP.

Что берём: layout- и shared-layout-переходы, анимация появления/исчезновения,
жесты (drag, tap, hover), скролл-связанные эффекты, таймлайны.

⚠️ Для Remotion-роликов Motion **не** используем напрямую: там кадр рендерится по
`useCurrentFrame()`, а не по часам реального времени. Motion — для лендингов, интерфейсов
и HTML-сцен, которые потом пишутся с экрана.

`animation` `react` `javascript` `vue`

---

## [Motion Canvas](https://motioncanvas.io/)

Анимация кодом с редактором для тонкой настройки таймингов. Заточен под объясняющие ролики.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/motion-canvas/motion-canvas |

`programmatic` `explainer`

---

## [p5.js](https://p5js.org/)

Процедурная графика с минимумом обвязки. Быстрый способ получить уникальный анимированный фон.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/processing/p5.js |

`generative` `canvas`

---

## [PixiJS](https://pixijs.com/)

2D-рендер на WebGL. Тянет тысячи частиц там, где обычный canvas уже начинает захлёбываться.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/pixijs/pixijs |

`2d` `webgl` `particles`

---

## [Poly Haven](https://polyhaven.com/)

HDRI, текстуры и 3D-модели в CC0 — без атрибуции и ограничений. Свет для сцены берут отсюда.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `API` |

`3d` `hdri` `textures` `cc0`

---

## [React Spring](https://www.react-spring.dev/)

Анимации на физике пружин для React. Альтернатива Motion со своим взглядом на API.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/pmndrs/react-spring |

`animation` `react` `spring`

---

## [React Three Fiber](https://github.com/pmndrs/react-three-fiber) ⭐

Three.js как React-компоненты. Именно через него 3D попадает в Remotion-композицию.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/pmndrs/react-three-fiber |

`3d` `react` `webgl`

---

## [Rive](https://rive.app/)

Интерактивная анимация с машиной состояний. Тяжелее Lottie, зато реагирует на события.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`animation` `interactive`

---

## [Rough.js](https://roughjs.com/)

Рисует графику так, будто её набросали от руки. Схема перестаёт выглядеть корпоративным слайдом.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/rough-stuff/rough |

`style` `sketchy` `svg`

---

## [Sketchfab](https://sketchfab.com/)

Готовые 3D-модели в .glb/.gltf, много бесплатных.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`3d` `assets`

---

## [Spline](https://spline.design/)

3D-сцены в браузере без порога входа Blender. Экспортируется в React-компонент.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`3d` `no-code` `react`

---

## [Theatre.js](https://www.theatrejs.com/)

Настоящий таймлайн с ключевыми кадрами прямо в браузере. Анимация настраивается мышкой, а сохраняется в JSON.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/theatre-js/theatre |

`animation` `timeline` `keyframes`

---

## [Three.js](https://threejs.org/) ⭐

3D в браузере. В связке с @remotion/three рендерится покадрово в готовое видео.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/mrdoob/three.js |

`3d` `webgl`

---

