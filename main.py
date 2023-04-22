
import logging
import requests
import datetime
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6133648224:AAHNOBixz6FByo6DGHFtfH2_b7IJ8tEGk5w'
weather_token = "6e8d79779a0c362f14c60a1c7f363e29"
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
    buttons_row1 = ["download\U0001F4AF", "tutorial\U0001F4Ac", "dog\U0001F976"]
    buttons_row2 = ["CSGO CHEATS\U0001F631", "Weather\U0001F30D"]
    keyboard.add(*buttons_row1)
    keyboard.add(*buttons_row2)
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

@dp.message_handler(lambda message: message.text == "Weather\U0001F30D")
async def name_city(message: types.Message):
    await message.reply("Введіть назву міста: ")

    @dp.message_handler(lambda message: message.text not in ["download\U0001F4AF", "tutorial\U0001F4Ac", "dog\U0001F976", "CSGO CHEATS\U0001F631"])
    async def without_puree(message: types.Message):
        try:
            r1 = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric")
            data = r1.json()
            city = data["name"]
            temperature = round(data["main"]["temp"])
            humidity = round(data["main"]["humidity"])
            wind = round(data["wind"]["speed"])
            await message.reply(f"***{datetime.datetime.now().strftime('%b %d %Y %H:%M')}***\n"
                                f"Погода в місті: {city}\n\U0001F321Температура: {temperature} C°\n"
                                f"\U0001F4A7Вологість повітря: {humidity} %\n"
                                f"\U0001F32AВітер: {wind} м/с\n ")
        except:
            await message.reply("\U0001F3D9 Провірте назву міста \U0001F3D9")


@dp.message_handler(lambda message: message.text =='tutorial\U0001F4Ac')
async def send_tutorial(message: types.Message):
    await message.reply("Hi!\nIf you want to download the game you need to press download when its done press on it then open the file and press on main.py\nPowered by MAX.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)