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

def main():
    app = Application.builder().token(8505345629:AAE_PrnTHpYI-yAhGuKPKFngtWhRWpt5SSA).build()
    app.add_handler(CommandHandler("start", start_command))
    app.run_polling()  # Теперь работает корректно
