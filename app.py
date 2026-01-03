import streamlit as st
from google import genai
from PIL import Image
from pymatgen.core import Structure
from pymatgen.io.cif import CifParser
import io

# 1. Page Configuration
st.set_page_config(page_title="MatNexus", layout="wide")
st.title(" MatNexus: Lab-Bench Debugger")

# Sidebar for API Key
api_key = st.sidebar.text_input("Gemini API Key", type="password")

if api_key:
    try:
        client = genai.Client(api_key=api_key)
        
        uploaded_file = st.file_uploader("Upload XRD/SEM Image", type=["jpg", "png"])

        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Experimental Data", width=400)

            if st.button("Run Diagnostic"):
                with st.spinner("Gemini 3 is analyzing the crystal structure..."):
                    
                    prompt = """
                    You are a Senior Materials Scientist.
                    1. Identify the crystal phase and any impurity peaks in this plot.
                    2. Explain the physics (e.g., peak broadening, lattice strain).
                    3. Provide a valid .CIF (Crystallographic Information File) for this material.
                       Ensure the CIF block starts with 'data_' and is inside a code block.
                    """
                    
                    response = client.models.generate_content(
                        model="gemini-3-flash-preview", 
                        contents=[prompt, image]
                    )
                    
                    st.markdown(response.text)

                    # LOGIC: Extract the CIF file and run Pymatgen Analysis
                    if "data_" in response.text:
                        st.divider()
                        
                        # Extract CIF string from the markdown code block
                        parts = response.text.split("```")
                        cif_data = ""
                        for p in parts:
                            if "data_" in p:
                                cif_data = p.replace("cif", "").strip()
                                break
                        
                        if cif_data:
                            # Feature 1: Download Button
                            st.subheader("Download Crystal Structure")
                            st.download_button(
                                label="Download .CIF File",
                                data=cif_data,
                                file_name="structure_output.cif",
                                mime="text/plain"
                            )

                            # Feature 2: Automated Physical Property Analysis
                            try:
                                parser = CifParser.from_str(cif_data) #
                                structure = parser.get_structures()[0]

                                st.subheader("Automated Material Analysis")
                                col_a, col_b, col_c = st.columns(3) #
                                
                                with col_a:
                                    st.metric("Density", f"{structure.density:.2f} g/cm³") #
                                with col_b:
                                    st.metric("Volume", f"{structure.volume:.2f} Å³") #
                                with col_c:
                                    st.metric("Space Group", f"{structure.get_space_group_info()[0]}") #

                                st.success(f"Verified Composition: {structure.composition.reduced_formula}")
                            
                            except Exception as sim_err:
                                st.warning(f"Note: Scientific verification skipped. {sim_err}")

    except Exception as e:
        if "429" in str(e):
            st.error("Rate limit reached. Please wait 60 seconds.")
        else:
            st.error(f"An error occurred: {e}")
else:
    st.info("Please enter your API key in the sidebar.")