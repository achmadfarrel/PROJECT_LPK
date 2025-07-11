import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------
# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;500;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
        background-color: #f8f9fa;
    }
    .card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
    .icon {
        font-size: 1.5rem;
        margin-right: 0.5rem;
        color: #4a4a4a;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# Header
st.title("📊 Dashboard Penjualan")
st.markdown("Visualisasi data penjualan harian dengan tampilan yang modern dan ringan.")

# ---------------------
# Sample Data
data = {
    "Tanggal": pd.date_range(start="2025-07-01", periods=7),
    "Penjualan": [100, 150, 200, 180, 220, 250, 300]
}
df = pd.DataFrame(data)

# ---------------------
# Metrics Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="card"><i class="icon">💰</i><b>Total:</b><br>Rp {:,}</div>'.format(df['Penjualan'].sum()), unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><i class="icon">📈</i><b>Rata-rata:</b><br>Rp {:,.2f}</div>'.format(df['Penjualan'].mean()), unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card"><i class="icon">📅</i><b>Hari Aktif:</b><br>{}</div>'.format(len(df)), unsafe_allow_html=True)

# ---------------------
# Chart
fig = px.line(df, x='Tanggal', y='Penjualan', title='Tren Penjualan Harian', markers=True)
fig.update_layout(
    plot_bgcolor='white',
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor="#eee")
)
st.plotly_chart(fig, use_container_width=True)

# ---------------------
# Footer
st.markdown("---")
st.markdown("© 2025 | Dashboard by [Your Name]")
