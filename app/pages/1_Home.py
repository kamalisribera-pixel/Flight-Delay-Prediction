import streamlit as st
from pathlib import Path

from src.database import FlightDatabase

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Home",
    page_icon="✈️",
    layout="wide"
)

# =========================================================
# LOAD CSS
# =========================================================

def load_css():

    css_file = (
        Path(__file__).resolve().parents[1]
        / "assets"
        / "style.css"
    )

    with open(css_file, encoding="utf-8") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()

# =========================================================
# DATABASE
# =========================================================

db = FlightDatabase()
db.connect()

airlines = len(db.get_airlines())
airports = len(db.get_airports())

db.close()

# =========================================================
# HERO
# =========================================================

st.markdown(
    """
<div class="hero">

<h1>✈ Flight Operations Intelligence</h1>

<p>

Predict whether a scheduled flight will be delayed by
<strong>15 minutes or more</strong> using Machine Learning.

Built on more than <strong>517,000 historical flights</strong>,
the application combines feature engineering,
machine learning, and an interactive dashboard
for real-time flight delay prediction.

</p>

</div>
""",
    unsafe_allow_html=True
)

# =========================================================
# DASHBOARD METRICS
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-value">{airlines}</div>

<div class="metric-title">Airlines</div>

</div>
""",
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-value">{airports}</div>

<div class="metric-title">Airports</div>

</div>
""",
        unsafe_allow_html=True
    )

with c3:

    st.markdown(
        """
<div class="metric-card">

<div class="metric-value">4</div>

<div class="metric-title">ML Models</div>

</div>
""",
        unsafe_allow_html=True
    )

with c4:

    st.markdown(
        """
<div class="metric-card">

<div class="metric-value">SQLite</div>

<div class="metric-title">Database</div>

</div>
""",
        unsafe_allow_html=True
    )

# =========================================================
# MISSION BRIEF
# =========================================================

st.markdown(
    '<div class="section-header">Mission Brief</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="info-card">

The Flight Delay Prediction System is an end-to-end
Machine Learning application that predicts whether a flight
is likely to depart late.

The system integrates

• Data Cleaning

• Feature Engineering

• Model Training

• Hyperparameter Optimization

• SQLite Database

• Interactive Streamlit Dashboard

into one complete prediction pipeline.

</div>
""",
    unsafe_allow_html=True
)

# =========================================================
# MACHINE LEARNING PIPELINE
# =========================================================

st.markdown(
    '<div class="section-header">Machine Learning Pipeline</div>',
    unsafe_allow_html=True
)

p1, p2, p3, p4 = st.columns(4)

with p1:

    st.markdown(
        """
<div class="info-card">

<h3>📂 Data</h3>

Dataset Validation

<br>

Data Cleaning

<br>

Data Profiling

</div>
""",
        unsafe_allow_html=True
    )

with p2:

    st.markdown(
        """
<div class="info-card">

<h3>⚙ Features</h3>

Time Features

<br>

Airport Features

<br>

Route Features

</div>
""",
        unsafe_allow_html=True
    )

with p3:

    st.markdown(
        """
<div class="info-card">

<h3>🤖 Models</h3>

Logistic Regression

<br>

Random Forest

<br>

Gradient Boosting

</div>
""",
        unsafe_allow_html=True
    )

with p4:

    st.markdown(
        """
<div class="info-card">

<h3>💾 Database</h3>

Airlines

<br>

Airports

<br>

Prediction History

</div>
""",
        unsafe_allow_html=True
    )

# =========================================================
# TECHNOLOGY STACK
# =========================================================

st.markdown(
    '<div class="section-header">Technology Stack</div>',
    unsafe_allow_html=True
)

t1, t2, t3 = st.columns(3)

with t1:

    st.markdown(
        """
<div class="info-card">

<h3>🐍 Languages</h3>

Python

<br>

SQL

</div>
""",
        unsafe_allow_html=True
    )

with t2:

    st.markdown(
        """
<div class="info-card">

<h3>📚 Libraries</h3>

Pandas

<br>

NumPy

<br>

Scikit-Learn

</div>
""",
        unsafe_allow_html=True
    )

with t3:

    st.markdown(
        """
<div class="info-card">

<h3>🛠 Tools</h3>

SQLite

<br>

Streamlit

<br>

Joblib

</div>
""",
        unsafe_allow_html=True
    )

# =========================================================
# APPLICATION FEATURES
# =========================================================

st.markdown(
    '<div class="section-header">Application Features</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="info-card">

✈ Flight Delay Prediction

<br><br>

📈 Delay Probability Estimation

<br><br>

📜 Prediction History

<br><br>

📊 Model Performance Dashboard

<br><br>

💾 SQLite Integration

</div>
""",
    unsafe_allow_html=True
)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Flight Operations Intelligence • Version 1.0 • Built with Python, Scikit-Learn, SQLite & Streamlit"
)