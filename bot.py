import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Получение токена из переменной окружения
TOKEN = 8505345629:AAE_PrnTHpYI-yAhGuKPKFngtWhRWpt5SSA("TELEGRAM_BOT_TOKEN")  # Имя переменной, а не токен!
if not TOKEN:
    logging.error("Ошибка: TELEGRAM_BOT_TOKEN не задан!")
    raise ValueError("Установите переменную TELEGRAM_BOT_TOKEN в настройках окружения.")

logging.info("Инициализация бота...")

# Инициализация бота
app = Application.builder().token(TOKEN).build()

# Обработчик команды /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет!")

def main():
    # Добавление обработчика
    app.add_handler(CommandHandler("start", start_command))
    
    # Запуск бота
    logging.info("Запуск polling...")
    app.run_polling()

# Запуск бота
if __name__ == "__main__":
    main()


def main():
    app = Application.builder().token(8505345629:AAE_PrnTHpYI-yAhGuKPKFngtWhRWpt5SSA).build()
    app.add_handler(CommandHandler("start", start_command))
    app.run_polling()  # Теперь работает корректно
