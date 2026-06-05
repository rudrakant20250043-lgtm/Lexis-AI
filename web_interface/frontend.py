import streamlit as st
import requests

st.set_page_config(page_title="Lexis AI", layout="centered")

st.title("LEXIS AI")
st.subheader("Audio File Upload karke Voice Saaf Karein")

# Sirf File Upload rakhte hain taaki error na aaye
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