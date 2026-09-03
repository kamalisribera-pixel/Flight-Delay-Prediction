from pathlib import Path

import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
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
# HEADER
# =========================================================

st.title("ℹ️ About")

st.markdown("""
The **Flight Delay Prediction System** is an end-to-end Machine Learning
application that predicts whether a scheduled flight will be delayed by
**15 minutes or more** using historical U.S. flight data.

It demonstrates the complete ML lifecycle—from data preprocessing to model
deployment through an interactive Streamlit application.
""")

st.divider()

# =========================================================
# PROJECT SNAPSHOT
# =========================================================

st.header("📊 Project Snapshot")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Flights", "517,222")

with c2:
    st.metric("Features", "25")

with c3:
    st.metric("ML Models", "4")

with c4:
    st.metric("Database", "SQLite")

st.divider()

# =========================================================
# MACHINE LEARNING PIPELINE
# =========================================================

st.header("⚙️ Machine Learning Pipeline")

st.code("""
Raw Dataset
      │
      ▼
Data Validation
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Preprocessing
      │
      ▼
Train / Test Split
      │
      ▼
 ┌──────────────┬──────────────┬──────────────┬
 │              │              │              │
 ▼              ▼              ▼              ▼
Logistic     Decision      Random        Gradient
Regression     Tree         Forest        Boosting
 │              │              │              │
 └──────────────┴──────────────┴──────────────┘
                    │
                    ▼
            Model Evaluation
                    │
                    ▼
      Best Model Selection
                    │
                    ▼
         Random Forest Model
                    │
      ┌─────────────┴─────────────┐
      ▼                           ▼
SQLite Database           Streamlit App
      │                           │
      └─────────────┬─────────────┘
                    ▼
             Flight Delay Prediction
""")

st.divider()

# =========================================================
# MODELS
# =========================================================

st.header("🤖 Machine Learning Models")

left, right = st.columns(2)

with left:

    st.success("🌲 Random Forest")
    st.success("🚀 Gradient Boosting")

with right:

    st.success("🌳 Decision Tree")
    st.success("📈 Logistic Regression")

st.divider()

# =========================================================
# APPLICATION FEATURES
# =========================================================

st.header("✨ Application Features")

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
- ✈ Flight Delay Prediction
- 📊 Model Performance Dashboard
- 📜 Prediction History
- 💾 SQLite Integration
""")

with c2:

    st.markdown("""
- 🧠 Feature Engineering
- ⚡ Hyperparameter Optimization
- 📈 Interactive Analytics
- 🎨 Aerospace Dark Theme
""")

st.divider()

# =========================================================
# TECHNOLOGY STACK
# =========================================================

st.header("🛠 Technology Stack")

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
### Programming

- Python
- SQL
""")

with c2:

    st.markdown("""
### Libraries

- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
""")

with c3:

    st.markdown("""
### Tools

- Streamlit
- SQLite
- Joblib
- Git
""")

st.divider()

# =========================================================
# PROJECT STRUCTURE
# =========================================================

st.header("📁 Project Structure")

st.code("""
FDP/
│
├── app/
├── src/
├── scripts/
├── models/
├── database/
├── data/
├── reports/
└── results/
""")

st.divider()

# =========================================================
# DEVELOPER
# =========================================================

st.header("👨‍💻 Developer")

st.info("""
**Lucky KB**

AI Engineer • Machine Learning • Python • Software Engineering
""")

st.divider()

st.caption(
    "Flight Delay Prediction System • End-to-End Machine Learning Project • Version 1.0"
)
