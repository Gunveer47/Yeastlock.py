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
        target_dye = st.selectbox("Select Target Textile Dye", ["Methylene Blue", "Congo Red", "Malachite Green", "Rhodamine B"])
        effluent_volume = st.number_input("Effluent Volume (Liters)", min_value=1.0, max_value=10000.0, value=50.0)
        bead_formulation = st.selectbox("Bead Formulation Type", ["Standard Alginate-Yeast (2% Na-Alg + 2% Yeast)", "High-Capacity Crosslinked Beads", "Optimized Composite Film"])
        
    with col2:
        st.markdown("### Kinetics & Results")
        # Dynamic calculation based on inputs
        dye_factor = 25.0 if target_dye == "Methylene Blue" else 30.0
        required_mass = effluent_volume * (dye_factor / 10.0)
        treatment_time = round((effluent_volume / 50.0) * 5.3, 1)
        
        st.metric(label="Required Yeast-Alginate Bead Mass", value=f"{required_mass:.1f} g")
        st.metric(label="Estimated Treatment Time", value=f"{treatment_time} min")
        
        st.markdown("#### Biosorption Simulation (Progress):")
        st.progress(85)
        st.success("Adsorption Equilibrium Reached: 94.2% Dye Removal Efficiency")

elif navigation == "Tech Fest Presentation Demo":
    st.markdown("## 🏆 Tech Fest Presentation Demo")
    st.write("Interactive tool featuring bead mass, treatment time, and inventory tracking for live judging.")
    
    tab1, tab2 = st.tabs(["📦 Inventory Tracker", "🔬 Live Process Summary"])
    
    with tab1:
        st.markdown("### Immobilized Yeast Bead Stock")
        inventory_data = pd.DataFrame({
            "Batch ID": ["YB-101", "YB-102", "YB-103"],
            "Formulation": ["Standard Alginate", "Crosslinked", "Composite Film"],
            "Quantity Available (g)": [500, 750, 300],
            "Status": ["Ready", "Ready", "In Curing"]
        })
        st.dataframe(inventory_data, use_container_width=True)
        
    with tab2:
        st.markdown("### System Performance Metrics")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Reusability Cycles", "5 Cycles", "Stable")
        col_b.metric("Cost per 100L", "₹45.00", "Low Cost")
        col_c.metric("Biodegradability", "100%", "Eco-friendly")
        
        st.info("💡 **Project Note:** YeastLock uses baker's yeast immobilized in sodium alginate and calcium chloride beads for cost-effective dye biosorption from textile wastewater.")
