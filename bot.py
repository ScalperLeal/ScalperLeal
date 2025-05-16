# bot.py
import os
import time
from binance.client import Client
from config import API_KEY, API_SECRET, SYMBOL
from telegram_notifier import send_telegram_message
from telegram.ext import Updater, CommandHandler

# Conectar com Binance
client = Client(API_KEY, API_SECRET)

def calculate_position_size():
    balance = float(client.get_account()['balances'][0]['free'])
    risk_amount = balance * 0.005  # 0.5%
    lot_size = risk_amount / 10
    return round(lot_size, 3)

def fetch_data():
    klines = client.get_klines(symbol=SYMBOL, interval="5m", limit=100)
    df = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_volume', 'taker_buy_quote_volume', 'ignore'
    ])
    df['close'] = df['close'].astype(float)
    df['ma_9'] = df['close'].rolling(9).mean()
    df['ma_21'] = df['close'].rolling(21).mean()
    return df.iloc[-1]

# Estratégia e sinais
print("🚀 Bot iniciado com sucesso!")
send_telegram_message("🟢 Bot Scalper Leal iniciado!")

# Loop principal
while True:
    try:
        data = fetch_data()
        if data['ma_9'] > data['ma_21']:
            signal = "BUY"
        elif data['ma_9'] < data['ma_21']:
            signal = "SELL"
        else:
            signal = None

        if signal:
            qty = calculate_position_size()
            message = f"🚨 SINAL DETECTADO\nAtivo: {SYMBOL}\nAção: *{signal}*\nPreço: {data['close']:.2f}"
            send_telegram_message(message)
        time.sleep(60)
    except Exception as e:
        send_telegram_message(f"❌ Erro no ciclo: {e}")
        time.sleep(10)

# === BOT DO TELEGRAM RESPONDENDO AO /start ===
if __name__ == '__main__':
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if TELEGRAM_BOT_TOKEN:
        def start_command(update, context):
            update.message.reply_text("🟢 Bot Scalper Leal está ativo!")

        updater = Updater(TELEGRAM_BOT_TOKEN)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start_command))
        updater.start_polling()
        print("🤖 Bot do Telegram iniciado e aguardando comandos...")
        updater.idle()
    else:
        print("❌ Token do Telegram não configurado. Comandos desativados.")
