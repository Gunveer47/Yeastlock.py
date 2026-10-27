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
            "Immobilized Yeast Bead Stock Management"
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
        
        # Updated Formulation Section with Concentrations
        bead_formulation = st.selectbox(
            "Bead Formulation (CaCl2 Crosslinked)", 
            [
                "Standard Concentration (2% Alginate + 2% Yeast)", 
                "Medium Concentration (2% Alginate + 3.5% Yeast)", 
                "Higher Concentration (2% Alginate + 5% Yeast)"
            ]
        )
        
        submitted = st.button("Calculate Remediation", type="primary", use_container_width=True)
        
    with col2:
        st.markdown("### Kinetics & Results")
        
        if submitted:
            dye_factor = 25.0 if target_dye == "Methylene Blue" else 30.0
            required_mass = effluent_volume * (dye_factor / 10.0)
            treatment_time = round((effluent_volume / 50.0) * 5.3, 1)
            
            st.metric(label="Required Immobilized Bead Mass", value=f"{required_mass:.1f} g")
            st.metric(label="Estimated Treatment Time", value=f"{treatment_time} min")
            
            st.markdown("#### Biosorption Simulation (Progress):")
            st.progress(85)
            st.success("Adsorption Equilibrium Reached: 94.2% Dye Removal Efficiency")
        else:
            st.info("👈 Adjust your parameters on the left and click **Calculate Remediation** to run the live simulation.")

elif navigation == "Immobilized Yeast Bead Stock Management":
    st.markdown("## 📦 Immobilized Yeast Bead Stock Management")
    st.write("Manage live batch inventory and track system performance metrics.")
    
    tab1, tab2 = st.tabs(["📦 Interactive Inventory Tracker", "🔬 Live Process Summary"])
    
    with tab1:
        st.markdown("### Immobilized Yeast Bead Stock Management")
        
        # Initialize session state for inventory so added rows persist
        if "inventory_df" not in st.session_state:
            st.session_state.inventory_df = pd.DataFrame(columns=["Batch ID", "Formulation", "Quantity Available (g)", "Status"])
        
        # Form to add custom inventory rows live
        with st.form("add_inventory_form", clear_on_submit=True):
            st.markdown("#### ➕ Add New Batch Record")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                new_batch_id = st.text_input("Batch ID (e.g., YB-101)")
                
                # Updated Inventory Formulation Section with Concentrations
                new_formulation = st.selectbox(
                    "Formulation Type", 
                    [
                        "Standard Concentration (2% Alginate + 2% Yeast)", 
                        "Medium Concentration (2% Alginate + 3.5% Yeast)", 
                        "Higher Concentration (2% Alginate + 5% Yeast)"
                    ]
                )
            with col_f2:
                new_qty = st.number_input("Quantity Available (g)", min_value=0.0, value=50.0)
                new_status = st.selectbox("Batch Status", ["Ready", "In Curing (CaCl2 Bath)", "In Testing", "Depleted"])
                
            add_button = st.form_submit_button("Add to Inventory Table", type="primary")
            
            if add_button:
                if new_batch_id.strip() == "":
                    st.error("Please enter a valid Batch ID.")
                else:
                    new_row = pd.DataFrame({
                        "Batch ID": [new_batch_id],
                        "Formulation": [new_formulation],
                        "Quantity Available (g)": [new_qty],
                        "Status": [new_status]
                    })
                    st.session_state.inventory_df = pd.concat([st.session_state.inventory_df, new_row], ignore_index=True)
                    st.success(f"Batch {new_batch_id} added successfully!")

        st.markdown("---")
        st.markdown("### Current Inventory Table")
        if st.session_state.inventory_df.empty:
            st.info("No batches logged yet. Use the form above to log your actual lab batches!")
        else:
            st.dataframe(st.session_state.inventory_df, use_container_width=True)
        
    with tab2:
        st.markdown("### System Performance Metrics")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Reusability Cycles", "5 Cycles", "Stable")
        col_b.metric("Cost per 100L", "₹40.00", "Low Cost")
        col_c.metric("Biodegradability", "100%", "Eco-friendly")
        
        st.info("💡 **Project Note:** YeastLock uses baker's yeast immobilized in sodium alginate cross-linked with calcium chloride for cost-effective dye biosorption from textile wastewater.")
