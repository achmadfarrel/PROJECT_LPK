import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="GreenMart - Marketplace", layout="wide", page_icon="🛒")

# CSS styling dengan font Orbitron + Space Grotesk
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Space+Grotesk:wght@400;600&display=swap" rel="stylesheet">
<style>
body {
    background-color: #f4fdf5;
    font-family: 'Space Grotesk', sans-serif;
}
h1, h2 {
    color: #2e7d32;
    font-family: 'Orbitron', sans-serif;
}
.card {
    background-color: white;
    padding: 1rem;
    border-radius: 1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    text-align: center;
    margin-bottom: 1rem;
    font-family: 'Space Grotesk', sans-serif;
}
.card img {
    max-width: 100%;
    border-radius: 0.5rem;
}
.card h4 {
    margin: 0.5rem 0 0.3rem 0;
    font-family: 'Orbitron', sans-serif;
    font-weight: 600;
}
.button {
    background-color: #4caf50;
    color: white;
    padding: 0.4rem 1rem;
    border: none;
    border-radius: 0.5rem;
    font-size: 0.9rem;
    cursor: pointer;
    font-family: 'Space Grotesk', sans-serif;
}
.button:hover {
    background-color: #388e3c;
}
</style>
""", unsafe_allow_html=True)

# Judul halaman versi Gen Z keren maksimal
st.markdown("""
<h1 style="font-family: 'Orbitron', sans-serif; font-size: 3.5rem; color: #1b5e20; margin-bottom: 0.2rem;">
    🧪 CHEM!GO
</h1>
<p style="font-family: 'Space Grotesk', sans-serif; font-size: 1.3rem; color: #444;">
    Platform Transaksi Terbaik se-AKA Bogor 🧬⚡
</p>
""", unsafe_allow_html=True)

# Data produk
products = [
    {
        "name": "GELAS PIALA 500ML",
        "price": "Rp 85.000",
        "image": "https://images.unsplash.com/photo-1612197551535-e6d1f6e251d5?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "BEAKER GLASS 100ML",
        "price": "Rp 50.000",
        "image": "https://images.unsplash.com/photo-1598032896325-5a50efc8aeb1?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "BEAKER GLASS 250ML",
        "price": "Rp 60.000",
        "image": "https://images.unsplash.com/photo-1604668915840-e4f064790ebc?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "PIPET VOLUME 10ML",
        "price": "Rp 95.000",
        "image": "https://images.unsplash.com/photo-1589927986089-35812388d1a2?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "PIPET VOLUME 25ML",
        "price": "Rp 135.000",
        "image": "https://images.unsplash.com/photo-1589571894960-20bbe2828fa8?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "ERLENMEYER 250ML",
        "price": "Rp 80.000",
        "image": "https://images.unsplash.com/photo-1598032895446-0ff978646cb4?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "ERLENMEYER 100ML",
        "price": "Rp 80.000",
        "image": "https://images.unsplash.com/photo-1598032895446-0ff978646cb4?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "ERLENMEYER 50ML",
        "price": "Rp 70.000",
        "image": "https://images.unsplash.com/photo-1598032895446-0ff978646cb4?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "PIPET MOHR 5ML",
        "price": "Rp 70.000",
        "image": "https://images.unsplash.com/photo-1598032895446-0ff978646cb4?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "PIPET MOHR 10ML",
        "price": "Rp 75.000",
        "image": "https://images.unsplash.com/photo-1598032895446-0ff978646cb4?auto=format&fit=crop&w=500&q=60"
    }
]

# Tampilkan produk dalam 3 kolom per baris
for i in range(0, len(products), 3):
    cols = st.columns(3)
    for idx, col in enumerate(cols):
        if i + idx < len(products):
            p = products[i + idx]
            with col:
                st.markdown(f"""
                <div class="card">
                    <img src="{p['image']}" alt="{p['name']}">
                    <h4>{p['name']}</h4>
                    <p><b>{p['price']}</b></p>
                    <button class="button">🛒 Beli Yuk!</button>
                </div>
                """, unsafe_allow_html=True)

# Footer gaya Gen Z
st.markdown("---")
st.markdown(
    '<p style="text-align:center; font-family:\'Orbitron\', sans-serif; font-size:1.1rem;">© 2025 CHEM!GO 🚀 — Marketplace Lab Tools Kekinian 🔬✨</p>',
    unsafe_allow_html=True
)
