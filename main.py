
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6133648224:AAHNOBixz6FByo6DGHFtfH2_b7IJ8tEGk5w'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm YOURMOM.COM\U0001F975\nPowered by MAX.")
    #buttons
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_row1 = ["download\U0001F4AF", "tutorial\U0001F4Ac", "dog\U0001F976", "CSGO CHEATS\U0001F631"]
    keyboard.add(*buttons_row1)
    await message.answer("Обери одну з функцій внизу: ", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text =='download\U0001F4AF')
async def send_file(message: types.Document):
  await message.reply_document(open('shooter (1).zip', 'rb'))

@dp.message_handler(lambda message: message.text =='dog\U0001F976')
async def send_file(message: types.Document):
    await message.reply_document(open('dog.jpg', 'rb'))

@dp.message_handler(lambda message: message.text =='CSGO CHEATS\U0001F631')
async def send_Cheats (message: types.Message):
    await message.reply("https://interium.ooo/")



@dp.message_handler(lambda message: message.text =='tutorial\U0001F4Ac')
async def send_tutorial(message: types.Message):
    await message.reply("Hi!\nIf you want to download the game you need to press download when its done press on it then open the file and press on main.py\nPowered by MAX.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)