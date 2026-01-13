import streamlit as st
from PIL import Image
import io

# Import custom components
from component.gemini_client import get_gemini_client, process_uploaded_pdfs
from component.visualizer import render_crystal
from component.physics_engine import analyze_structure 
from component.simulator import generate_xrd_plot 
from component.reporter import generate_markdown_report
from component.styles import apply_custom_css
from component.mp_client import get_mp_reference

# 1. Page Configuration
st.set_page_config(
    page_title="MatNexus | Computational Materials Hub", 
    layout="wide", 
    page_icon="⚛️"
)

# 2. Initialize Client
client = get_gemini_client()

if client:
    apply_custom_css()
    
    # --- HEADER SECTION ---
    st.markdown("""
        <div style='text-align: center; padding: 10px;'>
            <h1 style='color: #00ffcc; margin-bottom: 0;'>MATNEXUS : VIRTUAL CHARACTERIZATION LAB</h1>
            <p style='color: #a0a0a0; font-style: italic;'>AI-Driven Phase Identification & Autonomous Discovery Loop</p>
        </div>
    """, unsafe_allow_html=True)
    
    # --- MAIN NAVIGATION ---
    tab_theory, tab_lab, tab_miner = st.tabs(["📖 INTRODUCTION", "🚀 LAB DEBUGGER", "📚 LITERATURE MINER"])

    # --- TAB: THEORY HUB ---
    with tab_theory:
        st.markdown("## 🧬 The Science of MatNexus")
        st.write("""
        MatNexus is a **Multimodal Materials Informatics Platform**. It bridges the gap between raw laboratory 
        images and physical reality by combining Vision AI with established Physics engines.
        """)
        
        st.markdown("### ⚡ Performance Comparison: AI vs. Traditional Lab Work")
        comparison_data = {
            "Workflow Feature": ["Phase Identification", "Data Correlation", "Symmetry Verification", "Synthesis Advice"],
            "Traditional Method": ["Hours of manual database search", "Manual file comparison", "Textbook/Table lookup", "Trial & Error synthesis"],
            "MatNexus (AI)": ["Seconds (Vision Engine)", "Automated Multimodal Synthesis", "Instant Materials Project API", "AI Synthesis Advisor"]
        }
        st.table(comparison_data)
        
        st.divider()

        t_col1, t_col2 = st.columns(2)
        with t_col1:
            with st.container(border=True):
                st.markdown("### 📡 XRD Analysis")
                st.write("**What it is:** X-Ray Diffraction measures the 'atomic fingerprint'.")
                st.latex(r"n\lambda = 2d \sin \theta")
                st.info("💡 **Application:** Use XRD to identify 'who' is in your sample and check for lattice strain.")

        with t_col2:
            with st.container(border=True):
                st.markdown("### 🔬 SEM Analysis")
                st.write("**What it is:** Scanning Electron Microscopy reveals physical morphology.")
                st.info("💡 **Application:** Use SEM to identify 'how' your material is shaped (Habit) and check for porosity.")

        st.divider()
        st.markdown("### 🗺️ Discovery Roadmap: MatNexus v2.0")
        r_col1, r_col2 = st.columns(2)
        with r_col1:
            st.markdown("#### ⚛️ Quantum Simulation (DFT)")
            st.write("Predict electronic band structures and thermal stability directly from generated .CIF files.")
        with r_col2:
            st.markdown("#### 🤖 Autonomous Lab Integration")
            st.write("Self-driving lab loops where MatNexus identifies a failure and adjusts the 'recipe' automatically.")

    # --- TAB: LAB DEBUGGER ---
    with tab_lab:
        st.markdown("### 🚀 Real-time Diagnostic & Discovery")
        with st.container(border=True):
            col_u1, col_u2 = st.columns([2, 1])
            with col_u1:
                uploaded_files = st.file_uploader(
                    "Upload Research Package (XRD/SEM/TEM)", 
                    type=["jpg", "png"], 
                    accept_multiple_files=True
                )
            with col_u2:
                material_class = st.selectbox(
                    "Select Material System", 
                    ["Oxide", "Perovskite", "Metal/Alloy", "2D Material", "Unknown"]
                )
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
                with st.spinner("Synthesizing Multimodal Data & Predicting Properties..."):
                    prompt = f"ACT AS: A Senior Characterization Scientist. Analyze these images. 1. Identify Phase. 2. Describe Morphology. 3. Correlate XRD/SEM. Provide a valid .CIF block starting with 'data_'."
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
                            st.markdown("<h2 style='text-align: center; color: #00ffcc;'>📊 Integrated Discovery Workspace</h2>", unsafe_allow_html=True)
                            results = analyze_structure(cif_data)

                            # --- TOP ROW: PRIMARY ACTIONS ---
                            with st.container(border=True):
                                col_dl1, col_dl2, col_dl3 = st.columns([1, 1, 1])
                                with col_dl1:
                                    st.download_button("💾 Export Structure (.CIF)", data=cif_data, file_name="predicted.cif", width='stretch')
                                with col_dl2:
                                    report_md = generate_markdown_report(response.text, results, material_class)
                                    st.download_button("📄 Download Research Brief", data=report_md, file_name="MatNexus_Report.md", width='stretch', type="primary")
                                with col_dl3:
                                    st.button("🔄 Clear & Re-run", width='stretch', on_click=lambda: st.rerun())

                            # --- MIDDLE ROW: ANALYTICS ---
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

                            # --- BOTTOM ROW: VISUALS & ROBOTICS ---
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

                            # --- FOOTER: AUTONOMOUS COMMAND ---
                            st.divider()
                            st.markdown("### 🤖 Autonomous Synthesis Command")
                            if mp_ref and "error" not in mp_ref and abs(results['density'] - mp_ref['density']) > 0.5:
                                st.error(f"**System Warning:** High Lattice Discrepancy. **Correction:** Increase Sintering Time by 20% to stabilize the {results['formula']} phase.")
                            else:
                                st.success(f"**System Ready:** AI prediction aligns with {results['formula']} standards. Proceed to next stage.")

    with tab_miner:
        st.header("📚 Research Knowledge Miner")
        pdf_files = st.file_uploader("Upload PDF Papers", type="pdf", accept_multiple_files=True)
        if pdf_files and st.button("🚀 MINE KNOWLEDGE", width='stretch'):
            gemini_files = process_uploaded_pdfs(client, pdf_files)
            response = client.models.generate_content(model="gemini-3-flash-preview", contents=[*gemini_files, "Summarize key properties."])
            st.markdown("### 📚 Extracted Insights")
            st.markdown(response.text)
else:
    st.error("API Connection Failed.")