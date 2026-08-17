<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# 🖼️ Картинки: генерация и редактирование

> Генерация с нуля, img2img, инпейнт, удаление фона, апскейл.

[← Ко всему каталогу](../README.md)

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

