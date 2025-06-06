# Архитектура проекта

```
graph TD
    A[Пользователь] --> B[Telegram]
    B --> C[Бот]
    C --> D[FFmpeg]
    C --> E[SpeechRecognition]
    D --> F[Конвертация в WAV]
    E --> G[Google Speech API]
    G --> H[Текст]
    H --> C
    C --> B
```

### 4. `src/bot.py` (основной код бота)
```python
import os
import asyncio
import speech_recognition as sr
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from dotenv import load_dotenv

# Загрузка конфигурации
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# Инициализация бота
bot = Bot(TOKEN)
dp = Dispatcher()
recognizer = sr.Recognizer()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("🎤 Привет! Отправь мне голосовое сообщение или аудиофайл, и я преобразую его в текст!")

@dp.message(F.voice | F.audio)
async def handle_audio(message: types.Message):
    try:
        # Скачивание файла
        if message.voice:
            file_id = message.voice.file_id
            ext = ".ogg"
        else:
            file_id = message.audio.file_id
            ext = os.path.splitext(message.audio.file_name)[1]
        
        file_path = f"temp_audio{ext}"
        await bot.download(file_id, destination=file_path)
        
        # Конвертация в WAV
        wav_path = "temp_audio.wav"
        os.system(f'ffmpeg -i "{file_path}" "{wav_path}"')
        
        # Распознавание текста
        with sr.AudioFile(wav_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language='ru-RU')
        
        await message.reply(f"🔍 Текст:\n\n{text}")
    
    except Exception as e:
        await message.reply(f"❌ Ошибка: {str(e)}")
    
    finally:
        # Удаление временных файлов
        if os.path.exists(file_path): os.remove(file_path)
        if os.path.exists(wav_path): os.remove(wav_path)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())