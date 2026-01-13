# ⚛️ MatNexus: Autonomous Materials Discovery Hub
**Bridging Experimental Morphology with Quantum Crystallography**

MatNexus is a multimodal Materials Informatics platform that transforms raw laboratory data (XRD/SEM) into physics-validated "Digital Twins". By leveraging the **Gemini 3 Flash** multimodal engine and the **Materials Project API**, it reduces the materials-to-market timeline by automating the identification, verification, and simulation of new compounds.

---

## 🚀 The MatNexus Edge
| Feature | Traditional Lab Workflow | MatNexus AI Workflow |
| :--- | :--- | :--- |
| **Phase ID Time** | 2–6 Hours (Manual Search) | **< 30 Seconds** (Automated) |
| **Data Correlation** | Manual overlap of XRD/SEM | **Multimodal Synthesis** |
| **Verification** | Manual journal lookup | **Materials Project API** |
| **Decision Making** | Trial & Error synthesis | **Autonomous Loop Advice** |

---

## 🛠️ Core Modules

### 1. 🔬 Multimodal Lab Debugger
The Vision Engine performs cross-correlation between uploaded XRD patterns and SEM micrographs:
* **Crystallography:** Identifies Phase, Space Group, and Lattice Parameters.
* **Morphology:** Extracts grain size and shape, correlating them with Scherrer peak broadening.
* **CIF Generation:** Exports standardized 3D structural files (.CIF) automatically.



### 2. ⚛️ Quantum Discovery (AI-DFT Proxy)
MatNexus predicts the electronic nature of your sample before you run a single supercomputer simulation:
* **Band Gap Prediction:** Estimates $E_g$ (eV) and electronic nature (Metal/Semiconductor) based on identified symmetry.
* **3D Visualization:** Real-time 3D unit cell rendering using `py3Dmol`.



### 3. 🤖 Autonomous Synthesis Loop
The engine detects discrepancies between your experimental data and the **Materials Project** ground truth.
* **Correction Logic:** If density or lattice deviations are high, the system issues an "Autonomous Command" (e.g., "Increase sintering time by 20%") to stabilize the target phase.



### 4. 📚 Literature Miner
Utilizes Gemini's 1M+ token context window to index multiple research PDFs. It extracts property tables and compares your lab results with global literature in seconds.

---

## 🏗️ Project Architecture
- `app.py`: Streamlit interface with Glassmorphism UI and Multimodal logic.
- `component/mp_client.py`: Real-time grounding via the Materials Project API.
- `component/physics_engine.py`: Scientific computation using Pymatgen.
- `component/simulator.py`: Synthetic XRD plot generation for peak matching.
- `component/reporter.py`: Automated Research Brief generation with LaTeX support.



## 🛠️ Tech Stack
* **AI Model:** Google Gemini 3 Flash (Multimodal)
* **Ground Truth:** Materials Project API
* **Physics Engine:** Pymatgen
* **Visualization:** py3Dmol, Matplotlib, Streamlit

---
**Developed for the 2026 Google Gemini Hackathon** *Accelerating materials research from years to seconds.*
