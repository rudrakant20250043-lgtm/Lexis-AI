import streamlit as st
import time
import os

# ---- BACKEND CONNECTION ----
try:
    # Tumhari backend_model.py file se restore_audio function import ho raha hai
    from backend_model import restore_audio
    MODEL_READY = True
except ImportError:
    MODEL_READY = False

# Page Config
st.set_page_config(page_title="Lexis AI - Neural Restoration", layout="centered", initial_sidebar_state="collapsed")

# ---- ULTRA ANIMATED CYBERPUNK CSS ----
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0c0a24 0%, #020208 100%);
        background-image: 
            linear-gradient(rgba(18, 16, 54, 0.3) 1px, transparent 1px),
            linear-gradient(90deg, rgba(18, 16, 54, 0.3) 1px, transparent 1px);
        background-size: 40px 40px;
        color: #00ffcc;
        font-family: 'Courier New', Courier, monospace;
    }
    h1 {
        background: linear-gradient(90deg, #00ffcc, #ff007f, #00ffcc);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem !important;
        font-weight: 900 !important;
        text-align: center;
        letter-spacing: 4px !important;
        animation: shine 4s linear infinite;
    }
    @keyframes shine { to { background-position: 200% center; } }
    .sub-text { text-align: center; color: #8fa0dd; font-size: 1rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 40px; }
    .metric-container { display: flex; justify-content: space-between; gap: 15px; margin-bottom: 30px; }
    .metric-card { background: rgba(5, 5, 20, 0.75); border: 1px solid #00ffcc; padding: 15px; border-radius: 5px; text-align: center; flex: 1; }
    .metric-val { color: #ff007f; font-size: 1.6rem; font-weight: bold; }
    .metric-lbl { color: #00ffcc; font-size: 0.75rem; }
    div[data-testid="stFileUploader"] { background: rgba(5, 5, 15, 0.8) !important; border: 2px solid #00ffcc !important; padding: 30px !important; }
    div.stButton > button { background: transparent !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; width: 100%; padding: 15px !important; text-transform: uppercase; }
    div.stButton > button:hover { background: #ff007f !important; border-color: #ff007f !important; box-shadow: 0 0 35px #ff007f !important; }
    </style>
""", unsafe_allow_html=True)

# ---- APP HEADER ----
st.markdown("<h1>LEXIS AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>// NEURAL SPECTRUM INTERPOLATION CORE ACTIVE</p>", unsafe_allow_html=True)

# ---- LIVE METRICS BAR ----
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
        if not MODEL_READY:
            st.error("⚠️ SYSTEM ERROR: 'backend_model.py' not found in root directory.")
        else:
            # --- DYNAMIC PROCESSING ANIMATION ---
            status_box = st.empty()
            progress_bar = st.progress(0)
            steps = [">> Injecting vectors...", ">> Isolating noise...", ">> Tensor convolution...", ">> Re-synthesizing...", ">> Exporting..."]
            
            for idx, step in enumerate(steps):
                status_box.markdown(f"📡 `{step}`")
                progress_bar.progress((idx + 1) * 20)
                time.sleep(0.5)
            
            status_box.empty()
            progress_bar.empty()
            
            # --- CLOUD PROCESSING LOGIC ---
            with st.spinner("Locking signal arrays..."):
                input_p = "temp_input.wav"
                output_p = "temp_output.wav"
                
                try:
                    # Save temporary file
                    with open(input_p, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Direct function call from your backend_model.py
                    success = restore_audio(input_p, output_p)
                    
                    if success and os.path.exists(output_p):
                        st.success("🤖 SIGNAL RESTORED TO MAXIMUM FIDELITY!")
                        with open(output_p, "rb") as f:
                            st.audio(f.read(), format='audio/wav')
                            st.download_button("📥 EXTRACT CLEAN DECODED FILE", f, file_name="cleaned.wav")
                    else:
                        st.error(">> SYSTEM ERROR: Model processing failed.")
                except Exception as e:
                    st.error(f"⚠️ SYSTEM FAULT: {str(e)}")
    else:
        st.warning(">> WARNING: Please insert input payload before system activation.")

# ---- FOOTER ----
st.markdown("""
<div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 50px;'>
    <div style='background: rgba(5,5,15,0.6); border: 1px solid rgba(0,255,204,0.2); padding: 15px;'>
        <h4 style='color:#ff007f;'>[01] VOCAL ISOLATION</h4>
        <p style='color:#8fa0dd; font-size:0.85rem;'>Neural suppression grids active.</p>
    </div>
    <div style='background: rgba(5,5,15,0.6); border: 1px solid rgba(0,255,204,0.2); padding: 15px;'>
        <h4 style='color:#ff007f;'>[02] TENSOR-FLOW</h4>
        <p style='color:#8fa0dd; font-size:0.85rem;'>Real-time spectral analysis.</p>
    </div>
</div>
""", unsafe_allow_html=True)
