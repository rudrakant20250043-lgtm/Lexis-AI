import streamlit as st
import requests

# Page Config sabse pehle hona chahiye
st.set_page_config(page_title="Lexis AI", layout="centered")

# ---- CUSTOM CSS FOR PREMIUM DARK THEME & LAYOUT ----
st.markdown("""
    <style>
    /* Pure UI ka background aur text color */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
    }
    
    /* Main Title (LEXIS AI) ko chamkane ke liye gradient */
    h1 {
        background: linear-gradient(to right, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 5px !important;
    }
    
    /* Subheadings styling */
    h3 {
        color: #cbd5e1 !important;
        font-weight: 400;
        margin-bottom: 25px !important;
    }
    
    /* Upload file box ko premium card look dene ke liye */
    div[data-testid="stFileUploader"] {
        background-color: rgba(30, 41, 59, 0.7);
        border: 2px dashed #4f46e5;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    /* Uploader ke andar ka text color adjust karne ke liye */
    div[data-testid="stFileUploader"] section {
        color: #e2e8f0 !important;
    }
    
    /* "Audio Enhance Karein" Button ko modern styling */
    div.stButton > button {
        background: linear-gradient(90deg, #4f46e5 0%, #06b6d4 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        padding: 12px 28px !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 14px 0 rgba(79, 70, 229, 0.4) !important;
        margin-top: 15px;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px 0 rgba(6, 182, 212, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---- APP INTERFACE ----
st.title("LEXIS AI")
st.subheader("Audio File Upload karke Voice Saaf Karein")

uploaded_file = st.file_uploader("Apni audio file (.wav) yahan upload karein:", type=["wav", "mp3"])

if st.button("🚀 Audio Enhance Karein"):
    if uploaded_file is not None:
        with st.spinner("AI aapki voice saaf kar raha hai..."):
            files = {"audio": uploaded_file.getvalue()}
            try:
                response = requests.post("http://127.0.0.1:5000/upload", files=files)
                if response.status_code == 200:
                    st.audio(response.content, format='audio/wav')
                    st.success("Audio Saaf ho gayi!")
                    st.download_button("Download Clean Audio", response.content, file_name="cleaned.wav")
                else:
                    st.error("Backend Error! app.py check karein.")
            except:
                st.error("Connection Error! Backend chalu hai?")
    else:
        st.warning("Pehle file toh dalo bhai!")
