import datetime
import pandas as pd
import streamlit as st

# 1. Page Configuration & Custom CSS Styling for High Contrast
st.set_page_config(
    page_title="YeastLock | Smart Biosorption System",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    /* App background and font styling */
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    
    /* Force all input labels and markdown text to be bright and fully visible */
    label, .stSelectbox label, .stNumberInput label, .stSlider label {
        color: #F8FAFC !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    /* Header Container */
    .main-header {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        border-left: 6px solid #00CEC9;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    
    .main-header h1 {
        color: #00CEC9;
        font-size: 2.1rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    
    .main-header p {
        color: #94A3B8;
        font-size: 1.05rem;
        margin: 0;
    }

    /* Vibrant Metric Cards */
    .metric-card {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #00CEC9;
    }
    
    .metric-label {
        font-size: 0.8rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 2. Sidebar Navigation
with st.sidebar:
    st.title("YeastLock v2.0")
    st.caption("Smart Industrial Biosorption System")
    st.markdown("---")

    navigation = st.radio(
        "📍 Control Center Navigation",
        [
            "⚡ Remediation & Dosage Calculator",
            "📦 Bead Batch & Inventory Manager",
        ],
    )

    st.markdown("---")
    st.info(
        "**Tech Fest Presentation Demo**\n\nInteractive tool featuring bead mass, treatment time, and inventory tracking."
    )

# Session State for Batch Inventory
if "batches" not in st.session_state:
    st.session_state.batches = pd.DataFrame(
        [
            {
                "Batch ID": "YL-001",
                "Date Synthesized": "2026-10-20",
                "Storage Temp (°C)": 4.0,
                "Status": "Stored in 0.1M CaCl2",
                "Cycle Count": 3,
            },
            {
                "Batch ID": "YL-002",
                "Date Synthesized": "2026-10-25",
                "Storage Temp (°C)": 4.0,
                "Status": "Active / Viable",
                "Cycle Count": 1,
            },
        ]
    )

# ==============================================================================
# SECTION 1: REMEDIATION & DOSAGE CALCULATOR
# ==============================================================================
if navigation == "⚡ Remediation & Dosage Calculator":

    st.markdown(
        """
        <div class="main-header">
            <h1>🧪 YeastLock Dye Remediation & Dosage Calculator</h1>
            <p>Calculate required bead mass, treatment duration, and monitor color removal efficiency.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.subheader("⚙️ Process Parameters")

        target_dye = st.selectbox(
            "Select Target Textile Dye",
            [
                "Methylene Blue",
                "Crystal Violet",
                "Malachite Green",
                "Congo Red",
            ],
        )

        effluent_volume = st.number_input(
            "Effluent Volume (Liters)",
            min_value=1.0,
            max_value=1000.0,
            value=50.0,
            step=5.0,
        )

        bead_formulation = st.selectbox(
            "Bead Formulation Type",
            [
                "Standard Alginate-Yeast (2% Na-Alg + 2% Yeast)",
                "High-Density Matrix (3% Na-Alg + 4% Yeast)",
            ],
        )

        target_efficiency = st.slider(
            "Target Removal Efficiency (%)",
            min_value=50.0,
            max_value=99.0,
            value=90.0,
            step=1.0,
        )

        st.markdown("<br>", unsafe_allow_html=True)
        # Explicit Action Button as requested
        calculate_btn = st.button(
            "🚀 Run Remediation Simulation", type="primary", use_container_width=True
        )

    with col_right:
        st.subheader("📊 System Calculations & Kinetics")

        # Calculations
        dosage_factor = (
            25.0 if "Standard" in bead_formulation else 18.0
        )  # grams per liter
        required_mass_g = effluent_volume * dosage_factor

        base_time = (effluent_volume / 10.0) * (target_efficiency / 85.0)
        if "High-Density" in bead_formulation:
            base_time *= 0.85

        # Display Metrics (Showing BOTH Bead Mass and Treatment Time)
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">{required_mass_g:.1f} g</div>
                    <div class="metric-label">Required Bead Mass</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

        with m_col2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">{base_time:.1f} min</div>
                    <div class="metric-label">Est. Treatment Time</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.write("**Biosorption Process Simulation (Progress):**")
        st.progress(int(target_efficiency))

        st.markdown("<br>", unsafe_allow_html=True)
        if calculate_btn:
            st.success(
                f"✅ **Simulation Executed:** Successfully calculated parameters for **{target_dye}** across **{effluent_volume} Liters**. Required **{required_mass_g:.1f}g** of yeast beads to achieve **{target_efficiency}%** removal in **{base_time:.1f} minutes**."
            )
        else:
            st.info(
                "💡 Adjust your parameters on the left and click **'Run Remediation Simulation'** to generate live process metrics."
            )


# ==============================================================================
# SECTION 2: BEAD BATCH & INVENTORY MANAGER
# ==============================================================================
elif navigation == "📦 Bead Batch & Inventory Manager":

    st.markdown(
        """
        <div class="main-header">
            <h1>📦 Immobilized Bead Batch & Inventory Manager</h1>
            <p>Track synthesis history, 4°C storage conditions, and reusability cycles.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.5, 1], gap="large")

    with col1:
        st.subheader("📋 Current Active Inventory")
        st.dataframe(
            st.session_state.batches,
            use_container_width=True,
            hide_index=True,
        )

    with col2:
        st.subheader("➕ Register New Bead Batch")
        with st.form("register_batch_form", clear_on_submit=True):
            next_id_num = len(st.session_state.batches) + 1
            b_id = st.text_input("Batch ID", value=f"YL-00{next_id_num}")
            b_date = st.date_input("Synthesis Date", datetime.date.today())
            b_temp = st.number_input(
                "Storage Temperature (°C)", value=4.0, step=0.5
            )
            b_status = st.selectbox(
                "Initial Status",
                [
                    "Active / Viable",
                    "Stored in 0.1M CaCl2",
                    "Regenerated & Recycled",
                ],
            )

            submitted = st.form_submit_button("➕ Add Batch to Inventory")

            if submitted:
                new_batch = pd.DataFrame(
                    [
                        {
                            "Batch ID": b_id,
                            "Date Synthesized": str(b_date),
                            "Storage Temp (°C)": b_temp,
                            "Status": b_status,
                            "Cycle Count": 0,
                        }
                    ]
                )
                st.session_state.batches = pd.concat(
                    [st.session_state.batches, new_batch], ignore_index=True
                )
                st.success(f"Batch **{b_id}** successfully registered!")
                st.rerun()

    st.markdown("---")
    st.subheader("📌 Quality Control Guidelines")
    q1, q2, q3 = st.columns(3)
    with q1:
        st.markdown(
            "**🌡️ Cold Storage**\n\nKeep at 4°C in 0.1M $CaCl_2$ to maintain gel structural integrity."
        )
    with q2:
        st.markdown(
            "**🔄 Reusability**\n\nBeads endure up to 5 desorptive wash cycles successfully."
        )
    with q3:
        st.markdown(
            "**⏱️ Shelf Life**\n\nBatches older than 14 days require viability checks."
        )