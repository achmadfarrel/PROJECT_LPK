import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Penjualan", layout="wide", page_icon="📊")

# Judul
st.title("📊 Dashboard Penjualan")
st.write("Visualisasi data penjualan harian dengan tampilan yang modern.")

# Data contoh
data = {
    "Tanggal": pd.date_range(start="2025-07-01", periods=7),
    "Penjualan": [100, 150, 200, 180, 220, 250, 300]
}
df = pd.DataFrame(data)

# Tiga kolom metrik
col1, col2, col3 = st.columns(3)
col1.metric("Total Penjualan", f"Rp {df['Penjualan'].sum():,}")
col2.metric("Rata-rata", f"Rp {df['Penjualan'].mean():,.2f}")
col3.metric("Hari Aktif", f"{len(df)} hari")

# Grafik
fig = px.line(df, x='Tanggal', y='Penjualan', title='Tren Penjualan Harian', markers=True)
st.plotly_chart(fig, use_container_width=True)
