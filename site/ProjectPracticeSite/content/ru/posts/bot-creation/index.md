---
title: 'Документация создания бота в Телеграмм'
slug: 'bot-creation'
tags: ['Бот', 'Документация']
summary: 'В рамках проектной практики мы модифицировали телеграмм-бота. Теперь он может конвентировать аудио-файлы в речь!' # This is what will be displayed as summary for the post (the theme will automatically generate one from the content you write in the post if left empty)
description: # This is what will be displayed as meta data (the theme will automatically grab it from summary if left empty)
date: '2025-05-02T12:10:50+02:00'
expiryDate: '' # You want your post to vanish after a certain date? Write it down here! Must be in the same format of `date`
translationKey: flower-poem # If you have a translated post for this one, set the same translationKey to have the translation displayed
draft: false # Set wether this post is a draft
layout: 'single'
Params:
   imageAttribution: '' # Set an attribution to the author of the picture you're using for the post
# Refer to [Front matter | Hugo](https://gohugo.io/content-management/front-matter/)
---

# Telegram Audio-to-Text Bot

Бот для конвертации голосовых сообщений и аудиофайлов в текст.

##  Возможности
- Конвертация аудио в текст (поддержка русского и английского)
- Обработка голосовых сообщений
- Простое управление

##  Быстрый старт

### 1. Установите зависимости:
```bash
pip install -r requirements.txt
```
#### структура
```
audio-bot/
├── src/
│   └── BlackRedBot.py      # Основной код бота
├── docs/
│   ├── BotDocumentation.md # Отчёт о работе
│   └── ARCHITECTURE.md     # Описание архитектуры
├── assets/                 # Изображения
└── requirements.txt        # Зависимости
```

### 2. `docs/REPORT.md` (отчёт о проекте)

#### Цели проекта
1. Создать Telegram-бота для конвертации аудио в текст
2. Обеспечить поддержку популярных аудиоформатов
3. Достичь точности распознавания не менее 80%

####  Результаты тестирования
| Параметр         | Значение |
|------------------|----------|
| Точность (русский) | 85%      |
| Время обработки  | 3-7 сек  |
| Поддержка форматов | MP3, WAV, OGG |

####  Проблемы и решения
1. Проблема: Долгая обработка больших файлов  
   Решение: Добавил ограничение на 30 секунд аудио

2. Проблема: Ошибки кодировки  
   Решение: Принудительная конвертация в WAV
