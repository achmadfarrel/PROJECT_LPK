import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="GreenMart - Marketplace", layout="wide", page_icon="🛒")

# CSS styling dengan font Gen Z yang lebih ringan (Fredoka + Poppins)
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Poppins:wght@400;600&display=swap" rel="stylesheet">
<style>
body {
    background-color: #f4fdf5;
    font-family: 'Poppins', sans-serif;
}
h1, h2 {
    color: #2e7d32;
    font-family: 'Fredoka', sans-serif;
}
.card {
    background-color: white;
    padding: 1rem;
    border-radius: 1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    text-align: center;
    margin-bottom: 1rem;
    font-family: 'Poppins', sans-serif;
}
.card img {
    max-width: 100%;
    border-radius: 0.5rem;
}
.card h4 {
    margin: 0.5rem 0 0.3rem 0;
    font-family: 'Fredoka', sans-serif;
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
    font-family: 'Poppins', sans-serif;
}
.button:hover {
    background-color: #388e3c;
}
</style>
""", unsafe_allow_html=True)

# Judul halaman versi Gen Z
st.markdown("""
<h1 style="font-family: 'Fredoka', sans-serif; font-size: 3rem; color: #2e7d32; margin-bottom: 0;">
    ⚗️ chemiGO! — tools anak lab edgy 💥
</h1>
<p style="font-family: 'Poppins', sans-serif; font-size: 1.2rem; color: #444;">
    Semua alat lab, tinggal klik. No ribet, no drama 😎
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
        "name
