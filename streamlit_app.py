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

# Inisialisasi keranjang belanja
if "cart" not in st.session_state:
    st.session_state.cart = []

# Judul halaman
st.markdown("""
<h1 style="font-family: 'Orbitron', sans-serif; font-size: 3.5rem; color: #1b5e20; margin-bottom: 0.2rem;">
    🧪 CHEM!GO
</h1>
<p style="font-family: 'Space Grotesk', sans-serif; font-size: 1.3rem; color: #444;">
    Where science meets swag 🧬⚡
</p>
""", unsafe_allow_html=True)

# Data produk
products = [
    {"name": "BEAKER GLASS 500ML", "price": "Rp 85.000", "price_int": 85000, "image": "https://images.unsplash.com/photo-1612197551535-e6d1f6e251d5?auto=format&fit=crop&w=500&q=60"},
    {"name": "BEAKER GLASS 100ML", "price": "Rp 50.000", "price_int": 50000, "image": "https://images.unsplash.com/photo-1598032896325-5a50efc8aeb1?auto=format&fit=crop&w=500&q=60"},
    {"name": "BEAKER GLASS 250ML", "price": "Rp 60.000", "price_int": 60000, "image": "https://images.unsplash.com/photo-1604668915840-e4f064790ebc?auto=format&fit=crop&w=500&q=60"},
    {"name": "PIPET VOLUME 10ML", "price": "Rp 95.000", "price_int": 95000, "image": "https://images.unsplash.com/photo-1589927986089-35812388d1a2?auto=format&fit=crop&w=500&q=60"},
    {"name": "PIPET VOLUME 25ML", "price": "Rp 135.000", "price_int": 135000, "image": "https://images.unsplash.com/photo-1589571894960-20bbe2828fa8?auto=format&fit=crop&w=500&q=60"},
    {"name": "ERLENMEYER 250ML", "price": "Rp 80.000", "price_int": 80000, "image": "https://images.unsplash.com/photo-1598032895446-0ff978646cb4?auto=format&fit=crop&w=500&q=60"},
    {"name": "ERLENMEYER 100ML", "price": "Rp 80.000", "price_int": 80000, "image": "https://images.unsplash.com/photo-1598032895446-0ff978646cb4?auto=format&fit=crop&w=500&q=60"},
    {"name": "ERLENMEYER 50ML", "price": "Rp 70.000", "price_int": 70000, "image": "https://images.unsplash.com/photo-1598032895446-0ff978646cb4?auto=format&fit=crop&w=500&q=60"},
    {"name": "PIPET MOHR 5ML", "price": "Rp 70.000", "price_int": 70000, "image": "https://images.unsplash.com/photo-1598032895446-0ff978646cb4?auto=format&fit=crop&w=500&q=60"},
    {"name": "PIPET MOHR 10ML", "price": "Rp 75.000", "price_int": 75000, "image": "https://images.unsplash.com/photo-1598032895446-0ff978646cb4?auto=format&fit=crop&w=500&q=60"}
]

# Tampilkan produk dalam 3 kolom per baris
for i in range(0, len(products), 3):
    cols = st.columns(3)
    for idx, col in enumerate(cols):
        if i + idx < len(products):
            p = products[i + idx]
            with col:
                st.image(p["image"], use_column_width=True)
                st.markdown(f"<h4 style='font-family: Orbitron, sans-serif;'>{p['name']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p><b>{p['price']}</b></p>", unsafe_allow_html=True)
                if st.button("🛒 Beli Yuk!", key=f"buy_{i+idx}"):
                    st.session_state.cart.append(p)
                    st.success(f"{p['name']} berhasil dimasukkan ke keranjang!")

# Divider
st.markdown("---")

# Tampilkan isi keranjang
st.markdown("### 🧺 Keranjang Belanja Kamu:")
if st.session_state.cart:
    total = 0
    for i in range(len(st.session_state.cart)):
        item = st.session_state.cart[i]
        cols = st.columns([8, 1])
        with cols[0]:
            st.markdown(f"{i+1}. **{item['name']}** - {item['price']}")
        with cols[1]:
            if st.button("❌", key=f"remove_{i}"):
                st.session_state.cart.pop(i)
                st.stop()  # agar halaman tidak terus lanjut render lama
        total += item["price_int"]

    st.markdown(f"**💰 Total Belanja: Rp {total:,.0f}**".replace(",", "."))
else:
    st.info("Keranjang kamu masih kosong. Yuk beli dulu! 💚")

# Footer gaya Gen Z
st.markdown("---")
st.markdown(
    '<p style="text-align:center; font-family:\'Orbitron\', sans-serif; font-size:1.1rem;">© 2025 CHEM!GO 🚀 — Marketplace Lab Tools Kekinian 🔬✨</p>',
    unsafe_allow_html=True
)
