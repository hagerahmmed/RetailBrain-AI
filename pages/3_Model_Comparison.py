import streamlit as st
import plotly.express as px

from utils.comparison import load_results

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

st.title("Model Comparison")

st.write(
    "Compare the performance of different object detection models used in RetailBrainAI."
)

st.divider()

# ==========================================
# Load Results
# ==========================================

comparison = load_results()

# ==========================================
# Results Table
# ==========================================

st.subheader("Performance Comparison")

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================
# mAP50 Chart
# ==========================================

st.subheader("mAP50 Comparison")

fig1 = px.bar(
    comparison,
    x="Model",
    y="mAP50",
    text="mAP50",
    title="Model Accuracy"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================================
# Precision Chart
# ==========================================

st.subheader("Precision Comparison")

fig2 = px.bar(
    comparison,
    x="Model",
    y="Precision",
    text="Precision",
    title="Precision"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================================
# Recall Chart
# ==========================================

st.subheader("Recall Comparison")

fig3 = px.bar(
    comparison,
    x="Model",
    y="Recall",
    text="Recall",
    title="Recall"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================================
# Inference Time
# ==========================================

st.subheader("Inference Time")

fig4 = px.bar(
    comparison,
    x="Model",
    y="Inference Time",
    text="Inference Time",
    title="Inference Time (Seconds)"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.divider()

# ==========================================
# Best Model
# ==========================================

best_model = comparison.loc[
    comparison["mAP50"].idxmax()
]

st.success(
    f"""
Best Performing Model

Model: {best_model['Model']}

mAP50: {best_model['mAP50']}

Precision: {best_model['Precision']}

Recall: {best_model['Recall']}
"""
)

st.divider()

# ==========================================
# Download Results
# ==========================================

csv = comparison.to_csv(index=False)

st.download_button(
    label="Download Comparison Results",
    data=csv,
    file_name="Model_Comparison.csv",
    mime="text/csv",
    use_container_width=True
)
