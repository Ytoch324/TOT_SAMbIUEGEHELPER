from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# ── Вставь сюда свой токен от @BotFather
import os
BOT_TOKEN = os.getenv("8603842589:AAEC9jYDXX08CJLdDJvxO2-L70gVsTHbfFo")

# ── URL твоего задеплоенного мини-приложения (см. README)
WEBAPP_URL = "https://ytoch324.github.io/TOT_SAMbIUEGEHELPER/"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            "📚 Открыть шпаргалку ЕГЭ",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]])
    await update.message.reply_text(
        "👋 Привет!\n\n"
        "Это мини-приложение для подготовки к *заданиям 10 и 11* ЕГЭ по русскому языку.\n\n"
        "Внутри:\n"
        "📚 Теория по суффиксам (зад. 11)\n"
        "🔤 Теория по приставкам (зад. 10)\n"
        "✏️ Тест на 15 вопросов\n"
        "📋 Шпаргалка одним экраном\n\n"
        "Нажми кнопку ниже 👇",
        parse_mode="Markdown",
        reply_markup=kb
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
