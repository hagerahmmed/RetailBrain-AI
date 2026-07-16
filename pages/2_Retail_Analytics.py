import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(

    page_title="Retail Analytics",

    page_icon="📊",

    layout="wide"

)

# ==========================================
# Header
# ==========================================

st.title("Retail Analytics Dashboard")

st.markdown("""

AI-powered analytics for retail shelf monitoring.

""")

st.divider()

# ==========================================
# Session Check
# ==========================================

if "statistics" not in st.session_state:

    st.warning("⚠ Please run Product Detection first.")

    st.stop()

statistics = st.session_state.statistics

# ==========================================
# Metrics
# ==========================================

c1,c2=st.columns(2)

with c1:

    st.metric(

        "Products",

        statistics["products"]

    )

with c2:

    st.metric(

        "Avg Confidence",

        f"{statistics['avg_confidence']:.2f}"

    )

st.divider()

# ==========================================
# Bar Chart
# ==========================================

st.subheader("Products Summary")

fig,ax=plt.subplots(figsize=(5,4))

ax.bar(

    ["Detected Products"],

    [statistics["products"]]

)

st.pyplot(fig)

st.divider()

# ==========================================
# Confidence Gauge
# ==========================================

st.subheader("Confidence Level")

st.progress(

    float(statistics["avg_confidence"])

)

st.caption(

    f"{statistics['avg_confidence']:.2%}"

)
