import streamlit as st
import json
import os
import requests

# -------------------- KONFIGURASI --------------------
st.set_page_config(page_title="CHEMIGO - Marketplace", layout="wide", page_icon="🛒")
USER_DATA_FILE = "users.json"
BOT_TOKEN = "8101821591:AAFoQ7LCEkq7F1XGyxjAhpsUd4P6xI37WhE"
CHAT_ID = "1490556477"

# -------------------- AUTENTIKASI --------------------
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_user(username, password):
    users = load_users()
    users[username] = password
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

def login_page():
    st.markdown("## 🔐 Login CHEM!GO")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        users = load_users()
        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Login berhasil!")
            st.query_params.clear()
            if "redirect_after_login" in st.session_state:
                st.session_state.cart.append(st.session_state["redirect_after_login"])
                del st.session_state["redirect_after_login"]
            st.rerun()
        else:
            st.error("Username atau password salah!")
    st.markdown("Belum punya akun? 👉 [Register di sini](?register=1)")

def register_page():
    st.markdown("## ✍️ Register Akun Baru")
    new_user = st.text_input("Buat Username")
    new_pass = st.text_input("Buat Password", type="password")
    confirm_pass = st.text_input("Ulangi Password", type="password")
    if st.button("Daftar"):
        if new_pass != confirm_pass:
            st.warning("Password tidak cocok.")
        elif new_user in load_users():
            st.error("Username sudah terdaftar.")
        else:
            save_user(new_user, new_pass)
            st.success("Registrasi berhasil! Silakan login.")
            st.query_params.clear()
            st.rerun()

# -------------------- ARAH HALAMAN --------------------
query_params = st.query_params
if "register" in query_params:
    register_page()
    st.stop()
elif "login" in query_params:
    login_page()
    st.stop()

if st.session_state.get("logged_in"):
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

# -------------------- STYLING --------------------
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
</style>
""", unsafe_allow_html=True)

# -------------------- HALAMAN --------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# Judul dan pencarian
col_judul, col_search = st.columns([3, 1])
with col_judul:
    st.markdown("<h1 style='font-family: Orbitron;'>🧪 CHEM!GO</h1><p>Platform Terpercaya se-AKA Bogor 🧬⚡</p>", unsafe_allow_html=True)
with col_search:
    search_query = st.text_input(" ", "", placeholder="Cari produk...", label_visibility="collapsed")

products = [
    {"name": "BEAKER GLASS 500ML", "price": 85000, "image": "https://microyntech.com/wp-content/uploads/2019/06/1101-500.jpg"},
    {"name": "BEAKER GLASS 100ML", "price": 50000, "image": "https://charlestonscientific.com.sg/wp-content/uploads/2021/10/Glassware-1_beaker-100ml.jpg"},
    {"name": "BEAKER GLASS 250ML", "price": 60000, "image": "https://image.made-in-china.com/2f0j00ihQlwPCcbAfE/Laboratory-Glassware-Beaker-Borosilicate-Pyrex-Glass-Beaker-250ml-500ml-1000ml-Beaker-with-Graduations.jpg"},
    {"name": "PIPET VOLUME 10ML", "price": 95000, "image": "https://www.piwine.com/media/Products/VP10.jpg"},
    {"name": "ERLENMEYER 100ML", "price": 80000, "image": "https://tse2.mm.bing.net/th/id/OIP.T4JuL2Wy5LGHUfnN_Yt64QHaHa?pid=Api&P=0&h=220"},
]

filtered_products = [p for p in products if search_query.lower() in p["name"].lower()]
for i in range(0, len(filtered_products), 3):
    cols = st.columns(3)
    for idx, col in enumerate(cols):
        if i + idx < len(filtered_products):
            p = filtered_products[i + idx]
            with col:
                st.image(p["image"], use_container_width=True)
                st.markdown(f"**{p['name']}**\n\nRp {p['price']:,}")
                if st.button("🛒 Beli", key=f"buy_{i+idx}"):
                    if not st.session_state.get("logged_in"):
                        st.warning("Login dulu yuk!")
                        st.session_state["redirect_after_login"] = p
                        st.markdown("👉 [Klik untuk login](?login=1)")
                    else:
                        st.session_state.cart.append(p)
                        st.success("Berhasil ditambahkan ke keranjang!")

# -------------------- KERANJANG & CHECKOUT --------------------
st.markdown("---")
st.markdown("### 🧺 Keranjang Belanja")
total = 0
if st.session_state.cart:
    for idx, item in enumerate(st.session_state.cart, start=1):
        st.markdown(f"{idx}. **{item['name']}** - Rp {item['price']:,}")
        total += item["price"]
    st.markdown(f"**Total: Rp {total:,}**")

    st.markdown("### 📋 Formulir Checkout:")
    nama = st.text_input("Nama")
    kelas = st.text_input("Kelas")
    nim = st.text_input("NIM")
    prodi = st.text_input("Prodi")
    wa = st.text_input("No. WhatsApp (cth: 6281234567890)")

    if st.button("📨 Checkout via Telegram"):
        if not all([nama, kelas, nim, prodi, wa]):
            st.warning("Mohon lengkapi semua data sebelum checkout.")
        else:
            username = st.session_state.get("username", "Anon")
            pesan = f"🧾 Pesanan Baru dari {username}:%0A"
            pesan += f"👤 Nama: {nama}%0A🏫 Kelas: {kelas}%0A🆔 NIM: {nim}%0A📚 Prodi: {prodi}%0A📱 WA: https://wa.me/{wa}%0A%0A📦 Produk:%0A"
            for i, item in enumerate(st.session_state.cart, 1):
                pesan += f"{i}. {item['name']} - Rp {item['price']:,}%0A"
            pesan += f"%0A🧾 Total: Rp {total:,}"

            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={pesan}"
            response = requests.get(url)
            if response.status_code == 200:
                st.success("Pesanan berhasil dikirim!")
                st.session_state.cart.clear()
            else:
                st.error("Gagal mengirim pesanan.")

else:
    st.info("Keranjang masih kosong.")

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p>© 2025 CHEM!GO — Marketplace Lab Tools POLITEKNIK AKA BOGOR</p>
    <a href="https://wa.me/62895609627802?text=Halo%20CHEM!GO%2C%20saya%20mau%20bertanya" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="50" style="margin-top: 10px;" />
    </a>
</div>
""", unsafe_allow_html=True)
