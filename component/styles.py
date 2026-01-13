import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #e0e0e0;
    }
    
    /* Glassmorphism Containers */
    [data-testid="stVerticalBlock"] > div:has(div.stExpander), .stMetric {
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 255, 204, 0.2) !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }

    /* Neon Accents */
    h1, h2, h3 {
        color: #00ffcc !important;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.5);
    }

    /* Primary Button Style */
    .stButton > button {
        background: linear-gradient(45deg, #00ffcc, #0099ff) !important;
        color: black !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 20px !important;
        transition: 0.3s all;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.8);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)