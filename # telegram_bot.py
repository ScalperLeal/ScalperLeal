telegram_bot.py
import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("🟢 Bot Scalper Leal está ativo!")

def setup_telegram_bot():
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TELEGRAM_BOT_TOKEN:
        print("❌ Token do Telegram não configurado.")
        return

    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    print("🤖 Bot do Telegram iniciado e aguardando comandos...")
    updater.idle()
