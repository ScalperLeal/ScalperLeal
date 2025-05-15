import os

# Credenciais da Binance
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Configurações do mercado
SYMBOL = "BTCUSDT"
TIMEFRAME = "5m"
QTD_CANDLES = 100

# Risco por operação e stop diário
RISK_PER_TRADE_PCT = 0.5
MAX_DRAWDOWN_PCT = 5

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")