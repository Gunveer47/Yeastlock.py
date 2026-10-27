import streamlit as st

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
    .stApp, [data-testid="stSidebar"], .block-container {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }
    
    /* Force all input labels, text, and sidebar text to be bright and fully visible */
    label, .stSelectbox label, .stNumberInput label, .stSlider label, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span, [data-testid="stSidebar"] p {
        color: #F8FAFC !important;
        font-weight: 600 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 3. Sidebar Navigation & App Content
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

# Main App Content Area
st.markdown("### Tech Fest Presentation Demo")
st.write("Interactive tool featuring bead mass, treatment time, and inventory tracking.")
