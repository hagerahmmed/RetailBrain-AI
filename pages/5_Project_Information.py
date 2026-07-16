import streamlit as st

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Project Information",
    page_icon="ℹ️",
    layout="wide"
)

# ==========================================
# Header
# ==========================================

st.title("Project Information")

st.write(
    "RetailBrainAI is an AI-powered retail shelf monitoring system."
)

st.divider()

# ==========================================
# Project Overview
# ==========================================

st.header("Project Overview")

st.write("""
RetailBrainAI is a computer vision application designed to detect products
on retail shelves using Deep Learning and YOLOv8.

The system provides:

- Product Detection
- Retail Analytics
- Model Comparison
- Smart Recommendation System
- PDF & CSV Reports
""")

st.divider()

# ==========================================
# Technologies
# ==========================================

st.header("Technologies")

st.markdown("""
- Python
- Streamlit
- PyTorch
- YOLOv8
- OpenCV
- Pandas
- Plotly
- ReportLab
""")

st.divider()

# ==========================================
# Dataset
# ==========================================

st.header("Dataset")

st.write("""
SKU-110K Dataset

The dataset contains thousands of retail shelf images with bounding box annotations for product detection.
""")

st.divider()

# ==========================================
# AI Models
# ==========================================

st.header("Object Detection Models")

st.markdown("""
- YOLOv8 Nano
- YOLOv8 Small
- Faster R-CNN
""")

st.divider()

# ==========================================
# Features
# ==========================================

st.header("Project Features")

st.markdown("""
- Product Detection
- Retail Shelf Analytics
- Inventory Recommendation
- Model Comparison
- PDF Report Generation
- CSV Export
""")

st.divider()

# ==========================================
# Future Improvements
# ==========================================

st.header("Future Improvements")

st.markdown("""
- Real-Time Video Detection
- Live Camera Support
- Product Classification
- Cloud Deployment
- Recommendation Engine
""")

st.divider()

# ==========================================
# Footer
# ==========================================

st.caption(
    "RetailBrainAI | AI-Based Retail Shelf Monitoring"
)
