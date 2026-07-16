import streamlit as st

st.set_page_config(
    page_title="Product Detection",
    page_icon="📦",
    layout="wide"
)

st.title("Product Detection")

st.warning(
    "Product Detection module is temporarily unavailable in the cloud deployment version."
)

st.info(
    "The object detection pipeline runs successfully in the local environment using YOLOv8 and Faster R-CNN."
)

st.success(
    "All training notebooks, model weights, and inference pipelines are included in the project repository."
)
