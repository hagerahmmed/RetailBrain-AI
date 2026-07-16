import streamlit as st

# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="RetailBrainAI",
    page_icon="🛒",
    layout="wide"
)

# ==========================================
# Hero Section
# ==========================================

st.title("RetailBrainAI")

st.subheader("AI-Powered Retail Shelf Monitoring System")

st.markdown("""

Welcome to **RetailBrainAI**, an intelligent computer vision platform for retail shelf monitoring.

This system uses **YOLOv8** and **Deep Learning** to:

- Detect Products
- Analyze Shelf Inventory
- Compare AI Models
- Generate Smart Recommendations

""")

st.divider()

# ==========================================
# Features
# ==========================================

col1, col2 = st.columns(2)

with col1:

    st.info("""
### Product Detection

Detect products on retail shelves using YOLOv8.
""")

    st.info("""
### Retail Analytics

Generate real-time analytics from detection results.
""")

with col2:

    st.info("""
### Model Comparison

Compare YOLOv8 Nano, Small, and Faster R-CNN.
""")

    st.info("""
### Recommendation System

Receive AI-powered inventory recommendations.
""")

st.divider()

st.success("Use the left sidebar to navigate through the application.")
