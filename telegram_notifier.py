# telegram_notifier.py
import requests
import os

def send_telegram_message(message):
    TELEGRAM_BOT_TOKEN = os.getenv("7228891982:AAE8i0SwYeEVJFo8o02avyeTgtn4nHeoTQI")
    TELEGRAM_CHAT_ID = os.getenv("858755726")

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Token ou Chat ID do Telegram não configurados.")
        return

    url = f"https://api.telegram.org/bot {TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Mensagem enviada no Telegram!")
        else:
            print(f"❌ Falha ao enviar mensagem. Código HTTP: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem no Telegram: {e}")
