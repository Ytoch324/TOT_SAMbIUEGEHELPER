import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = "https://ytoch324.github.io/TOT_SAMbIUEGEHELPER/"  # вставь свою ссылку

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        "📖 Открыть материалы",
        web_app=WebAppInfo(url=WEBAPP_URL)
    ))
    bot.send_message(
        message.chat.id,
        "Привет! Здесь теория и тесты для подготовки к заданиям 10 и 11 ЕГЭ по русскому языку.",
        reply_markup=kb
    )


print("Бот запущен...")
bot.infinity_polling()
