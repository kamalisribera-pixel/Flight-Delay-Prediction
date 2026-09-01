import streamlit as st


# =========================================================
# HERO
# =========================================================

def hero():

    st.markdown(
        """
        <div class="hero">

            <h1>✈ Flight Operations Intelligence</h1>

            <p>
                Machine Learning powered flight delay prediction system
                trained on over <b>517,000</b> historical US flights.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# KPI CARD
# =========================================================

def metric_card(title, value):

    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-title">
                {title}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# SECTION CARD
# =========================================================

def info_card(title, body):

    st.markdown(
        f"""
        <div class="info-card">

            <h3>{title}</h3>

            <p>{body}</p>

        </div>
        """,
        unsafe_allow_html=True
    )