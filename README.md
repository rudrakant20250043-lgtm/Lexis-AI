# 🎙️ Lexis-AI: The Neural Audio Restoration Engine
> **"Turning Noise into Knowledge with Studio-Grade Neural Clarity."**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blueviolet?style=for-the-badge&logo=python)](https://www.python.org/)
[![AI Engine: DeepFilterNet](https://img.shields.io/badge/AI_Engine-DeepFilterNet-FF6F61?style=for-the-badge&logo=pytorch)](https://github.com/Rikorose/DeepFilterNet)
[![Framework: FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

---

## 🌩️ The Problem: "The Audio Barrier"
Educational content on YouTube is a goldmine, but thousands of life-changing lectures are virtually unwatchable due to **aggressive background noise, echo, and poor equipment.** * **The Reality:** 65% of students drop off from videos with poor audio quality.
* **Our Mission:** Silence the chaos, amplify the mentor. 🚀

## ✨ The Solution: Neural Reconstruction
**Lexis-AI** isn't just a filter; it's a high-performance restoration engine. We use **Deep Neural Networks (DNN)** to surgically remove noise while reconstructing lost speech harmonics.

### 🔄 The Workflow
1. **Harvest:** Lossless audio extraction from YouTube via `yt-dlp`.
2. **De-Noise:** Neural Signal Processing using `DeepFilterNet`.
3. **Enhance:** Dynamic gain adjustment for peak clarity.
4. **Deliver:** Streamlined high-fidelity audio for the end-user.

---

## 🛠️ Tech Stack & Neural Architecture

| Layer | Technology | Engineering Role |
| :--- | :--- | :--- |
| **Data Extraction** | `yt-dlp` + `FFmpeg` | Asynchronous Audio Harvesting |
| **AI Core** | `DeepFilterNet` (SOTA) | Neural Signal Processing & Denoising |
| **Backend Logic** | `FastAPI` + `Python 3.10` | High-Concurrency API Management |
| **User Interface** | `Streamlit` | Minimalist UX for Rapid Interaction |
| **Data Management** | `PostgreSQL` | Secure Metadata & Processing Logs |

---

---

## 📂 System Architecture (Under the Hood)

```mermaid
graph LR
    A[YouTube URL] --> B(yt-dlp Extraction)
    B --> C{FastAPI Backend}
    C --> D[DeepFilterNet AI Engine]
    D --> E(FFmpeg Post-Processing)
    E --> F[Streamlit Dashboard]
    F --> G((High-Fidelity Audio))
'''
## 👥 The Lexis-AI Engineering Crew

| Profile | Name | Role |
| :--- | :--- | :--- |
| <img src="https://github.com/rudrakant20250043-lgtm.png" width="50"> | **Rudrakant Mishra** | 🚀 Lead & Documentation |
| <img src="https://github.com/vinsh111.png" width="50"> | **Vinsh Kushwaha** | 🛠️ Audio Extraction |
| <img src="https://github.com/jeelamrutiya08.png" width="50"> | **Jeel Amrutiya** | 📡 Signal Processing |
| <img src="https://github.com/HarshitRepswal.png" width="50"> | **Harshit Repswal** | 🧠 AI/ML Engineer |
| <img src="https://github.com/Swirlyswan248.png" width="50"> | **Manvi Singh** | 🎨 Frontend / UI |
| <img src="https://github.com/lalitbadera001.png" width="50"> | **Lalit Badera** | ⚙️ Backend + Integration |
