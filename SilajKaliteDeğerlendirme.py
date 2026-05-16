import streamlit as st

st.set_page_config(page_title="Silaj Kalite Analizi", layout="centered")
# --- ARKA PLAN RENK AYARI (Bu bloğu st.set_page_config'in altına ekle) ---
st.markdown(
    """
    <style>
    /* Tüm uygulamanin arka plan rengini değiştirir */
    .stApp {
        background-color: #3cb371; /* Buraya istediğin renk kodunu yazabilirsin */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("🌾 Silaj Kalite Değerlendirme Programı")
st.markdown(f"""
    <style>
     /* Başlik kutusunun stili */
    .analiz-baslik {{
        background-color: #1e4d2b; /* Koyu Yeşil Arka Plan */
        color: #ffffff; /* Beyaz Yazi */
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-family: 'Arial';
        font-weight: bold;
        font-size: 24px;
        margin-bottom: 25px;
        border: 2px solid #edffed;
        
    }}
    </style>
    <div class="analiz-baslik">📊 SİLAJ ANALİZ DEĞERLERİ GİRİŞİ</div>
    """, unsafe_allow_html=True)
st.header("Analiz Değerleri")

col1, col2 = st.columns(2)

with col1:
    kuru_madde = st.number_input("% Kuru Madde", value=0.0, step=0.0)
    ph_degeri = st.number_input("p.H Değeri", value=0.0, step=0.00)
    asetik_asit = st.number_input("Toplam Asetik Asit (%)", value=0.0, step=0.00)

with col2:
    butirik_asit = st.number_input("Toplam Bütirik Asit (%)", value=0.00, step=0.00)
    renk = st.number_input("Renk Puanı (0-4)", value=0, min_value=0, max_value=4, step=0)
    koku_tat = st.number_input("Koku-Tat Puanı (0-7)", value=0, min_value=0, max_value=7, step=0)
    struktur = st.number_input("Strüktür Puanı (0-4)", value=0, min_value=0, max_value=4, step=0)

# --- HESAPLAMALAR ---
if ph_degeri < 3.0: ph_puani = 0
elif 3.0 <= ph_degeri < 3.3: ph_puani = 1
elif 3.3 <= ph_degeri < 3.5: ph_puani = 2
elif 3.5 <= ph_degeri <= 4.0: ph_puani = 4
elif 4.0 < ph_degeri <= 4.25: ph_puani = 3
elif 4.25 < ph_degeri <= 4.5: ph_puani = 2
elif 4.5 < ph_degeri <= 5.0: ph_puani = 1
else: ph_puani = 0

if asetik_asit < 0.4: asetik_puani = 4
elif 0.4 <= asetik_asit < 0.6: asetik_puani = 3
elif 0.6 <= asetik_asit < 0.8: asetik_puani = 2
elif 0.8 <= asetik_asit <= 1.0: asetik_puani = 1
else: asetik_puani = 0

if butirik_asit < 0.05: butirik_puani = 12
elif 0.05 <= butirik_asit < 0.15: butirik_puani = 10
elif 0.15 <= butirik_asit < 0.25: butirik_puani = 8
elif 0.25 <= butirik_asit < 0.35: butirik_puani = 4
elif 0.35 <= butirik_asit <= 0.50: butirik_puani = 2
else: butirik_puani = 0

konigsberg_toplam = ph_puani + asetik_puani + butirik_puani + renk + koku_tat + struktur
fleig_skoru = 220 + (2 * kuru_madde - 15) - (40 * ph_degeri)

if konigsberg_toplam >= 32: kalite = "Çok İyi"
elif 28 <= konigsberg_toplam <= 31: kalite = "İyi"
elif 24 <= konigsberg_toplam <= 27: kalite = "Orta"
elif 18 <= konigsberg_toplam <= 23: kalite = "Düşük"
else: kalite = "Çok Kötü"

if fleig_skoru > 85: fleig_kalite = "Çok İyi Kalite"
elif fleig_skoru > 60: fleig_kalite = "İyi Kalite"
elif fleig_skoru > 40: fleig_kalite = "Orta Kalite"
elif fleig_skoru > 20: fleig_kalite = "Düşük Kalite"
else: fleig_kalite = "Çok Kötü Kalite"

st.divider()

# --- GÖRSEL SONUÇ PANELİ ---
sol_sonuc, sag_sonuc = st.columns(2)

with sol_sonuc:
    st.markdown(f"""
        <div style='background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 10px solid #1f77b4; text-align: center; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);'>
            <p style='font-size: 24px; font-weight: bold; color: #333; margin-bottom: 5px;'>Königsberg Puanı</p>
            <p style='font-size: 44px; font-weight: 900; color: #1f77b4; margin: 0;'>{konigsberg_toplam}</p>
            <h2 style='color: #444; margin-top: 10px;'>Kalite: {kalite}</h2>
        </div>
    """, unsafe_allow_html=True)

with sag_sonuc:
    st.markdown(f"""
        <div style='background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 10px solid #2ca02c; text-align: center; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);'>
            <p style='font-size: 24px; font-weight: bold; color: #333; margin-bottom: 5px;'>Fleig Skoru</p>
            <p style='font-size: 44px; font-weight: 900; color: #2ca02c; margin: 0;'>{fleig_skoru:.1f}</p>
            <h2 style='color: #444; margin-top: 10px;'>{fleig_kalite}</h2>
        </div>
    """, unsafe_allow_html=True)

st.divider()
st.info(f"Puanlar: pH({ph_puani}), Asetik({asetik_puani}), Bütirik({butirik_puani})")