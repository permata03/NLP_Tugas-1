import streamlit as st
import pickle
import re

st.set_page_config(
    page_title="Analisis Sentimen Produk",
    page_icon="🛒",
    layout="centered"
)

model = pickle.load(open("sentiment_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

st.markdown("""
<style>
.stButton > button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    height: 3em;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🛒 Analisis Sentimen Review Produk</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Masukkan ulasan produk untuk mengetahui sentimennya</p>", unsafe_allow_html=True)

st.divider()

text = st.text_area(
    "✍️ Masukkan Review",
    placeholder="contoh: barang bagus dan pengiriman cepat",
    height=120
)

if st.button("🔍 Prediksi Sentimen", use_container_width=True):
    if text.strip() == "":
        st.warning("⚠️ Review tidak boleh kosong")
    else:
        clean = clean_text(text)
        vec = tfidf.transform([clean])
        pred = model.predict(vec)[0]

        st.divider()

        if pred == 1:
            st.success("Sentimen: **POSITIF**")
        else:
            st.error("Sentimen: **NEGATIF**")

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color: #6c757d; font-size: 14px;">
        <b>Anggi Permata Sari</b><br>
        Neural Language Processing 
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()
st.caption("Model NLP – Naive Bayes | Dataset Review Produk Indonesia")