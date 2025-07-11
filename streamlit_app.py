import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Penjualan", layout="wide", page_icon="📊")

# Styling sederhana
st.markdown("""
    <style>
    .metric-box {
        background-color: #ffffff;
        padding: 1.2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        text-align: center;
    }
    .metric-title {
        font-size: 0.9rem;
        color: gray;
    }
    .metric-value {
        font-size: 1.5rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Judul
st.title("📊 Dashboard Penjualan")
st.write("Visualisasi data penjualan harian dengan tampilan simpel dan modern.")

# Data dummy
data = {
    "Tanggal": pd.date_range(start="2025-07-01", periods=7),
    "Penjualan": [100, 150, 200, 180, 220, 250, 300]
}
df = pd.DataFrame(data)

# Tampilkan metrik dalam tiga kolom
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""<div class='metric-box'>
        <div class='metric-title'>Total Penjualan</div>
        <div class='metric-value'>Rp {df['Penjualan'].sum():,}</div>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown(f"""<div class='metric-box'>
        <div class='metric-title'>Rata-rata Harian</div>
        <div class='metric-value'>Rp {df['Penjualan'].mean():,.2f}</div>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""<div class='metric-box'>
        <div class='metric-title'>Hari Aktif</div>
        <div class='metric-value'>{len(df)} hari</div>
    </div>""", unsafe_allow_html=True)

# Line chart bawaan Streamlit
st.subheader("📈 Tren Penjualan Harian")
df_chart = df.set_index("Tanggal")
st.line_chart(df_chart)

# Footer
st.markdown("---")
st.caption("© 2025 | Dashboard by Your Name")
