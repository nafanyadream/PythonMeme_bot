import random
import logging
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

logging.basicConfig(level=logging.INFO)

TOKEN = '7915766873:AAECjWAJF9lu6pCm_aRxZBhFKgoAo2QFdHs'

MEME_DIRECTORY = os.path.join(os.path.dirname(__file__), 'memes')

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("meme"))
async def send_meme(message: types.Message):
    memes = [f for f in os.listdir(MEME_DIRECTORY) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    if not memes:
        await message.answer("В директории нет мемов!")
        return

    meme_path = os.path.join(MEME_DIRECTORY, random.choice(memes))
    await message.answer_photo(FSInputFile(meme_path), caption="Вот ваш мем!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

#Код сделан Наиль Шириев РПО
