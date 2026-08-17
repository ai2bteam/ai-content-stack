<!-- GENERATED — не правь руками. Источник: data/*.yaml. Пересобрать: python3 scripts/build.py -->

# 🔊 Голос, музыка, звук

> Озвучка, клонирование голоса, фоновая музыка, SFX, транскрипция.

[← Ко всему каталогу](../README.md)

---

## [ACE-Step](https://github.com/ace-step/ACE-Step)

Открытая модель генерации музыки. Фоновые треки без роялти и без подписки.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/ace-step/ACE-Step |

`music` `open-weights`

---

## [Chatterbox TTS](https://github.com/resemble-ai/chatterbox) ⭐

MIT-лицензия и управление эмоцией. Локальная альтернатива, когда Kokoro звучит слишком ровно.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/resemble-ai/chatterbox |

`tts` `local` `mit`

---

## [ElevenLabs](https://elevenlabs.io/) ⭐

Эталон качества синтеза речи. Дорого, но по интонации пока никто не догнал.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен — [получить](https://elevenlabs.io/app/settings/api-keys) |
| **Документация** | https://elevenlabs.io/docs |

`tts` `voice-cloning`

---

## [Freesound](https://freesound.org/)

Библиотека SFX под Creative Commons. Есть API.

| | |
|---|---|
| **Тип** | API |
| **Цена** | 🟢 бесплатно |
| **Из агента** | `API` |
| **API-ключ** | нужен — [получить](https://freesound.org/apiv2/apply/) |

`sfx` `creative-commons`

---

## [Kokoro TTS](https://huggingface.co/hexgrad/Kokoro-82M) ⭐

82M параметров, Apache-2.0, крутится на CPU. Лучшее соотношение «качество / вес» для локальной озвучки.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |

`tts` `local` `apache-2`

---

## [Suno](https://suno.com/)

Генерация музыки с вокалом по текстовому описанию.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`music`

---

## [Voicebox](https://voicebox.sh/)

Локальная голосовая студия: 7 TTS-движков, 23 языка, клонирование голоса с нескольких секунд записи.

| | |
|---|---|
| **Тип** | приложение |
| **Цена** | 🔵 open source |
| **Из агента** | — |
| **Платформы** | macos, windows, linux |
| **Документация** | https://docs.voicebox.sh/ |
| **Исходники** | https://github.com/jamiepine/voicebox |
| **Разбор** | [читать](../guides/voicebox.md) |

Open-source и local-first — модели и голоса не уезжают с машины. Позиционируется как замена
связке ElevenLabs + WisprFlow: есть многодорожечный таймлайн, подрезка и сведение реплик,
то есть можно собирать диалоговые сцены, а не только рендерить отдельные фразы.

⚠️ Не путать с **Voicebox от Meta** (2023) — это исследовательская flow-matching модель,
её веса и код в открытый доступ не выкладывали. Одинаковое имя, разные вещи.

`tts` `voice-cloning` `local` `elevenlabs-alternative`

---

## [Whisper](https://github.com/openai/whisper) ⭐

Транскрипция и тайминги. Из него же получаются субтитры под автоматическую нарезку.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/openai/whisper |

`stt` `subtitles`

---

