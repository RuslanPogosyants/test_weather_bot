from aiogram import types, Dispatcher, Router
from bot.weather import get_weather
from bot.database import log_request

router = Router()


@router.message(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Отправь мне название города, и я пришлю тебе информацию о погоде.")


@router.message()
async def fetch_weather(message: types.Message):
    city_name = message.text
    weather_data = await get_weather(city_name)
    log_request(message.from_user.id, city_name)

    if weather_data.get('cod') != 200:
        await message.answer("Не удалось получить данные о погоде. Проверьте название города.")
        return

    city = weather_data['name']
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']

    weather_message = (
        f"Погода в городе {city}:\n"
        f"Температура: {temp}°C\n"
        f"Влажность: {humidity}%\n"
        f"Описание: {description.capitalize()}"
    )

    await message.answer(weather_message)


def register_handlers(dp: Dispatcher):
    dp.include_router(router)
