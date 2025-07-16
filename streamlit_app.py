import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="CHEMIGO - Marketplace", layout="wide", page_icon="🛒")

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

# Judul halaman versi Gen Z keren maksimal
st.markdown("""
<h1 style="font-family: 'Orbitron', sans-serif; font-size: 3.5rem; color: #1b5e20; margin-bottom: 0.2rem;">
    🧪 CHEM!GO
</h1>
<p style="font-family: 'Space Grotesk', sans-serif; font-size: 1.3rem; color: #444;">
    Platform Terpercaya se-AKA Bogor 🧬⚡
</p>
""", unsafe_allow_html=True)

# Data produk
products = [
    {"name": "BEAKER GLASS 500ML", "price": 85000, "image": "https://microyntech.com/wp-content/uploads/2019/06/1101-500.jpg"},
    {"name": "BEAKER GLASS 100ML", "price": 50000, "image": "https://charlestonscientific.com.sg/wp-content/uploads/2021/10/Glassware-1_beaker-100ml.jpg"},
    {"name": "BEAKER GLASS 250ML", "price": 60000, "image": "https://image.made-in-china.com/2f0j00ihQlwPCcbAfE/Laboratory-Glassware-Beaker-Borosilicate-Pyrex-Glass-Beaker-250ml-500ml-1000ml-Beaker-with-Graduations.jpg"},
    {"name": "PIPET VOLUME 10ML", "price": 95000, "image": "https://www.piwine.com/media/Products/VP10.jpg"},
    {"name": "PIPET VOLUME 25ML", "price": 135000, "image": "http://www.piwine.com/media/Products/VP25.jpg"},
    {"name": "ERLENMEYER 250ML", "price": 80000, "image": "https://tse2.mm.bing.net/th/id/OIP.SreUacbKVedTlO7BFsxFpQAAAA?pid=Api&P=0&h=220"},
    {"name": "ERLENMEYER 100ML", "price": 80000, "image": "https://tse2.mm.bing.net/th/id/OIP.T4JuL2Wy5LGHUfnN_Yt64QHaHa?pid=Api&P=0&h=220"},
    {"name": "ERLENMEYER 50ML", "price": 70000, "image": "https://tse4.mm.bing.net/th/id/OIP.FFz9bCD0xOT4sZku4XRr8gHaHa?pid=Api&P=0&h=220"},
    {"name": "PIPET MOHR 5ML", "price": 70000, "image": "https://cdn11.bigcommerce.com/s-zgzol/images/stencil/1280x1280/products/9207/238283/gilson-company-5ml-mohr-type-measuring-pipette-blue__39500.1699680334.jpg?c=2"},
    {"name": "PIPET MOHR 10ML", "price": 75000, "image": "https://cdn7.bigcommerce.com/s-ufhcuzfxw9/images/stencil/1280x1280/products/11898/15926/CE-PIPEG10__90162.1503517941.jpg?c=2&imbypass=on"}
]

# Tampilkan produk dalam 3 kolom per baris
for i in range(0, len(products), 3):
    cols = st.columns(3)
    for idx, col in enumerate(cols):
        if i + idx < len(products):
            p = products[i + idx]
            with col:
                st.image(p["image"], use_container_width=True)
                st.markdown(f"<h4 style='font-family: Orbitron, sans-serif;'>{p['name']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p><b>Rp {p['price']:,}</b></p>", unsafe_allow_html=True)
                if st.button("🛒 Beli Yuk!", key=f"buy_{i+idx}"):
                    st.session_state.cart.append(p)
                    st.success(f"{p['name']} berhasil dimasukkan ke keranjang!")

# Divider
st.markdown("---")

# Tampilkan isi keranjang
st.markdown("### 🧺 Keranjang Belanja Kamu:")
total = 0
if st.session_state.cart:
    for idx, item in enumerate(st.session_state.cart, start=1):
        col1, col2 = st.columns([6, 1])
        with col1:
            st.markdown(f"{idx}. **{item['name']}** - Rp {item['price']:,}")
        with col2:
            if st.button("❌", key=f"remove_{idx}"):
                del st.session_state.cart[idx - 1]
                st.stop()
        total += item["price"]
    st.markdown(f"**🧾 Total Belanja: Rp {total:,}**")
else:
    st.info("Keranjang kamu masih kosong. Yuk beli dulu! 💚")

# Footer gaya Gen Z
st.markdown("---")
st.markdown(
    '<p style="text-align:center; font-family:\'Orbitron\', sans-serif; font-size:1.1rem;">© 2025 CHEM!GO 🚀 — Marketplace Lab Tools Kekinian 🔬✨- POLITEKNIK AKA BOGOR </p>',
    unsafe_allow_html=True
)

# WhatsApp bubble lengkap dengan teks
st.markdown("""
<div style="position: fixed; bottom: 25px; right: 25px; z-index: 100; display: flex; align-items: center;">
    <a href="https://wa.me/62895609627802?text=Halo%20CHEM!GO%2C%20saya%20mau%20bertanya%20tentang%20produk%20laboratorium." target="_blank" style="text-decoration: none; display: flex; align-items: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="55" height="55" style="border-radius:50%; margin-right: 10px;">
        <span style="background-color: #25D366; color: white; padding: 10px 15px; border-radius: 10px; font-family: 'Space Grotesk', sans-serif; font-size: 14px;">
            CHAT DISINI UNTUK PERTANYAAN
        </span>
    </a>
</div>
""", unsafe_allow_html=True)
