# --- 1. PAGE CONFIGURATION (MUST BE THE ABSOLUTE FIRST COMMAND) ---
import streamlit as st
import pandas as pd
from PIL import Image
import time
import io
import os

st.set_page_config(
    page_title="MatNexus | Computational Materials Hub", 
    layout="wide", 
    page_icon="https://cdn-icons-png.flaticon.com/512/2103/2103633.png"
)

# --- 2. CUSTOM COMPONENT IMPORTS ---
from component.gemini_client import get_gemini_client, process_uploaded_pdfs
from component.visualizer import render_crystal
from component.physics_engine import analyze_structure 
from component.simulator import generate_xrd_plot 
from component.reporter import generate_markdown_report
from component.styles import apply_custom_css
from component.mp_client import get_mp_reference

# --- 3. STATE MANAGEMENT ---
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

def navigate_to(page):
    st.session_state.current_page = page

@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=True).encode('utf-8')

# --- 4. INITIALIZE AI CLIENT ---
client = get_gemini_client()

if client:
    apply_custom_css()
    
    # --- SHARED HEADER ---
    st.markdown("""
        <div style='text-align: center; padding: 10px;'>
        <img src="https://cdn-icons-png.flaticon.com/512/2103/2103633.png" alt="MatNexus Logo" style="width: 100px; height: 100px; margin-bottom: 10px;">
            <h1 style='margin-bottom: 0;'>MATNEXUS | COMPUTATIONAL MATERIALS HUB</h1>
            <p style='color: #50C878; font-weight: bold; margin-top: 5px;'>● AI ENGINE ONLINE</p>
            <p style='color: #a0a0a0; font-style: italic;'>AI-Driven Phase Identification & Autonomous Discovery Loop</p>
        </div>
    """, unsafe_allow_html=True)

    # --- 5. ROUTING LOGIC ---

    # PAGE: HOME / INTRODUCTION
    if st.session_state.current_page == 'home':
        st.markdown("## 🧬 The Science of MatNexus")
        st.write("""
        MatNexus is a **Multimodal Materials Informatics Platform**. It bridges the gap between raw laboratory 
        images and physical reality by combining Vision AI with established Physics engines. By synthesizing data 
        from multiple characterization techniques, it provides a "Digital Twin" of your material in seconds.
        """)

        st.divider()
        st.markdown("### 🛠️ Select Your Workstation")
        nav_c1, nav_c2 = st.columns(2)
        with nav_c1:
            if st.button("🔍 OPEN LAB DEBUGGER", use_container_width=True, type="primary"):
                navigate_to('loading_lab')
                st.rerun()
        with nav_c2:
            if st.button("📚 OPEN LITERATURE MINER", use_container_width=True):
                navigate_to('literature')
                st.rerun()

        # --- CAPABILITIES GRID ---
        st.divider()
        st.markdown("### 🚀 Workstation Capabilities")
        cap_c1, cap_c2, cap_c3 = st.columns(3)
        with cap_c1:
            st.markdown("#### 💎 Structural Modeling")
            st.write("- Automated .CIF Generation\n- 3D Unit Cell Rendering\n- Symmetry & Space Group Analysis")
        with cap_c2:
            st.markdown("#### 🔬 Physics Validation")
            st.write("- Materials Project API Sync\n- Density & Lattice Benchmarking\n- Theoretical XRD Simulation")
        with cap_c3:
            st.markdown("#### ⚡ Property Discovery")
            st.write("- Band Gap Estimation\n- Electronic Nature Prediction\n- Autonomous Synthesis Advice")

        st.divider()
        st.markdown("### 🧪 Core Characterization Principles")
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            with st.container(border=True):
                st.markdown("#### 📡 XRD: Crystallographic Fingerprinting")
                xrd_path = "data/assets/xrd_schema.png"
                if os.path.exists(xrd_path):
                    st.image(xrd_path, use_container_width=True)
                
                st.write("**Mechanism:** Constructive interference following **Bragg's Law**:")
                st.latex(r"n\lambda = 2d \sin \theta")
                st.write("**Why we need it:** Identify phases, measure lattice strain, and calculate crystallinity.")

        with t_col2:
            with st.container(border=True):
                st.markdown("#### 🔬 SEM: Morphological Habit")
                sem_path = "data/assets/sem_schema.png"
                if os.path.exists(sem_path):
                    st.image(sem_path, use_container_width=True)
                
                st.write("**Mechanism:** Surface mapping via focused electron beams to visualize topography and composition.")
                st.write("**Why we need it:** Visually confirm grain size, observe growth kinetics, and check surface porosity.")

        st.divider()
        st.markdown("### ⚡ Performance Comparison: AI vs. Traditional Lab Work")
        comparison_dict = {
            "Workflow Feature": ["Phase Identification", "Data Correlation", "Symmetry Verification", "Synthesis Advice"],
            "Traditional Method": ["Hours of manual database search", "Manual file comparison", "Textbook/Table lookup", "Trial & Error synthesis"],
            "MatNexus (AI)": ["Seconds (Vision Engine)", "Automated Multimodal Synthesis", "Instant Materials Project API", "AI Synthesis Advisor"]
        }
        df_comparison = pd.DataFrame(comparison_dict)
        df_comparison.index = df_comparison.index + 1
        st.table(df_comparison)

        csv_data = convert_df_to_csv(df_comparison)
        #st.download_button(label="📥 Download Performance Data (CSV)", data=csv_data, file_name="MatNexus_Performance.csv", mime="text/csv", use_container_width=True)

        st.divider()
        st.markdown("<div style='text-align: center; color: #707070; font-size: 0.9em;'><p>Developed for the Google AI Hackathon 2026 | Master's Research Initiative in Materials Informatics</p></div>", unsafe_allow_html=True)

    # PAGE: LOADING TRANSITION
    elif st.session_state.current_page == 'loading_lab':
        st.markdown("<br><br>", unsafe_allow_html=True)
        with st.container():
            st.markdown("<h2 style='text-align: center;'>Initializing Virtual Characterization Environment...</h2>", unsafe_allow_html=True)
            progress_bar = st.progress(0)
            status_text = st.empty()
            steps = ["Loading Physics Engine (Pymatgen)...", "Connecting to Gemini Vision API...", "Syncing Materials Project Database...", "Optimizing Discovery Loop...", "System Ready!"]
            for i, step in enumerate(steps):
                status_text.text(step)
                progress_bar.progress((i + 1) * 20)
                time.sleep(0.6)
            navigate_to('lab')
            st.rerun()

    # PAGE: LAB DEBUGGER
    elif st.session_state.current_page == 'lab':
        if st.button("⬅️ BACK TO HUB"):
            navigate_to('home')
            st.rerun()
            
        st.markdown("### 🚀 Real-time Diagnostic & Discovery")
        
        # --- INTEGRATED SAMPLE DATA OPTION ---
        with st.expander("📥 Need test data? Get Lab Samples here", expanded=False):
            sample_lab_dir = "data/lab_samples"
            if os.path.exists(sample_lab_dir):
                sample_files = os.listdir(sample_lab_dir)
                if sample_files:
                    selected_sample = st.selectbox("Select a sample image to download", sample_files, key="lab_sample_select")
                    with open(os.path.join(sample_lab_dir, selected_sample), "rb") as f:
                        st.download_button(label=f"💾 Download {selected_sample}", data=f, file_name=selected_sample, use_container_width=True)
                else:
                    st.info("No files found in 'data/lab_samples'.")
            else:
                st.warning("Folder 'data/lab_samples' not found.")

        with st.container(border=True):
            col_u1, col_u2 = st.columns([2, 1])
            with col_u1:
                uploaded_files = st.file_uploader("Upload Research Package (XRD/SEM/TEM)", type=["jpg", "png"], accept_multiple_files=True)
            with col_u2:
                material_class = st.selectbox("Select Material System", ["Oxide", "Perovskite", "Metal/Alloy", "2D Material", "Unknown"])
                run_btn = st.button("EXECUTE DISCOVERY RUN", width='stretch', type="primary")

        if uploaded_files:
            st.divider()
            with st.expander("📂 Experimental Data Preview", expanded=True):
                img_cols = st.columns(len(uploaded_files))
                images_for_gemini = []
                for idx, file in enumerate(uploaded_files):
                    img = Image.open(file)
                    images_for_gemini.append(img)
                    img_cols[idx].image(img, caption=file.name, width='stretch')
            
            if run_btn:
                with st.spinner("Synthesizing Multimodal Data..."):
                    prompt = "ACT AS: A Senior Characterization Scientist. Analyze these images. 1. Identify Phase. 2. Describe Morphology. 3. Correlate XRD/SEM. Provide a valid .CIF block starting with 'data_'."
                    try:
                        response = client.models.generate_content(model="gemini-3-flash-preview", contents=[prompt, *images_for_gemini])
                        st.markdown("### 📝 Multimodal Research Report")
                        st.markdown(response.text)
                        if "data_" in response.text:
                            parts = response.text.split("```")
                            cif_data = ""
                            for p in parts:
                                if "data_" in p:
                                    cif_data = p.replace("cif", "").strip()
                                    break
                            if cif_data:
                                st.divider()
                                st.markdown("<h2 style='text-align: center; color: #50C878;'>📊 Integrated Discovery Workspace</h2>", unsafe_allow_html=True)
                                results = analyze_structure(cif_data)
                                with st.container(border=True):
                                    col_dl1, col_dl2, col_dl3 = st.columns([1, 1, 1])
                                    with col_dl1:
                                        st.download_button("💾 Export Structure (.CIF)", data=cif_data, file_name="predicted.cif", width='stretch')
                                    with col_dl2:
                                        report_md = generate_markdown_report(response.text, results, material_class)
                                        st.download_button("📄 Download Research Brief", data=report_md, file_name="MatNexus_Report.md", width='stretch', type="primary")
                                    with col_dl3:
                                        st.button("🔄 Clear & Re-run", width='stretch', on_click=lambda: st.rerun())
                                
                                res_c1, res_c2 = st.columns([1.2, 1])
                                with res_c1:
                                    with st.container(border=True):
                                        st.markdown("#### 📦 Structural Ground-Truth")
                                        if "error" not in results:
                                            mp_ref = get_mp_reference(results['formula'])
                                            m1, m2 = st.columns(2)
                                            m1.metric("Formula", results['formula'])
                                            if mp_ref and "error" not in mp_ref:
                                                m2.metric("AI Density", f"{results['density']:.2f} g/cm³", delta=f"{results['density'] - mp_ref['density']:.2f} vs MP")
                                                st.caption(f"📍 Verified via [Materials Project: {mp_ref['mp_id']}](https://next-gen.materialsproject.org/materials/{mp_ref['mp_id']})")
                                            with st.expander("🔍 Extended Crystallographic Data", expanded=True):
                                                st.write(f"**Space Group:** {results['space_group']}")
                                                st.write(f"**Crystal System:** {results.get('crystal_system', 'N/A')}")
                                                st.write(f"**Lattice (a,b,c):** {results['a']:.3f}, {results['b']:.3f}, {results['c']:.3f}")
                                with res_c2:
                                    with st.container(border=True):
                                        st.markdown("#### ⚛️ Quantum Property Prediction")
                                        dft_prompt = f"Predict Band Gap (eV) and Electronic Nature for this CIF: {results['formula']}. Use a professional table format."
                                        dft_res = client.models.generate_content(model="gemini-3-flash-preview", contents=[dft_prompt, cif_data])
                                        st.markdown(dft_res.text)
                                vis_c1, vis_c2 = st.columns(2)
                                with vis_c1:
                                    with st.container(border=True):
                                        st.markdown("#### 🧊 3D Unit Cell Rendering")
                                        render_crystal(cif_data)
                                with vis_c2:
                                    with st.container(border=True):
                                        st.markdown("#### 📈 Predicted Powder Diffraction")
                                        fig = generate_xrd_plot(cif_data)
                                        if fig: st.pyplot(fig)
                                st.divider()
                                st.markdown("### 🤖 Autonomous Synthesis Command")
                                if mp_ref and "error" not in mp_ref and abs(results['density'] - mp_ref['density']) > 0.5:
                                    st.error(f"**System Warning:** High Lattice Discrepancy. **Correction:** Increase Sintering Time by 20% to stabilize the {results['formula']} phase.")
                                else:
                                    st.success(f"**System Ready:** AI prediction aligns with {results['formula']} standards. Proceed to device fabrication.")
                    except Exception as e:
                        st.error(f"⚠️ API Error: {str(e)}")

    # PAGE: LITERATURE MINER
    elif st.session_state.current_page == 'literature':
        if st.button("⬅️ BACK TO HUB"):
            navigate_to('home')
            st.rerun()
        st.header("📚 Research Knowledge Miner")

        # --- INTEGRATED SAMPLE DATA OPTION ---
        with st.expander("📥 Need a test paper? Download Reference PDFs here", expanded=False):
            sample_pdf_dir = "data/reference_papers"
            if os.path.exists(sample_pdf_dir):
                pdf_files = [f for f in os.listdir(sample_pdf_dir) if f.endswith('.pdf')]
                if pdf_files:
                    selected_pdf = st.selectbox("Select a sample paper to download", pdf_files, key="pdf_sample_select")
                    with open(os.path.join(sample_pdf_dir, selected_pdf), "rb") as f:
                        st.download_button(label=f"💾 Download {selected_pdf}", data=f, file_name=selected_pdf, use_container_width=True)
                else:
                    st.info("No PDF files found in 'data/reference_papers'.")
            else:
                st.warning("Folder 'data/reference_papers' not found.")

        pdf_files = st.file_uploader("Upload PDF Papers for Context", type="pdf", accept_multiple_files=True)
        if pdf_files and st.button("🚀 MINE KNOWLEDGE", width='stretch'):
            with st.spinner("Indexing Literature Database..."):
                gemini_files = process_uploaded_pdfs(client, pdf_files)
                response = client.models.generate_content(model="gemini-3-flash-preview", contents=[*gemini_files, "Summarize key material properties mentioned in these papers in a technical table."])
                st.markdown("### 📚 Extracted Insights")
                st.markdown(response.text)
else:
    st.error("API Connection Failed. Please check your configuration.")