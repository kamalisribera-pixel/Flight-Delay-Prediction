from pathlib import Path

import pandas as pd
import streamlit as st

from src.database import FlightDatabase

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
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

history = pd.DataFrame(
    [dict(row) for row in db.get_predictions()]
)

db.close()

# =========================================================
# HEADER
# =========================================================

st.title("📜 Prediction History")

st.markdown("""
Browse previously generated flight delay predictions stored
in the SQLite database.
""")

st.divider()

# =========================================================
# NO DATA
# =========================================================

if history.empty:

    st.info("No predictions have been generated yet.")

    st.stop()

# =========================================================
# SUMMARY
# =========================================================

total_predictions = len(history)

delayed = len(
    history[
        history["prediction"] == 1
    ]
)

on_time = total_predictions - delayed

avg_probability = (
    history["probability"]
    .mean()
)
c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "Predictions",
        total_predictions
    )

with c2:

    st.metric(
        "Delayed",
        delayed
    )

with c3:

    st.metric(
        "On Time",
        on_time
    )

with c4:

    st.metric(
        "Avg Delay Probability",
        f"{avg_probability:.1%}"
    )

st.divider()

# =========================================================
# FILTERS
# =========================================================

left, middle, right = st.columns(3)

with left:

    airlines = ["All"] + sorted(
        history["airline"].unique().tolist()
    )

    selected_airline = st.selectbox(
        "Airline",
        airlines
    )

with middle:

    prediction_filter = st.selectbox(

        "Prediction",

        [
            "All",
            "Delayed",
            "On Time"
        ]
    )

with right:

    search = st.text_input(
        "Search Airport"
    )

# =========================================================
# APPLY FILTERS
# =========================================================

filtered = history.copy()

if selected_airline != "All":

    filtered = filtered[
        filtered["airline"] == selected_airline
    ]

if prediction_filter == "Delayed":

    filtered = filtered[
        filtered["prediction"] == 1
    ]

elif prediction_filter == "On Time":

    filtered = filtered[
        filtered["prediction"] == 0
    ]

if search:

    search = search.upper()

    filtered = filtered[

        filtered["origin"].str.contains(search)

        |

        filtered["destination"].str.contains(search)

    ]

# =========================================================
# FORMAT TABLE
# =========================================================

display = filtered.copy()

display["prediction"] = display["prediction"].map({

    1: "🔴 Delayed",

    0: "🟢 On Time"

})

display["probability"] = (

    display["probability"] * 100

).round(1).astype(str) + "%"

display = display.rename(

    columns={

        "timestamp": "Timestamp",

        "airline": "Airline",

        "origin": "Origin",

        "destination": "Destination",

        "probability": "Delay Probability",

        "prediction": "Prediction"

    }

)

st.table(

    display,

    border=True

)

st.divider()

# =========================================================
# DOWNLOAD
# =========================================================

csv = display.to_csv(index=False)

st.download_button(

    "⬇ Download History",

    csv,

    "prediction_history.csv",

    "text/csv",

    use_container_width=True

)