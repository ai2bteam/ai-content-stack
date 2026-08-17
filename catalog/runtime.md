<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# ⚙️ Модели и где их запускать

> Веса, LoRA и площадки для инференса. Сюда идут, когда чужой сервис не устраивает по цене, приватности или контролю.

[← Ко всему каталогу](../README.md)

---

## [AnimateDiff](https://github.com/guoyww/AnimateDiff)

Оживляет статичную Stable Diffusion-картинку. Работает в ComfyUI, значит встраивается в локальный конвейер.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/guoyww/AnimateDiff |

`image-to-video` `stable-diffusion` `local`

---

## [Civitai](https://civitai.com/)

Чекпойнты и LoRA под конкретные стили. Оттуда берут единую эстетику для всего сезона роликов.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | необязателен |

`models` `lora` `stable-diffusion`

---

## [ControlNet](https://github.com/lllyasviel/ControlNet)

Задаёт генерации позу, глубину или контур. Единственный способ получить нужную композицию, а не лотерею.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/lllyasviel/ControlNet |

`stable-diffusion` `control` `composition`

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

## [Hugging Face](https://huggingface.co/) ⭐

Главный склад открытых моделей и датасетов. Почти всё локальное из этого каталога скачивается отсюда.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | необязателен |

`models` `datasets` `hub`

---

## [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter)

Переносит стиль или лицо с картинки-референса. Держит одного персонажа одинаковым от кадра к кадру.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/tencent-ailab/IP-Adapter |

`stable-diffusion` `style-transfer` `consistency`

---

## [LM Studio](https://lmstudio.ai/)

То же, что Ollama, но с интерфейсом и совместимым с OpenAI сервером из коробки.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `API` |

`local` `llm`

---

## [Modal](https://modal.com/)

Python-функция уезжает на GPU без возни с инфраструктурой. Удобно обернуть свой шаг пайплайна.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`gpu` `serverless` `python`

---

## [Ollama](https://ollama.com/)

Локальные языковые модели одной командой. Черновики и разметка текста без отправки материала наружу.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/ollama/ollama |

`local` `llm`

---

## [OpenRouter](https://openrouter.ai/)

Один ключ ко всем языковым моделям сразу. Сравнить их на своей задаче, не заводя пять аккаунтов.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен — [получить](https://openrouter.ai/keys) |

`llm` `aggregator`

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

## [RunDiffusion](https://rundiffusion.com/)

ComfyUI и A1111 в облаке с почасовой оплатой. Локальный пайплайн без локальной видеокарты.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | — |

`cloud` `comfyui` `gpu`

---

## [RunPod](https://www.runpod.io/)

Аренда GPU по минутам. Прогнать HunyuanVideo или обучить LoRA, не покупая видеокарту.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`gpu` `cloud`

---

## [Segment Anything](https://github.com/facebookresearch/segment-anything)

Точно вырезает любой объект по клику. Основа под маски, ротоскоп и замену фона.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/facebookresearch/segment-anything |

`segmentation` `masking`

---

## [vLLM](https://github.com/vllm-project/vllm)

Быстрый сервер инференса для языковых моделей на своём железе.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `API` |
| **Исходники** | https://github.com/vllm-project/vllm |

`local` `llm` `serving`

---

