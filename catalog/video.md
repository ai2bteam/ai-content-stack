<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# 🎬 Генерация видео

> text→video и image→video. Основной расходник — деньги и время рендера, поэтому сначала смотри, нет ли готового стока.

[← Ко всему каталогу](../README.md)

---

## [CogVideoX](https://github.com/THUDM/CogVideo)

Открытая модель, которая заводится на потребительской видеокарте. Порог входа ниже, чем у остальных.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/THUDM/CogVideo |

`text-to-video` `open-weights` `local`

---

## [fal.ai](https://fal.ai/)

Быстрый инференс десятков видео- и картиночных моделей под одним API. Не надо разворачивать своё железо.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`aggregator` `inference`

---

## [Google Veo](https://deepmind.google/models/veo/)

Генерирует видео сразу со звуком — редкость среди моделей. Доступна через Gemini API и Vertex AI.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`text-to-video` `audio`

---

## [Hailuo (MiniMax)](https://hailuoai.video/)

Заметно дешевле западных аналогов при сопоставимом движении. Считается по кредитам.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`text-to-video` `image-to-video`

---

## [Hedra](https://www.hedra.com/)

Оживляет статичный портрет под звуковую дорожку. Дешевле полноценного аватара, если нужен один говорящий персонаж.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`avatar` `lipsync`

---

## [HeyGen](https://www.heygen.com/)

Говорящие аватары и липсинк. Для форматов, где нужен «человек в кадре» без съёмки.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |
| **Документация** | https://docs.heygen.com/ |

`avatar` `lipsync`

---

## [HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo)

Открытые веса от Tencent. Крутится локально, если есть видеокарта, и не считает кредиты.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/Tencent-Hunyuan/HunyuanVideo |

`text-to-video` `open-weights` `local`

---

## [Kling AI](https://klingai.com/)

Сильная физика движения и длинные планы. Один из лучших вариантов для реалистичного B-roll.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`text-to-video` `image-to-video`

---

## [LTX-Video](https://www.lightricks.com/ltxv)

Открытая модель text→video и image→video от Lightricks. Гоняется локально или в облаке.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/Lightricks/LTX-Video |

`text-to-video` `image-to-video` `open-weights`

---

## [Luma Dream Machine](https://lumalabs.ai/dream-machine)

Хорошо держит движение камеры: наезды, облёты, проходы. Есть бесплатный тариф на попробовать.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`text-to-video` `image-to-video`

---

## [Mochi 1](https://github.com/genmoai/mochi)

Apache-2.0 и сильная физика движения. Один из немногих открытых вариантов с честно свободной лицензией.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/genmoai/mochi |

`text-to-video` `open-weights` `apache-2`

---

## [ModelsLab Video](https://modelslab.com/)

Один API поверх пачки видеомоделей — удобно, когда не хочешь заводить пять аккаунтов.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен — [получить](https://modelslab.com/) |
| **Документация** | https://docs.modelslab.com/ |

`text-to-video` `aggregator`

---

## [Pika](https://pika.art/)

Ставка на эффекты и трансформации объектов, а не на фотореализм. Для роликов с характером.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`text-to-video` `effects`

---

## [Replicate](https://replicate.com/)

Запуск почти любой открытой модели по HTTP с оплатой за секунды. Удобно, когда модель нужна разово.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен — [получить](https://replicate.com/account/api-tokens) |

`aggregator` `inference`

---

## [Runway](https://runwayml.com/)

Генерация и редактирование видео уровня продакшена. Есть API.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен — [получить](https://dev.runwayml.com/) |

`text-to-video` `image-to-video`

---

## [Sora](https://openai.com/sora/)

Модель OpenAI. Сильна в связности длинного плана — объекты не расползаются к концу клипа.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`text-to-video`

---

## [Synthesia](https://www.synthesia.io/)

Корпоративные аватары для обучающих роликов. Дорого, зато предсказуемо и с лицензионной чистотой.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`avatar` `corporate`

---

## [Topaz Video AI](https://www.topazlabs.com/topaz-video-ai)

Апскейл и интерполяция кадров. Вытягивает архивные и низкобитрейтные исходники до 4K.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔴 платно |
| **Из агента** | `CLI` |

`upscaling` `restoration`

---

## [Wan](https://github.com/Wan-Video/Wan2.1)

Открытая видеомодель Alibaba. Одна из немногих, что сносно рисует текст в кадре.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/Wan-Video/Wan2.1 |

`text-to-video` `open-weights`

---

