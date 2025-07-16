import streamlit as st
import json
import os
import requests

# -------------------- KONFIGURASI --------------------
st.set_page_config(page_title="CHEMIGO - Marketplace", layout="wide", page_icon="🛒")
USER_DATA_FILE = "users.json"
TELEGRAM_BOT_TOKEN = "8101821591:AAHW-tXE4-IRf3VSm-riFlpprlKa0uZGhRA"
TELEGRAM_CHAT_ID = "8101821591"

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
            st.success("Login berhasil! Selamat datang, " + username)
            st.query_params.clear()
            if "redirect_after_login" in st.session_state:
                st.session_state.cart.append(st.session_state["redirect_after_login"])
                st.success(f"{st.session_state['redirect_after_login']['name']} berhasil dimasukkan ke keranjang!")
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

# Tombol logout jika login
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

# -------------------- ISI HALAMAN --------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# Judul + Pencarian
col_judul, col_search = st.columns([3, 1])
with col_judul:
    st.markdown("""
    <h1 style="font-family: 'Orbitron', sans-serif; font-size: 3.5rem; color: #1b5e20; margin-bottom: 0.2rem;">
        🧪 CHEM!GO
    </h1>
    <p style="font-family: 'Space Grotesk', sans-serif; font-size: 1.3rem; color: #444;">
        Platform Terpercaya se-AKA Bogor 🧪⚡
    </p>
    """, unsafe_allow_html=True)
with col_search:
    search_query = st.text_input(" ", "", placeholder="Cari produk...", label_visibility="collapsed")

products = [
    {"name": "BEAKER GLASS 500ML", "price": 85000},
    {"name": "BEAKER GLASS 100ML", "price": 50000},
    {"name": "PIPET VOLUME 10ML", "price": 95000},
    {"name": "ERLENMEYER 250ML", "price": 80000},
]

filtered_products = [p for p in products if search_query.lower() in p["name"].lower()]

for p in filtered_products:
    st.markdown(f"**{p['name']}** - Rp {p['price']:,}")
    if st.button("🛒 Beli", key=p["name"]):
        if not st.session_state.get("logged_in"):
            st.warning("Silakan login terlebih dahulu untuk membeli produk.")
            st.session_state["redirect_after_login"] = p
            st.markdown("👉 [Klik di sini untuk login](?login=1)")
        else:
            st.session_state.cart.append(p)
            st.success(f"{p['name']} dimasukkan ke keranjang!")

# -------------------- KERANJANG --------------------
st.markdown("---")
st.markdown("### 🧺 Keranjang Belanja:")
total = 0
if st.session_state.cart:
    for item in st.session_state.cart:
        st.markdown(f"- {item['name']} (Rp {item['price']:,})")
        total += item["price"]
    st.markdown(f"**Total: Rp {total:,}**")

    if st.button("📦 Checkout"):
        username = st.session_state.get("username", "anonymous")
        pesan = f"""\n🎞️ Pesanan Baru dari {username}:

✉️ Total Pesanan: Rp {total:,}
📄 Daftar Produk:"""
        for item in st.session_state.cart:
            pesan += f"\n- {item['name']} (Rp {item['price']:,})"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {"chat_id": TELEGRAM_CHAT_ID, "text": pesan}
        try:
            requests.post(url, data=data)
            st.success("Pesanan berhasil! Admin sudah menerima notifikasinya di Telegram.")
            st.session_state.cart = []
        except:
            st.error("Gagal mengirim ke Telegram.")
else:
    st.info("Keranjang masih kosong.")
