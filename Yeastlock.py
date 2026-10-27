import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="YeastLock | Smart Industrial Biosorption System",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Bulletproof Dark Theme CSS Styling
st.markdown(
    """
    <style>
    /* Force entire app, container, and sidebar background to dark */
    .stApp, [data-testid="stSidebar"], .block-container, [data-testid="stHeader"] {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }
    
    /* Force all input labels, text, and sidebar text to be bright and fully visible */
    label, p, span, h1, h2, h3, h4, .stSelectbox label, .stNumberInput label, .stSlider label, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span, [data-testid="stSidebar"] p {
        color: #F8FAFC !important;
        font-weight: 600 !important;
    }
    
    /* Highlight metrics for high visibility */
    div[data-testid="stMetricValue"] {
        color: #38BDF8 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 3. Sidebar Navigation Control Center
# ==========================================
with st.sidebar:
    st.title("YeastLock v2.0")
    st.caption("Smart Industrial Biosorption System")
    st.markdown("---")
    
    navigation = st.radio(
        "Control Center Navigation",
        [
            "Remediation & Dosage Calculator",
            "Tech Fest Presentation Demo"
        ]
    )

# ==========================================
# 4. Main Application Views
# ==========================================
if navigation == "Remediation & Dosage Calculator":
    st.markdown("## ⚗️ YeastLock Dye Remediation & Dosage Calculator")
    st.write("Calculate required bead mass, treatment time, and adsorption efficiency for industrial effluent treatment.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Process Parameters")
        
