# 🔬 MatNexus: AI-Powered Lab-Bench Debugger

**MatNexus** is an intelligent assistant designed to accelerate materials science research. It bridges the gap between raw experimental data (XRD/SEM) and verified physical properties using the **Gemini 3 Flash** multimodal model and the **Pymatgen** physics engine.

## 🌟 Key Features
* **🔬 Lab Debugger (Tab 1):** Upload an XRD plot or SEM image. Gemini 3 identifies the phases, explains the underlying physics, and generates a valid Crystallographic Information File (.CIF).
* **🧊 3D Crystal Visualization:** Interactive 3D rendering of the predicted crystal structure directly in the browser using `stmol`.
* **🧬 Physical Verification:** Automated calculation of Density, Volume, and Space Group symmetry via `Pymatgen` to verify the AI's predictions.
* **📚 Literature Miner (Tab 2):** Leveraging Gemini 3’s 1M+ token context window to cross-reference multiple research PDFs simultaneously for comparative analysis.

## 🏗️ Project Architecture
The project is built with a modular structure for scalability:
- `app.py`: Main Streamlit interface and UI logic.
- `component/gemini_client.py`: Handles Google GenAI Files API and model connections.
- `component/physics_engine.py`: Scientific computation using Pymatgen.
- `component/visualizer.py`: 3D rendering logic using py3Dmol.

## 🛠️ Tech Stack
- **AI Model:** Google Gemini 3 Flash (Multimodal)
- **Framework:** Streamlit
- **Scientific Libraries:** Pymatgen, Matplotlib
- **Visualization:** stmol, py3Dmol
- **Environment:** Python 3.12, python-dotenv

## 🚀 Getting Started
1. Clone the repo:
   ```bash
   git clone [https://github.com/your-username/matnexus.git](https://github.com/your-username/matnexus.git)
