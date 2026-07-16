import streamlit as st

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="RetailBrainAI",
    page_icon="🛒",
    layout="wide"
)

# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1{
    color:#1f77b4;
    text-align:center;
}

h3{
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# Header
# ==========================================

st.title("RetailBrainAI")

st.subheader("AI-Powered Retail Shelf Monitoring System")

st.markdown("""

Welcome to **RetailBrainAI**, an intelligent computer vision platform designed for retail shelf monitoring.

The system uses **YOLOv8** and **Artificial Intelligence** to automatically detect products, analyze shelves, compare deep learning models, and generate smart retail recommendations.

""")

st.divider()

# ==========================================
# Features
# ==========================================

st.header("System Features")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### Product Detection

Detect products on retail shelves using YOLOv8 object detection.
""")

    st.info("""
### Retail Analytics

Analyze shelf inventory with AI-generated statistics.
""")

with col2:

    st.info("""
###  Model Comparison

Compare YOLOv8 Nano, YOLOv8 Small, and Faster R-CNN.
""")

    st.info("""
### Recommendation System

Generate intelligent recommendations based on inventory analysis.
""")

st.divider()

# ==========================================
# System Overview
# ==========================================

st.header("System Overview")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "AI Models",
        "3"
    )

with c2:

    st.metric(
        "Dataset",
        "SKU-110K"
    )

with c3:

    st.metric(
        "Framework",
        "YOLOv8"
    )

st.divider()

# ==========================================
# Workflow
# ==========================================

st.header(" Project Workflow")

st.markdown("""

1.  Upload a retail shelf image.
2.  Detect products using YOLOv8.
3.  Generate analytics automatically.
4.  Produce AI recommendations.
5.  Compare model performance.

""")

st.divider()

# ==========================================
# Navigation
# ==========================================

st.success(" Use the sidebar to explore all project modules.")
