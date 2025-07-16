# Divider
st.markdown("---")

# Tampilkan isi keranjang + tombol hapus & kosongkan semua
st.markdown("### 🧺 Keranjang Belanja Kamu:")
if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"- **{item['name']}** - {item['price']}")
        with col2:
            if st.button("❌ Hapus", key=f"remove_{i}"):
                st.session_state.cart.pop(i)
                st.experimental_rerun()
    
    st.markdown("### ")
    if st.button("🧹 Kosongkan Semua Keranjang"):
        st.session_state.cart.clear()
        st.experimental_rerun()
else:
    st.info("Keranjang kamu masih kosong. Yuk beli dulu! 💚")
