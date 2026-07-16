import streamlit as st
import pandas as pd

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Model Comparison",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# Header
# ==========================================

st.title("📈 Model Comparison")

st.markdown("""
Compare the performance of different object detection models used in RetailBrain AI.
""")

st.divider()

# ==========================================
# Comparison Table
# ==========================================

comparison = pd.DataFrame({

    "Model":[
        "YOLOv8 Nano",
        "YOLOv8 Small",
        "Faster R-CNN"
    ],

    "Precision":[
        "--",
        "--",
        "--"
    ],

    "Recall":[
        "--",
        "--",
        "--"
    ],

    "mAP50":[
        "--",
        "--",
        "--"
    ],

    "mAP50-95":[
        "--",
        "--",
        "--"
    ],

    "FPS":[
        "--",
        "--",
        "--"
    ]

})

st.dataframe(
    comparison,
    use_container_width=True
)

st.divider()

# ==========================================
# Model Details
# ==========================================

st.subheader("Model Information")

st.markdown("""

### YOLOv8 Nano
- Fastest model
- Lightweight
- Suitable for real-time inference

### YOLOv8 Small
- Higher accuracy
- Moderate inference speed
- Better feature extraction

### Faster R-CNN
- High detection accuracy
- Slower inference
- Suitable for offline analysis

""")

st.divider()

st.info(
    "The comparison table will be automatically updated after training and evaluating all models."
)
