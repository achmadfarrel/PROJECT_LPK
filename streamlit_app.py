import streamlit as st
import time
import requests

# ---------------------- Konfigurasi Telegram ----------------------
BOT_TOKEN = "6831812374:AAFqZBC2XDoV52Qt_Gcya6w_nCDkSt_xMaY"
CHAT_ID = "5360058126"

# ---------------------- Header Aplikasi ----------------------
st.set_page_config(page_title="Formulir Pemesanan", page_icon="🧪")
st.title("🧪 Formulir Pemesanan Produk CHEMIGO")
st.markdown("Silakan isi data diri dan pilih produk yang ingin Anda pesan.")

# ---------------------- Data Diri ----------------------
nama = st.text_input("👤 Nama Lengkap")
kelas = st.text_input("🏫 Kelas")
nim = st.text_input("🆔 NIM")
prodi = st.text_input("📚 Program Studi")
wa = st.text_input("📱 Nomor WhatsApp (Contoh: 6281234567890)")

# ---------------------- Daftar Produk ----------------------
st.markdown("---")
st.markdown("### 🧾 Pilih Produk:")
produk_data = [
    {"name": "BEAKER GLASS 100ML", "price": 50000, "image": "https://charlestonscientific.com.sg/wp-content/uploads/2021/10/Glassware-1_beaker-100ml.jpg"},
    {"name": "BEAKER GLASS 250ML", "price": 60000, "image": "https://image.made-in-china.com/2f0j00ihQlwPCcbAfE/Laboratory-Glassware-Beaker-Borosilicate-Pyrex-Glass-Beaker-250ml-500ml-1000ml-Beaker-with-Graduations.jpg"},
    {"name": "PIPET VOLUME 10ML", "price": 95000, "image": "https://www.piwine.com/media/Products/VP10.jpg"},
    {"name": "ERLENMEYER 100ML", "price": 80000, "image": "https://tse2.mm.bing.net/th/id/OIP.T4JuL2Wy5LGHUfnN_Yt64QHaHa?pid=Api&P=0&h=220"}
]

keranjang = {}
for produk in produk_data:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(produk["image"], width=80)
    with col2:
        qty = st.number_input(f"{produk['name']} (Rp {produk['price']:,})", min_value=0, step=1, key=produk['name'])
        if qty > 0:
            keranjang[produk['name']] = qty

# ---------------------- Metode Pembayaran ----------------------
st.markdown("---")
st.markdown("### 💳 Pilih Metode Pembayaran:")
metode_pembayaran = st.radio("", ["Transfer", "Tunai"])

bank_tujuan = None
bukti_transfer = None

if metode_pembayaran == "Transfer":
    st.markdown("#### 💳 Informasi Transfer:")
    st.markdown("""
    **GoPay:** 0895-6096-27802  
    a.n. ACHMAD FARREL INDERI  

    **BNI:** 1884905416  
    a.n. MUHAMMAD DZIKRIYANSYAH

    **BRI** 5711-0102-9217-531
    a.n. ACHMAD FARREL INDERI
    """)

    bank_tujuan = st.selectbox("🏦 Pilih Bank Tujuan Transfer", ["GoPay", "BNI", "BRI"], index=None)
    bukti_transfer = st.file_uploader("📤 Upload Bukti Pembayaran (jpg/png/pdf)", type=["jpg", "jpeg", "png", "pdf"])

# ---------------------- Tombol Kirim ----------------------
st.markdown("---")
kirim = st.button("🚀 Kirim Pesanan")

if kirim:
    if not nama or not kelas or not nim or not prodi or not wa:
        st.warning("⚠️ Mohon lengkapi semua data diri.")
    elif not keranjang:
        st.warning("⚠️ Mohon pilih setidaknya satu produk.")
    elif metode_pembayaran == "Transfer" and (not bank_tujuan or not bukti_transfer):
        st.warning("⚠️ Mohon pilih bank tujuan dan upload bukti pembayaran.")
    else:
        bank_info = f" ({bank_tujuan})" if metode_pembayaran == "Transfer" else ""
        pesan = (
            f"👤 Nama: {nama}%0A"
            f"🏫 Kelas: {kelas}%0A"
            f"🆔 NIM: {nim}%0A"
            f"📚 Prodi: {prodi}%0A"
            f"📱 WA: https://wa.me/{wa}%0A"
            f"💳 Pembayaran: {metode_pembayaran}{bank_info}%0A"
            f"%0A📦 Produk:%0A"
        )
        for produk, qty in keranjang.items():
            pesan += f"- {produk}: {qty} pcs%0A"

        # Kirim pesan teks ke Telegram
        url_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={pesan}"
        response_text = requests.get(url_text)

        # Kirim file bukti transfer ke Telegram jika ada
        if metode_pembayaran == "Transfer" and bukti_transfer is not None:
            files = {"document": (bukti_transfer.name, bukti_transfer.getvalue())}
            url_file = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
            response_file = requests.post(url_file, data={"chat_id": CHAT_ID}, files=files)
        else:
            response_file = None

        time.sleep(1.5)

        if response_text.status_code == 200 and (response_file is None or response_file.status_code == 200):
            st.success("✅ Pesanan dan bukti transfer berhasil dikirim!")
            st.session_state.cart.clear()
        else:
            st.error("❌ Gagal mengirim pesanan atau bukti transfer.")
