import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="GreenMart - Marketplace", layout="wide", page_icon="🛒")

# CSS untuk styling hijau & modern
st.markdown("""
<style>
body {
    background-color: #f4fdf5;
}
h1, h2 {
    color: #2e7d32;
}
.card {
    background-color: white;
    padding: 1rem;
    border-radius: 1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    text-align: center;
    margin-bottom: 1rem;
}
.card img {
    max-width: 100%;
    border-radius: 0.5rem;
}
.card h4 {
    margin: 0.5rem 0 0.3rem 0;
}
.button {
    background-color: #4caf50;
    color: white;
    padding: 0.4rem 1rem;
    border: none;
    border-radius: 0.5rem;
    font-size: 0.9rem;
    cursor: pointer;
}
.button:hover {
    background-color: #388e3c;
}
</style>
""", unsafe_allow_html=True)

# Judul
st.title("🛍️ CHEMIGO ")
st.subheader("Lab tools, one click away 🌿")

# Data produk dummy
products = [
    {
        "name": "Tumbler Stainless",
        "price": "Rp 45.000",
        "image": "https://images.unsplash.com/photo-1612197551535-e6d1f6e251d5?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Tas Daur Ulang",
        "price": "Rp 60.000",
        "image": "https://images.unsplash.com/photo-1598032896325-5a50efc8aeb1?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Sikat Bambu",
        "price": "Rp 15.000",
        "image": "https://images.unsplash.com/photo-1604668915840-e4f064790ebc?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Sabun Organik",
        "price": "Rp 25.000",
        "image": "https://images.unsplash.com/photo-1589927986089-35812388d1a2?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Sedotan Stainless",
        "price": "Rp 10.000",
        "image": "https://images.unsplash.com/photo-1589571894960-20bbe2828fa8?auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Totebag Katun",
        "price": "Rp 30.000",
        "image": "https://images.unsplash.com/photo-1598032895446-0ff978646cb4?auto=format&fit=crop&w=500&q=60"
    },
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
                    <button class="button">Beli</button>
                </div>
                """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("© 2025 GreenMart - Marketplace Hijau untuk Masa Depan 🌱")
