# app.py
import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("📈 Scalper Leal - Painel Online")

col1, col2 = st.columns(2)
col1.metric("Saldo Atual", "USDT 10,000")
col2.metric("ROI Hoje", "+1.2%")

st.subheader("📊 Gráfico ao Vivo")
chart = st.line_chart([])

st.subheader("🧾 Histórico de Operações")
df = pd.DataFrame({
    'Data': ['10:00', '10:05'],
    'Ativo': ['BTCUSDT', 'BTCUSDT'],
    'Sinal': ['BUY', 'SELL'],
    'Preço': [62500, 62600],
    'Resultado': ['$+100', '$+98']
})
st.table(df)

st.subheader("📄 Logs em Tempo Real")
logs = st.empty()

for i in range(100):
    new_data = pd.DataFrame([np.random.rand()])
    chart.add_rows(new_data)
    logs.text(f"[INFO] Ciclo {i+1} concluído.")
    time.sleep(5)