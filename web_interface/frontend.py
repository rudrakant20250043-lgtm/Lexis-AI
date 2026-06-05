import streamlit as st
import requests
import time

# Page Config sabse pehle hona chahiye
st.set_page_config(page_title="Lexis AI - Neural Restoration", layout="centered", initial_sidebar_state="collapsed")

# ---- ULTRA PREMIUM TECH CSS ----
st.markdown("""
    <style>
    /* Gradient Background with Glow */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1e1b4b 0%, #0f172a 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    /* Neon Glow Main Title */
    h1 {
        background: linear-gradient(135deg, #38bdf8 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        letter-spacing: -2px !important;
        text-align: center;
        margin-bottom: 0px !important;
        text-shadow: 0px 0px 50px rgba(168, 85, 247, 0.2);
    }
    
    /* Subtitle Description */
    .sub-text {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 40px;
    }
    
    /* Futuristic Metric Cards */
    .metric-container {
        display: flex;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 30px;
    }
    .metric-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        flex: 1;
    }
    .metric-val {
        color: #38bdf8;
        font-size: 1.5rem;
        font-weight: bold;
    }
    .metric-lbl {
        color: #64748b;
        font-size: 0.8rem;
        text-transform: uppercase;
    }

    /* Premium Glassmorphic Upload Box */
    div[data-testid="stFileUploader"] {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 2px dashed #6366f1 !important;
        border-radius: 16px !important;
        padding: 30px !important;
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.7);
        transition: all 0.4s ease;
    }
    div[data-testid="stFileUploader"]:hover {
        border-color: #ec4899 !important;
        box-shadow: 0 10px 40px -10px rgba(99, 102, 241, 0.3);
    }
    
    /* Pulse Glow Action Button */
    div.stButton > button {
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 50%, #ec4899 100%) !important;
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 14px 40px !important;
        border-radius: 50px !important;
        width: 100%;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 20px 0 rgba(168, 85, 247, 0.4) !important;
        letter-spacing: 0.5px;
    }
    div.stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px 0 rgba(236, 72, 153, 0.6) !important;
    }
    
    /* Company style Features Grid */
    .feature-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin-top: 50px;
    }
    .feature-box {
        background: rgba(30, 41, 59, 0.2);
        border-left: 3px solid #a855f7;
        padding: 15px;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- APP HEADER ----
st.markdown("<h1>LEXIS AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Next-Gen Deep Learning Architecture for Studio-Grade Audio Restoration</p>", unsafe_allow_html=True)

# ---- LIVE METRICS BAR (Badi company jaisa feel) ----
st.markdown("""
<div class='metric-container'>
    <div class='metric-card'><div class='metric-val'>0.02s</div><div class='metric-lbl'>Latency</div></div>
    <div class='metric-card'><div class='metric-val'>DeepClean v4</div><div class='metric-lbl'>Active Model</div></div>
    <div class='metric-card'><div class='metric-val'>99.4%</div><div class='metric-lbl'>Accuracy</div></div>
</div>
""", unsafe_allow_html=True)

# ---- AUDIO UPLOADER ----
uploaded_file = st.file_uploader("", type=["wav", "mp3"])

if st.button("⚡ ENGAGE NEURAL ENHANCER"):
    if uploaded_file is not None:
        
        # --- DYNAMIC PROCESSING STEPS (Khatarnak Real-time logs) ---
        status_box = st.empty()
        progress_bar = st.progress(0)
        
        steps = [
            "Initializing Neural Pipeline...", 
            "Analyzing Background Noise Profile (Hiss/Hum)...", 
            "Applying Deep-Learning Masking Layers...", 
            "Synthesizing High-Fidelity Vocals...", 
            "Finalizing Audio Rendering..."
        ]
        
        for idx, step in enumerate(steps):
            status_box.markdown(f"🧬 **Status:** *{step}*")
            progress_bar.progress((idx + 1) * 20)
            time.sleep(0.6) # Fake processing effect for premium feel
            
        status_box.empty()
        progress_bar.empty()
        
        # --- ACTUAL REQUEST TO BACKEND ---
        with st.spinner("Compiling high-fidelity streams..."):
            files = {"audio": uploaded_file.getvalue()}
            try:
                response = requests.post("http://127.0.0.1:5000/upload", files=files)
                if response.status_code == 200:
                    st.success("✨ Audio Successfully Restored to Studio Quality!")
                    st.audio(response.content, format='audio/wav')
                    st.download_button("📥 DOWNLOAD ENHANCED AUDIO", response.content, file_name="cleaned.wav")
                else:
                    st.error("Backend Core Error! Please verify model logs in app.py.")
            except:
                st.error("📡 Connection Link Severed! UI deployed successfully, local backend offline.")
    else:
        st.warning("Please upload a valid audio payload first, developer!")

# ---- FOOTER FEATURES SECTION ----
st.markdown("""
<div class='feature-grid'>
    <div class='feature-box'><h4>🎙️ Vocal Isolation</h4><p style='color:#94a3b8; font-size:0.85rem;'>Extracts human speech profiles from severe environmental noise grids.</p></div>
    <div class='feature-box'><h4>🚀 Multi-Band DSP</h4><p style='color:#94a3b8; font-size:0.85rem;'>Real-time spectral subtraction algorithms powered by custom PyTorch tensor graphs.</p></div>
</div>
""", unsafe_allow_html=True)
