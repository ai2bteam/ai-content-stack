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

## [Adobe Podcast Enhance](https://podcast.adobe.com/)

Превращает запись из комнаты с эхом в студийную. Иногда переусердствует — слушай результат.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`cleanup` `denoise`

---

## [AudioCraft / MusicGen](https://github.com/facebookresearch/audiocraft)

Открытая генерация музыки и звуков от Meta. Локально, без лимитов и вопросов о правах на результат.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/facebookresearch/audiocraft |

`music` `sfx` `open-weights` `local`

---

## [Auphonic](https://auphonic.com/)

Автоматическое выравнивание громкости, шумодав и приведение к вещательным нормам. Есть API.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`mastering` `loudness`

---

## [Bark](https://github.com/suno-ai/bark)

Генерирует не только речь, но и смех, вздохи, музыкальный фон. Непредсказуем — зато живой.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/suno-ai/bark |

`tts` `expressive` `local`

---

## [Cartesia](https://cartesia.ai/)

Ставка на низкую задержку синтеза. Берут, когда озвучка нужна в реальном времени, а не файлом.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`tts` `low-latency`

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

## [Coqui TTS](https://github.com/coqui-ai/TTS)

Библиотека с десятками моделей и рецептами обучения. Компания закрылась, код остался и работает.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/coqui-ai/TTS |

`tts` `local` `toolkit`

---

## [Demucs](https://github.com/adefossez/demucs)

Разбирает трек на голос, барабаны, бас и остальное. Вытащить чистую речь из записи с музыкой.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/adefossez/demucs |

`stem-separation` `cleanup`

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

## [F5-TTS](https://github.com/SWivid/F5-TTS)

Клонирование голоса по короткому сэмплу с внятной интонацией. Держится в топе открытых моделей.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/SWivid/F5-TTS |

`tts` `voice-cloning` `local`

---

## [faster-whisper](https://github.com/SYSTRAN/faster-whisper)

Тот же Whisper, но в разы быстрее и экономнее по памяти. На длинных роликах разница в десятки минут.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/SYSTRAN/faster-whisper |

`stt` `fast` `local`

---

## [Fish Speech](https://github.com/fishaudio/fish-speech)

Открытый многоязычный TTS с клонированием. Один из лучших вариантов для русского среди локальных.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/fishaudio/fish-speech |

`tts` `voice-cloning` `local` `multilingual`

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

## [OpenVoice](https://github.com/myshell-ai/OpenVoice)

Переносит тембр и эмоцию на другой язык. Один диктор — и русская, и английская версия ролика.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/myshell-ai/OpenVoice |

`voice-cloning` `cross-lingual`

---

## [Piper](https://github.com/OHF-Voice/piper1-gpl)

Очень быстрый TTS, работает даже на Raspberry Pi. Голос простоватый, зато синтез почти мгновенный.

| | |
|---|---|
| **Тип** | модель |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/OHF-Voice/piper1-gpl |

`tts` `local` `fast`

---

## [PlayAI](https://www.playht.com/)

Большая библиотека готовых голосов и клонирование. Основной конкурент ElevenLabs по цене.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`tts` `voice-cloning`

---

## [Resemble AI](https://www.resemble.ai/)

Клонирование голоса с упором на юридическую чистоту и водяные знаки в синтезе.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🔴 платно |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`voice-cloning` `watermarking`

---

## [Stable Audio](https://stableaudio.com/)

Инструментальные треки и звуковые текстуры под заданный хронометраж — важно, когда музыка ложится в тайминг сцены.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | `API` |
| **API-ключ** | нужен |

`music` `sfx`

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

## [Udio](https://www.udio.com/)

Генерация музыки с вокалом. Главный конкурент Suno, местами чище сводит.

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

## [whisper.cpp](https://github.com/ggml-org/whisper.cpp)

Whisper на C++ без Python и CUDA. На Apple Silicon летает через Metal.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/ggml-org/whisper.cpp |

`stt` `local` `apple-silicon`

---

## [WhisperX](https://github.com/m-bain/whisperX)

Whisper с пословными таймингами и разделением говорящих. То, из чего собираются караоке-субтитры.

| | |
|---|---|
| **Тип** | библиотека |
| **Цена** | 🔵 open source |
| **Из агента** | `CLI` |
| **Исходники** | https://github.com/m-bain/whisperX |

`stt` `subtitles` `word-timestamps`

---

## [Zapsplat](https://www.zapsplat.com/)

Большая библиотека SFX с бесплатным тарифом при указании авторства.

| | |
|---|---|
| **Тип** | сервис |
| **Цена** | 🟡 freemium |
| **Из агента** | — |

`sfx`

---

