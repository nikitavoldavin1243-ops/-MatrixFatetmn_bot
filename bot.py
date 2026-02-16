import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Бот запущен")
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет!")
import os
import logging
from telegram.ext import Application

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Получение токена из окружения
TOKEN = os.getenv("8505345629:AAE_PrnTHpYI-yAhGuKPKFngtWhRWpt5SSA")
if not TOKEN:
    logging.error("Ошибка: TELEGRAM_BOT_TOKEN не задан!")
    raise ValueError("Установите переменную TELEGRAM_BOT_TOKEN в настройках окружения.")

logging.info("Инициализация бота...")
app = Application.builder().token(TOKEN).build()


# Инициализация бота
app = Application.builder().token("8505345629:AAE_PrnTHpYI-yAhGuKPKFngtWhRWpt5SSA").build()


def main():
    app = Application.builder().token(8505345629:AAE_PrnTHpYI-yAhGuKPKFngtWhRWpt5SSA).build()
    app.add_handler(CommandHandler("start", start_command))
    app.run_polling()  # Теперь работает корректно
