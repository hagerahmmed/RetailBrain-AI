import streamlit as st

st.set_page_config(
    page_title="Project Information",
    page_icon="ℹ️",
    layout="wide"
)

st.title("RetailBrainAI")

st.markdown("""
### AI-Based Retail Shelf Monitoring System
""")

st.divider()

st.header("Project Objective")

st.write("""
RetailBrainAI is an AI-powered system designed to monitor retail shelves using computer vision and object detection.
""")

st.header("AI Models")

st.write("""
- YOLOv8 Nano
- YOLOv8 Small
- Faster R-CNN
""")

st.header("Dataset")

st.write("""
SKU-110K Dataset
""")

st.header("Technologies")

st.write("""
- Python
- Streamlit
- PyTorch
- Ultralytics YOLO
- OpenCV
- Pandas
""")

st.header("Features")

st.write("""
- Product Detection
- Retail Analytics
- Model Comparison
- Recommendation System
- Download Reports
""")

st.success("Developed for AI Graduation Project ")
