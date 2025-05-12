from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
import speech_recognition as sr
import subprocess
import asyncio
import os


TOKEN = '8073594612:AAGAn14M4DHyGSSN8DdNKoKf9T8vbN56mbI'
bot = Bot(TOKEN)
dp = Dispatcher()
r = sr.Recognizer()


@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer('Привет! Отправь мне аудиофайл и я конвертирую его в текст!')


@dp.message(F.audio)
async def converting_audio_to_text(message: types.Message):
    split_tup = os.path.splitext(message.audio.file_name)
    file_name = f'{split_tup[0]}_{message.from_user.full_name}{split_tup[1]}'
    await bot.download(message.audio.file_id, file_name)

    file_name_wav = f'{split_tup[0]}_{message.from_user.full_name}.wav'
    subprocess.call(['ffmpeg', '-i', file_name, file_name_wav])

    with sr.AudioFile(file_name_wav) as source:
        audio = r.record(source)
    text = r.recognize_google(audio, language='ru')
    await message.answer(text)

    os.remove(file_name)
    os.remove(file_name_wav)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


