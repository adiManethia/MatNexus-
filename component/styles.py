import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    /* 1. Softer Background - Deep Slate instead of Pure Black/Blue */
    .stApp {
        background: #121417; 
        color: #D1D5DB;
    }
    
    /* 2. Softened Containers - Reducing Contrast Strain */
    [data-testid="stVerticalBlock"] > div:has(div.stExpander), 
    [data-testid="stMetricWidget"], 
    div[data-testid="stForm"],
    .st-emotion-cache-12w0qpk {
        background: #1c1f24 !important;
        border: 1px solid #2d333b !important;
        border-radius: 12px !important;
        padding: 20px;
    }

    /* 3. Emerald Accents - Easier on the eyes than Neon Cyan */
    h1, h2, h3 {
        color: #50C878 !important; /* Emerald Green */
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        letter-spacing: -0.02em;
    }

    /* 4. Refined Buttons - Emerald to Forest Gradient */
    .stButton > button {
        background: linear-gradient(135deg, #50C878, #3e9c5d) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 8px !important;
        height: 3em;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        background: #50C878 !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(80, 200, 120, 0.3);
    }

    /* 5. Metrics Styling */
    [data-testid="stMetricValue"] {
        color: #50C878 !important;
    }

    /* 6. Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1c1f24;
        border-radius: 4px 4px 0 0;
        color: #9CA3AF;
    }
    </style>
    """, unsafe_allow_html=True)