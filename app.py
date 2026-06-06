import streamlit as st
import requests
import time

# Page Config sabse pehle hona chahiye
st.set_page_config(page_title="Lexis AI - Neural Restoration", layout="centered", initial_sidebar_state="collapsed")

# ---- ULTRA ANIMATED CYBERPUNK CSS ----
st.markdown("""
    <style>
    /* Animated Cyber Grid and Wave Background */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0c0a24 0%, #020208 100%);
        background-image: 
            linear-gradient(rgba(18, 16, 54, 0.3) 1px, transparent 1px),
            linear-gradient(90deg, rgba(18, 16, 54, 0.3) 1px, transparent 1px);
        background-size: 40px 40px;
        color: #00ffcc;
        font-family: 'Courier New', Courier, monospace;
        overflow-x: hidden;
    }
    
    /* Background moving glow animation effect */
    .stApp::before {
        content: "";
        position: absolute;
        top: -50%; left: -50%; right: -50%; bottom: -50%;
        background: radial-gradient(circle at 30% 20%, rgba(168, 85, 247, 0.15) 0%, transparent 40%),
                    radial-gradient(circle at 70% 80%, rgba(6, 182, 212, 0.15) 0%, transparent 40%);
        animation: rotateGlow 20s linear infinite;
        z-index: 0;
        pointer-events: none;
    }

    @keyframes rotateGlow {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Neon Glitch Text Title */
    h1 {
        background: linear-gradient(90deg, #00ffcc, #ff007f, #00ffcc);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem !important;
        font-weight: 900 !important;
        text-align: center;
        letter-spacing: 4px !important;
        animation: shine 4s linear infinite, glitch 1s linear infinite alternate;
        text-shadow: 0 0 20px rgba(0, 255, 204, 0.3);
        z-index: 1;
    }
    
    @keyframes shine {
        to { background-position: 200% center; }
    }

    /* Subtitle Description */
    .sub-text {
        text-align: center;
        color: #8fa0dd;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 40px;
    }
    
    /* Animated Metrics Grid */
    .metric-container {
        display: flex;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 30px;
    }
    .metric-card {
        background: rgba(5, 5, 20, 0.75);
        border: 1px solid #00ffcc;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.1);
        padding: 15px;
        border-radius: 5px;
        text-align: center;
        flex: 1;
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        box-shadow: 0 0 25px rgba(255, 0, 127, 0.4);
        border-color: #ff007f;
        transform: scale(1.05);
    }
    .metric-val {
        color: #ff007f;
        font-size: 1.6rem;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(255, 0, 127, 0.3);
    }
    .metric-lbl {
        color: #00ffcc;
        font-size: 0.75rem;
        letter-spacing: 1px;
    }

    /* Cyber Translucent Upload Box */
    div[data-testid="stFileUploader"] {
        background: rgba(5, 5, 15, 0.8) !important;
        border: 2px solid #00ffcc !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.2) !important;
        border-radius: 4px !important;
        padding: 30px !important;
        transition: all 0.5s ease;
    }
    div[data-testid="stFileUploader"]:hover {
        border-color: #ff007f !important;
        box-shadow: 0 0 40px rgba(255, 0, 127, 0.4) !important;
    }
    
    /* Hyper Pulse Processing Button */
    div.stButton > button {
        background: transparent !important;
        color: #00ffcc !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border: 2px solid #00ffcc !important;
        padding: 15px 40px !important;
        border-radius: 4px !important;
        width: 100%;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        letter-spacing: 2px;
        text-transform: uppercase;
        animation: pulseBorder 2s infinite;
    }
    
    @keyframes pulseBorder {
        0% { box-shadow: 0 0 10px rgba(0,255,204,0.3); }
        50% { box-shadow: 0 0 25px rgba(0,255,204,0.6); }
        100% { box-shadow: 0 0 10px rgba(0,255,204,0.3); }
    }

    div.stButton > button:hover {
        color: #ffffff !important;
        background: #ff007f !important;
        border-color: #ff007f !important;
        box-shadow: 0 0 35px #ff007f !important;
        transform: translateY(-2px);
    }
    
    /* Company style Features Grid */
    .feature-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin-top: 50px;
    }
    .feature-box {
        background: rgba(5, 5, 15, 0.6);
        border: 1px solid rgba(0, 255, 204, 0.2);
        padding: 15px;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- APP HEADER ----
st.markdown("<h1>LEXIS AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>// NEURAL SPECTRUM INTERPOLATION CORE ACTIVE</p>", unsafe_allow_html=True)

# ---- LIVE METRICS BAR (Hover Effects Ke Saath) ----
st.markdown("""
<div class='metric-container'>
    <div class='metric-card'><div class='metric-val'>0.02s</div><div class='metric-lbl'>SPECTRUM LATENCY</div></div>
    <div class='metric-card'><div class='metric-val'>MATRIX_v4</div><div class='metric-lbl'>CORE MODEL</div></div>
    <div class='metric-card'><div class='metric-val'>99.4%</div><div class='metric-lbl'>RESTORATION RATE</div></div>
</div>
""", unsafe_allow_html=True)

# ---- AUDIO UPLOADER ----
uploaded_file = st.file_uploader("", type=["wav", "mp3"])

if st.button("⚡ INITIALIZE NEURAL EXTRACTION"):
    if uploaded_file is not None:
        
        # --- DYNAMIC PROCESSING STEPS ---
        status_box = st.empty()
        progress_bar = st.progress(0)
        
        steps = [
            ">> Injecting core neural vectors...", 
            ">> Isolate environmental noise phase grids...", 
            ">> Running high-order tensor convolution...", 
            ">> Re-synthesizing uncompressed vocal matrix...", 
            ">> Exporting master output pipeline..."
        ]
        
        for idx, step in enumerate(steps):
            status_box.markdown(f"📡 `{step}`")
            progress_bar.progress((idx + 1) * 20)
            time.sleep(0.7) # Animated step feedback
            
        status_box.empty()
        progress_bar.empty()
        
        # --- ACTUAL REQUEST TO BACKEND ---
        with st.spinner("Locking signal arrays..."):
            files = {"audio": uploaded_file.getvalue()}
            try:
                response = requests.post("http://127.0.0.1:5000/upload", files=files)
                if response.status_code == 200:
                    st.success("🤖 SIGNAL RESTORED TO MAXIMUM FIDELITY!")
                    st.audio(response.content, format='audio/wav')
                    st.download_button("📥 EXTRACT CLEAN DECODED FILE", response.content, file_name="cleaned.wav")
                else:
                    st.error(">> SYSTEM ERROR: CORE BACKEND FAULT RECOGNIZED.")
            except:
                st.error("⚠️ INTERCEPT LINK SEVERED: Local node offline. UI operating on isolated cloud container.")
    else:
        st.warning(">> WARNING: Please insert input payload before system activation.")

# ---- FOOTER FEATURES SECTION ----
st.markdown("""
<div class='feature-grid'>
    <div class='feature-box'><h4 style='color:#ff007f;'>[01] VOCAL ISOLATION MATRIX</h4><p style='color:#8fa0dd; font-size:0.85rem;'>Strips severe overlapping acoustic artifacts using custom neural suppression grids.</p></div>
    <div class='feature-box'><h4 style='color:#ff007f;'>[02] TENSOR-FLOW GRAPH</h4><p style='color:#8fa0dd; font-size:0.85rem;'>Real-time spectral analysis powered by automated matrix processing weights.</p></div>
</div>
""", unsafe_allow_html=True)
