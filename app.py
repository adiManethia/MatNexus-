import streamlit as st
from PIL import Image
import io

# Import your custom components
from component.gemini_client import get_gemini_client, process_uploaded_pdfs
from component.visualizer import render_crystal
from component.physics_engine import analyze_structure # Moved to top for cleanliness

# 1. Page Configuration
st.set_page_config(page_title="MatNexus", layout="wide", page_icon="🔬")
st.title("🔬 MatNexus: Lab-Bench Debugger")

# 2. Initialize Client from Component
client = get_gemini_client()

if client:
    tab1, tab2 = st.tabs(["🔬 Lab Debugger", "📚 Literature Miner"])

    # --- TAB 1: XRD/SEM DIAGNOSTIC ---
    with tab1:
        uploaded_file = st.file_uploader("Upload XRD/SEM Image", type=["jpg", "png"])
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Experimental Data", width=400)

            if st.button("Run Diagnostic"):
                with st.spinner("Gemini 3 is analyzing..."):
                    prompt = "Identify the crystal phase and provide a valid .CIF block starting with 'data_'."
                    response = client.models.generate_content(
                        model="gemini-3-flash-preview", 
                        contents=[prompt, image]
                    )
                    st.markdown(response.text)
                    
                    # --- FIXED: CIF EXTRACTION & DASHBOARD (Must be inside the button logic) ---
                    if "data_" in response.text:
                        parts = response.text.split("```")
                        cif_data = ""
                        for p in parts:
                            if "data_" in p:
                                cif_data = p.replace("cif", "").strip()
                                break
                        
                        if cif_data:
                            st.divider()
                            col_left, col_right = st.columns([1, 1])
                            
                            with col_left:
                                st.subheader("📦 Download & Metrics")
                                st.download_button("Download .CIF", data=cif_data, file_name="sample.cif")
                                
                                # Run Physics Analysis
                                try:
                                    results = analyze_structure(cif_data)
                                    if "error" not in results:
                                        st.metric("Density", f"{results['density']:.2f} g/cm³")
                                        st.metric("Volume", f"{results['volume']:.2f} Å³")
                                        st.metric("Space Group", results['space_group'])
                                except Exception as e:
                                    st.error(f"Analysis failed: {e}")

                            with col_right:
                                st.subheader("🧊 3D Unit Cell")
                                render_crystal(cif_data)

    # --- TAB 2: LITERATURE MINER ---
    with tab2:
        st.header("Research Knowledge Miner")
        pdf_files = st.file_uploader("Upload Research Papers", type="pdf", accept_multiple_files=True)
        
        if pdf_files and st.button("🚀 Mine Knowledge"):
            with st.spinner("Processing PDFs through Gemini Files API..."):
                gemini_files = process_uploaded_pdfs(client, pdf_files)
                mining_prompt = "Extract a Markdown comparison table from these papers."
                
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=[*gemini_files, mining_prompt]
                )
                st.markdown(response.text)
else:
    st.warning("⚠️ GEMINI_API_KEY not found. Please check your .env file.")