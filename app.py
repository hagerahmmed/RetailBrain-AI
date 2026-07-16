import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="RetailBrain AI",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🛒 RetailBrain AI")

st.subheader("AI-Powered Smart Retail Shelf Monitoring System")

st.markdown("---")

# --------------------------------------------------
# Project Description
# --------------------------------------------------

st.markdown("""
Welcome to **RetailBrain AI**, an intelligent retail analytics platform powered by Computer Vision and Deep Learning.

This system enables retailers to:

- 📦 Detect products automatically.
- 📊 Analyze shelf occupancy.
- 📈 Monitor product density.
- 🤖 Generate smart retail insights.
- 💡 Support inventory management.
""")

st.markdown("---")

# --------------------------------------------------
# Dashboard Metrics
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Model", "YOLOv8")

with col2:
    st.metric("Dataset", "SKU-110K")

with col3:
    st.metric("Framework", "Streamlit")

with col4:
    st.metric("Status", "Ready")

st.markdown("---")

# --------------------------------------------------
# Quick Start
# --------------------------------------------------

st.info("👈 Use the sidebar to navigate through the project pages.")

st.success("RetailBrain AI is ready to use.")
