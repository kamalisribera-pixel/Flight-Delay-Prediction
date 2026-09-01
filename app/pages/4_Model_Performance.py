from pathlib import Path

import pandas as pd
import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# HERO
# =========================================================

st.title("📊 Model Performance")

st.markdown("""
Evaluate and compare the performance of multiple Machine Learning
models trained on more than **517,000 commercial flight records**.

This dashboard summarizes the evaluation metrics, confusion matrices,
and final production model selected for deployment.
""")

st.divider()

# =========================================================
# RESULTS DIRECTORY
# =========================================================

RESULTS = Path("results")
# =========================================================
# LOAD METRICS
# =========================================================

MODELS = {

    "Random Forest":
        "random_forest_metrics.csv",

    "Gradient Boosting":
        "gradient_boosting_metrics.csv",

    "Decision Tree":
        "decision_tree_metrics.csv",

    "Logistic Regression":
        "logistic_regression_metrics.csv"

}

metrics_data = {}

for model, file in MODELS.items():

    path = RESULTS / file

    if path.exists():

        df = pd.read_csv(path)

        metrics_data[model] = {

            row["Metric"]: row["Value"]

            for _, row in df.iterrows()

        }
# =========================================================
# PRODUCTION MODEL
# =========================================================

st.subheader("🏆 Production Model")

rf = metrics_data["Random Forest"]

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric(
        "Accuracy",
        f"{rf['Accuracy']:.2%}"
    )

with c2:
    st.metric(
        "Precision",
        f"{rf['Precision']:.2%}"
    )

with c3:
    st.metric(
        "Recall",
        f"{rf['Recall']:.2%}"
    )

with c4:
    st.metric(
        "F1 Score",
        f"{rf['F1 Score']:.2%}"
    )

with c5:
    st.metric(
        "ROC AUC",
        f"{rf['ROC AUC']:.2%}"
    )

st.success("""
### 🌲 Random Forest

Selected as the production model because it achieved the
best balance between Accuracy, Precision, Recall,
F1 Score and ROC AUC.
""")

st.divider()

# =========================================================
# HELPER FUNCTION
# =========================================================

def show_model(
    model_name: str,
    metrics_file: Path,
    confusion_matrix: Path
):

    st.markdown(
        f"""
    <div class="section-header">

    {model_name}

    </div>
    """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # LOAD METRICS
    # -----------------------------------------------------

    if not metrics_file.exists():

        st.warning("Metrics file not found.")
        return

    metrics = pd.read_csv(metrics_file)

    values = {
        row["Metric"]: row["Value"]
        for _, row in metrics.iterrows()
    }

    # -----------------------------------------------------
    # METRICS + CONFUSION MATRIX
    # -----------------------------------------------------

    col1, col2 = st.columns([1, 1.2])

    with col1:

        st.markdown("#### Evaluation Metrics")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Accuracy",
                f"{values['Accuracy']:.2%}"
            )

            st.metric(
                "Recall",
                f"{values['Recall']:.2%}"
            )

            st.metric(
                "ROC AUC",
                f"{values['ROC AUC']:.2%}"
            )

        with c2:

            st.metric(
                "Precision",
                f"{values['Precision']:.2%}"
            )

            st.metric(
                "F1 Score",
                f"{values['F1 Score']:.2%}"
            )

    with col2:

        st.markdown("#### Confusion Matrix")

        if confusion_matrix.exists():

            st.image(
                confusion_matrix,
                use_container_width=True
            )

        else:

            st.warning(
                "Confusion matrix not found."
            )
    if "Random Forest" in model_name:

        st.success(
            """
**Strengths**

• Highest overall accuracy

• Excellent generalization

• Robust against noisy flight records

• Selected for production deployment
"""
        )

    elif "Gradient" in model_name:

        st.info(
            """
**Strengths**

• Strong predictive performance

• Good balance between bias and variance

• Competitive alternative to Random Forest
"""
        )

    elif "Decision" in model_name:

        st.warning(
            """
**Strengths**

• Fast training

• Highly interpretable

• Lower predictive accuracy on this dataset
"""
        )

    else:

        st.info(
            """
**Strengths**

• Simple baseline model

• Easy to interpret

• Useful benchmark for comparison
"""
        )

    st.divider()
# =========================================================
# INDIVIDUAL MODEL PERFORMANCE
# =========================================================

st.header("📋 Individual Model Evaluation")

show_model(
    "🌲 Random Forest",
    RESULTS / "random_forest_metrics.csv",
    RESULTS / "random_forest_confusion_matrix.png"
)

show_model(
    "🚀 Gradient Boosting",
    RESULTS / "gradient_boosting_metrics.csv",
    RESULTS / "gradient_boosting_confusion_matrix.png"
)

show_model(
    "🌳 Decision Tree",
    RESULTS / "decision_tree_metrics.csv",
    RESULTS / "decision_tree_confusion_matrix.png"
)

show_model(
    "📈 Logistic Regression",
    RESULTS / "logistic_regression_metrics.csv",
    RESULTS / "logistic_regression_confusion_matrix.png"
)


RESULTS = Path("results")
# =========================================================
# MODEL COMPARISON
# =========================================================

st.subheader("🏆 Model Comparison")

comparison = []

...
st.dataframe(...)

st.info("""
### 📌 Performance Summary

• 🌲 **Random Forest** achieved the highest overall performance and was selected for deployment.

• 🚀 **Gradient Boosting** delivered competitive results with strong generalization.

• 🌳 **Decision Tree** trained quickly but showed lower predictive performance.

• 📈 **Logistic Regression** provides an interpretable baseline model for comparison.
""")