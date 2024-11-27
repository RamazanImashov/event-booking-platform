from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from fastapi import FastAPI
from pydantic import BaseModel

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

app = FastAPI()
active_users = {}


class LogRequest(BaseModel):
    service_name: str
    log_level: str
    log_message: str


@app.post("/send_log")
async def send_log(log_request: LogRequest):
    message = f"📌 **Service**: {log_request.service_name}\n" \
              f"⚠️ **Level**: {log_request.log_level}\n" \
              f"📝 **Log**: {log_request.log_message}"
    for user_id in active_users.keys():
        await bot.send_message(chat_id=user_id, text=message, parse_mode=ParseMode.MARKDOWN)
    return {"status": "success"}


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    active_users[message.from_user.id] = message.from_user.username
    await message.reply("Вы зарегистрированы для получения логов!")

if __name__ == "__main__":
    import uvicorn
    from threading import Thread

    def start_fastapi():
        uvicorn.run(app, reload=True, port=5000)

    Thread(target=start_fastapi, daemon=True).start()
    executor.start_polling(dp, skip_updates=True)
