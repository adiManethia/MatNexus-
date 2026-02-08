# ⚛️ MatNexus | Computational Materials Hub 
**AI-Driven Phase Identification & Autonomous Discovery Loop**

MatNexus is a professional Materials Informatics platform designed to bridge the gap between raw laboratory characterization and physical reality. By combining the **Gemini 3 Flash** vision-language model with established physics engines like **Pymatgen**, MatNexus provides a validated "Digital Twin" of materials in seconds. (https://matnexusv1.streamlit.app/)

---

## 🚀 The MatNexus Edge
| Feature | Traditional Lab Workflow | MatNexus AI Workflow |
| :--- | :--- | :--- |
| **Phase ID Time** | 2–6 Hours (Manual Search) | **< 30 Seconds** (Vision AI) |
| **Data Correlation** | Manual overlap of XRD/SEM | **Multimodal Synthesis** |
| **Verification** | Manual journal lookup | **Materials Project API Grounding** |
| **Decision Making** | Trial & Error synthesis | **Autonomous Loop Advice** |

---

## 🛠️ Core Workstations

### 1. 🔍 Lab Debugger (The Discovery Engine)
The engine performs cross-correlation between uploaded XRD patterns and SEM micrographs:
* **Crystallography:** Identifies Phase, Space Group, and Lattice Parameters.
* **Morphology:** Extracts grain size and habit, correlating physical observations with peak broadening.
* **CIF Generation:** Automatically exports standardized 3D structural files (.CIF) for simulation.
* **Physics Validation:** Real-time benchmarking against the **Materials Project** to detect lattice discrepancies.

### 2. 📚 Literature Miner (Knowledge Extraction)
Utilizes Gemini’s 1M+ token context window to index multiple research PDFs simultaneously.
* **Automated Extraction:** Converts dense PDF text into structured property tables.
* **Cross-Referencing:** Compares your current lab results with global peer-reviewed standards.

---

## 🧬 Scientific Foundations

### 📡 X-Ray Diffraction (XRD)
MatNexus analyzes diffraction patterns by measuring constructive interference of X-rays scattered by crystal lattice planes, governed by **Bragg's Law**:
$$n\lambda = 2d \sin \theta$$


### 🔬 Scanning Electron Microscopy (SEM)
By mapping surface topography via focused electron beams, the system correlates physical grain habit with the internal crystallographic unit cell.


---

## 🚀 Workstation Capabilities
* **💎 Structural Modeling:** Automated .CIF generation, 3D Unit Cell rendering, and Symmetry analysis.
* **🔬 Physics Validation:** Materials Project API sync, Density benchmarking, and Theoretical XRD simulation.
* **⚡ Property Discovery:** Band Gap estimation ($E_g$), Electronic nature prediction, and Autonomous synthesis advice.

---

## 🏗️ System Architecture
* `app.py`: Main entry point with **Hub-and-Spoke** state-based navigation and a "Scientific Environment" loading screen.
* `component/styles.py`: Custom **Emerald & Slate** Glassmorphism UI (Eye-friendly dark mode).
* `component/physics_engine.py`: Scientific computation using **Pymatgen**.
* `component/mp_client.py`: Real-time grounding via the **Materials Project API**.
* `component/simulator.py`: Synthetic XRD plot generation for experimental peak matching.

---

## 📂 Project Structure
```text
MatNexus/
├── app.py                # Core Streamlit application
├── component/            # Modular scientific & UI logic
│   ├── gemini_client.py  # Gemini 3 Flash Multimodal API
│   ├── physics_engine.py # Crystallography calculations
│   ├── styles.py         # Refined Emerald & Slate CSS
│   └── visualizer.py     # 3D Lattice rendering
├── data/
│   ├── assets/           # UI Icons and XRD/SEM Schematics
│   ├── lab_samples/      # Sample XRD/SEM images
│   └── reference_papers/ # Sample research PDFs for mining
└── requirements.txt      # Project dependencies
``` 

## Setup & repository

1. Clone the repository:
```bash
git clone https://github.com/adiManethia/MatNexus-.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Configure API Keys: Add your API keys to the .env file

4. Run the application:
```bash
streamlit run app.py
```

## 🛠️ Tech Stack
* **AI Model:** Google Gemini 3 Flash (Multimodal)
* **Ground Truth:** Materials Project API
* **Physics Engine:** Pymatgen
* **Visualization:** py3Dmol, Matplotlib, Streamlit

---
**Developed for the 2026 Google Gemini Hackathon** *Accelerating materials research from years to seconds.*
