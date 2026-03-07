import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = "https://ytoch324.github.io/TOT_SAMbIUEGEHELPER/"  # вставь свою ссылку

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(
        "Начать подготовку",
        web_app=WebAppInfo(url=WEBAPP_URL)
    ))
    bot.send_message(
        message.chat.id,
        """Привет! Ты здесь, значит, ЕГЭ по русскому уже маячит на горизонте 😅
Не паникуй — я помогу разложить всё по полочкам.
Каждый день немного практики — и к экзамену ты будешь во всеоружии 🎯
Готов? Жми «Начать подготовку»!""",
        reply_markup=kb
    )

print("Бот запущен...")
bot.infinity_polling()
