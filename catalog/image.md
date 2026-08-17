<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# 🖼️ Картинки: генерация и редактирование

> Генерация с нуля, img2img, инпейнт, удаление фона, апскейл.

[← Ко всему каталогу](../README.md)

---

## [Adobe Firefly](https://www.adobe.com/products/firefly.html)

Обучена на лицензионных данных — Adobe даёт правовые гарантии на результат. Важно для коммерческих роликов.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`text-to-image` `commercial-safe`

---

## [Artbreeder](https://www.artbreeder.com/)

Скрещивает и плавно смешивает изображения. Другой способ управления, чем текстовый промпт.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`image-blending` `exploration`

---

## [AUTOMATIC1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

Классический локальный интерфейс к Stable Diffusion. Расширений больше, чем у всех остальных вместе.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/AUTOMATIC1111/stable-diffusion-webui |

`local` `stable-diffusion`

---

## [Clipdrop](https://clipdrop.co/)

Набор операций одним API: убрать фон, убрать объект, расширить кадр, перерисовать освещение.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`image-editing` `background-removal`

---

## [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) ⭐

Flux Schnell и SD 1.5 по HTTP с щедрым бесплатным лимитом. Ответ приходит base64-PNG.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен — [получить](https://dash.cloudflare.com/profile/api-tokens) |

`text-to-image` `image-to-image` `free-tier`

---

## [CodeFormer](https://github.com/sczhou/CodeFormer)

Восстанавливает лица на мыльных и старых снимках. Обязателен при работе с архивными фото.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/sczhou/CodeFormer |

`face-restoration` `archival`

---

## [ComfyUI](https://www.comfy.org/)

Нодовый пайплайн для диффузии локально. Когда нужен контроль, которого нет в чужом API.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/comfyanonymous/ComfyUI |

`local` `workflow` `inpainting`

---

## [Craiyon](https://www.craiyon.com/)

Бывший DALL·E mini: бесплатно и без регистрации. Качество среднее, зато порог нулевой.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`text-to-image` `free` `no-signup`

---

## [DiffusionBee](https://diffusionbee.com/)

Stable Diffusion на Mac одним установщиком. Без Python, командной строки и настройки окружения.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Платформы** | macos |

`local` `macos` `stable-diffusion`

---

## [DreamStudio](https://dreamstudio.ai/)

Официальная веб-оболочка Stability. Попробовать их модели, ничего не разворачивая.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | — |

`text-to-image` `stability`

---

## [FLUX](https://blackforestlabs.ai/) ⭐

Текущий рабочий дефолт для text→image. Schnell — быстрый и бесплатный на большинстве хостингов.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | необязателен |
| **Исходники** | https://github.com/black-forest-labs/flux |

`text-to-image` `open-weights`

---

## [Fooocus](https://github.com/lllyasviel/Fooocus)

Локальная генерация без настройки сорока параметров. Когда ComfyUI — это перебор.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Исходники** | https://github.com/lllyasviel/Fooocus |

`local` `stable-diffusion`

---

## [Freepik](https://www.freepik.com/)

Сток и AI-генерация в одной подписке, с доступом к нескольким чужим моделям через один API.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`stock` `text-to-image` `aggregator`

---

## [GFPGAN](https://github.com/TencentARC/GFPGAN)

Реставрация лиц от Tencent. Даёт результат мягче CodeFormer — сравнивай на своём материале.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/TencentARC/GFPGAN |

`face-restoration` `archival`

---

## [Google AI Studio](https://aistudio.google.com/)

Доступ к картиночным моделям Gemini, включая редактирование по текстовой инструкции. Есть бесплатный лимит.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен — [получить](https://aistudio.google.com/apikey) |

`text-to-image` `image-editing`

---

## [Have I Been Trained?](https://haveibeentrained.com/)

Проверяет, попала ли конкретная работа в обучающие датасеты. Нужно, если работаешь с чужой графикой.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟢 бесплатно |
| **Из агента** | — |

`ethics` `datasets` `rights`

---

## [Ideogram](https://ideogram.ai/)

Единственный, кто уверенно рисует читаемый текст внутри картинки. Для превью и плашек — незаменим.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`text-to-image` `typography`

---

## [InvokeAI](https://github.com/invoke-ai/InvokeAI)

Локальная студия с нормальным холстом для инпейнта. Удобнее нодов, когда правишь конкретный кусок кадра.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/invoke-ai/InvokeAI |

`local` `inpainting`

---

## [IOPaint](https://github.com/Sanster/IOPaint)

Убрать со стока водяной знак, лишнего человека или логотип. Локально, пакетно, бесплатно.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/Sanster/IOPaint |

`inpainting` `cleanup` `local`

---

## [Krea](https://www.krea.ai/)

Генерация в реальном времени: правишь промпт — картинка меняется на глазах. Быстрый подбор направления.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`text-to-image` `realtime`

---

## [Leonardo AI](https://leonardo.ai/)

Обучение своих стилей и щедрый бесплатный лимит. Полезно, когда нужна единая эстетика на весь сезон роликов.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`text-to-image` `style`

---

## [Lexica](https://lexica.art/)

Поиск по миллионам сгенерированных картинок вместе с их промптами. Быстрый способ понять, как просить нужный стиль.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | необязателен |

`prompts` `search` `reference`

---

## [Magnific](https://magnific.ai/)

Апскейл, который дорисовывает детали, а не просто растягивает. Лучший результат в категории и самая высокая цена.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`upscaling`

---

## [Midjourney](https://www.midjourney.com/)

До сих пор эталон по художественности кадра. Официального API нет — в пайплайн автоматом не вставить.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | — |

`text-to-image`

---

## [NVIDIA NIM](https://build.nvidia.com/) ⭐

Бесплатные кредиты на генеративные модели. Хорош как первое звено фолбэк-цепочки.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен — [получить](https://build.nvidia.com/) |

`text-to-image` `free-tier`

---

## [OpenArt](https://openart.ai/)

Библиотека промптов плюс генерация на месте. Полезен как справочник формулировок.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`prompts` `text-to-image`

---

## [Pixlr](https://pixlr.com/)

Браузерный редактор с AI-инструментами. Быстрая правка, когда локально ставить нечего.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`editing` `browser`

---

## [Pollinations](https://pollinations.ai/) ⭐

Генерация картинки обычным GET-запросом, без ключа вообще. Последний рубеж фолбэка.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `API` |
| **Исходники** | https://github.com/pollinations/pollinations |

`text-to-image` `keyless`

---

## [promptoMANIA](https://promptomania.com/)

Конструктор промпта по частям: свет, объектив, стиль. Хорош, пока не выработался свой словарь.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟢 бесплатно |
| **Из агента** | — |

`prompts` `builder`

---

## [PublicPrompts](https://publicprompts.art/)

Бесплатные проверенные промпты под конкретные стили. Готовые рецепты вместо угадывания.

| | |
|---|---|
| **Тип** | справочник |
| **Цена** | 🟢 бесплатно |
| **Из агента** | — |

`prompts` `free`

---

## [Qwen-Image](https://github.com/QwenLM/Qwen-Image)

Открытая модель Alibaba, сильная в тексте внутри картинки — включая нелатиницу.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/QwenLM/Qwen-Image |

`text-to-image` `open-weights` `typography`

---

## [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)

Апскейл картинок. Спасает сток низкого разрешения перед укладкой в 4K-таймлайн.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/xinntao/Real-ESRGAN |

`upscaling`

---

## [Recraft](https://www.recraft.ai/)

Генерирует настоящий вектор в SVG, а не растр. Иконки и иллюстрации масштабируются без потерь.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`text-to-image` `svg` `vector`

---

## [rembg](https://github.com/danielgatis/rembg)

Удаление фона одной командой, локально и бесплатно.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/danielgatis/rembg |

`background-removal`

---

## [remove.bg](https://www.remove.bg/)

Удаление фона одним запросом. Дороже локального rembg, но по краям волос заметно аккуратнее.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен — [получить](https://www.remove.bg/api) |

`background-removal`

---

## [Stability AI](https://stability.ai/)

Stable Diffusion от первоисточника: API плюс открытые веса, которые можно унести к себе.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`text-to-image` `open-weights`

---

## [Upscayl](https://github.com/upscayl/upscayl)

Апскейл с человеческим интерфейсом поверх Real-ESRGAN. Готовое приложение вместо возни с командной строкой.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/upscayl/upscayl |

`upscaling` `local`

---

## [Vectorizer.AI](https://vectorizer.ai/)

Растр в чистый вектор. Логотип из скриншота, который не рассыплется на 4K.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`vectorization` `svg`

---

