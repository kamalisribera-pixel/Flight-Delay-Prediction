from datetime import date, datetime
from pathlib import Path

import streamlit as st

from src.inference import PredictService

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Predict Flight Delay",
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
# LOAD SERVICE
# =========================================================

@st.cache_resource
def load_service():

    return PredictService()


service = load_service()

# =========================================================
# LOAD DROPDOWNS
# =========================================================

airlines = service.get_airlines()

airports = service.get_airports()

# =========================================================
# HERO
# =========================================================

st.markdown(
    """
<div class="hero">

<h1>✈ Flight Delay Prediction</h1>

<p>

Predict whether a scheduled flight is likely to
depart <strong>15 minutes or more</strong> behind schedule.

The prediction is generated using a trained Random Forest
model built from over 500,000 historical US domestic flights.

</p>

</div>
""",
    unsafe_allow_html=True
)

# =========================================================
# FLIGHT INFORMATION
# =========================================================

st.markdown(
    '<div class="section-header">Flight Information</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2)

with left:

    airline = st.selectbox(
        "✈ Airline",
        airlines
    )

    origin = st.selectbox(
        "🛫 Origin Airport",
        airports
    )

    departure_date = st.date_input(
        "📅 Departure Date",
        value=date.today()
    )

with right:

    destinations = service.get_destinations(origin)

    destination = st.selectbox(
        "🛬 Destination Airport",
        destinations
    )

    departure_time = st.time_input(
        "🕒 Departure Time"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# PREDICT BUTTON
# =========================================================

predict = st.button(
    "🚀 Generate Prediction",
    use_container_width=True
)

if not predict:
    st.stop()

# =========================================================
# VALIDATION
# =========================================================

if predict:

    if departure_date < date.today():

        st.error(
            "Departure date cannot be in the past."
        )

        st.stop()

    if origin == destination:

        st.error(
            "Origin and Destination cannot be the same."
        )

        st.stop()

    with st.spinner("Running prediction model..."):

        result = service.predict(

            airline=airline,

            origin=origin,

            destination=destination,

            departure_date=departure_date,

            departure_time=departure_time.strftime(
                "%H:%M"
            )

        )

    delay_probability = result["delay_probability"]

    on_time_probability = result["on_time_probability"]

    prediction = result["prediction"]

    prediction_time = datetime.now()

    # =========================================================
# CONFIDENCE
# =========================================================

if delay_probability < 0.30:

    confidence = "Very High"
    risk = "Low"
    color = "#2ECC71"

elif delay_probability < 0.50:

    confidence = "High"
    risk = "Moderate"
    color = "#F4B942"

elif delay_probability < 0.70:

    confidence = "Medium"
    risk = "Elevated"
    color = "#FF914D"

else:

    confidence = "Low"
    risk = "High"
    color = "#FF6B6B"

# =========================================================
# PREDICTION RESULT
# =========================================================

st.markdown(
    '<div class="section-header">Prediction Result</div>',
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-value">
{delay_probability:.0%}
</div>

<div class="metric-title">
Delay Probability
</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.progress(delay_probability)

with c2:

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-value">
{on_time_probability:.0%}
</div>

<div class="metric-title">
On-Time Probability
</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.progress(on_time_probability)

# =========================================================
# FLIGHT STATUS
# =========================================================

st.markdown(
    '<div class="section-header">Flight Status</div>',
    unsafe_allow_html=True
)

if prediction == 1:

    title = "⚠ Flight Likely Delayed"

    description = (
        "Historical flight patterns indicate a higher "
        "probability of departure delay."
    )

else:

    title = "✅ Flight Likely On Time"

    description = (
        "Based on historical data, the flight is expected "
        "to depart on schedule."
    )

st.markdown(
    f"""
<div class="status-card">

<h2 style="color:{color};">

{title}

</h2>

<p>

{description}

</p>

</div>
""",
    unsafe_allow_html=True
)

# =========================================================
# OPERATIONAL INSIGHTS
# =========================================================

st.markdown(
    '<div class="section-header">Operational Insights</div>',
    unsafe_allow_html=True
)

i1, i2 = st.columns(2)

with i1:

    st.markdown(
        f"""
<div class="info-card">

<div class="info-label">

Delay Risk

</div>

<div class="info-value">

{risk}

</div>

</div>
""",
        unsafe_allow_html=True
    )

with i2:

    st.markdown(
        f"""
<div class="info-card">

<div class="info-label">

Model Confidence

</div>

<div class="info-value">

{confidence}

</div>

</div>
""",
        unsafe_allow_html=True
    )

# =========================================================
# RECOMMENDATION
# =========================================================

st.markdown(
    '<div class="section-header">Recommendation</div>',
    unsafe_allow_html=True
)

if delay_probability < 0.30:

    recommendation = (
        "No operational concerns detected. "
        "Passengers should proceed with normal boarding."
    )

elif delay_probability < 0.60:

    recommendation = (
        "Monitor airport operations and weather "
        "conditions before departure."
    )

else:

    recommendation = (
        "Potential disruption expected. Consider "
        "allowing additional travel time and monitor "
        "airline notifications."
    )

st.markdown(
    f"""
<div class="info-card">

{recommendation}

</div>
""",
    unsafe_allow_html=True
)
# =========================================================
# FLIGHT SUMMARY
# =========================================================

st.markdown(
    '<div class="section-header">Flight Summary</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2)

with left:

    st.markdown(
        f"""
<div class="info-card">

<div class="info-label">

Airline

</div>

<div class="info-value">

{airline}

</div>

<br>

<div class="info-label">

Origin Airport

</div>

<div class="info-value">

{origin}

</div>

<br>

<div class="info-label">

Destination Airport

</div>

<div class="info-value">

{destination}

</div>

</div>
""",
        unsafe_allow_html=True
    )

with right:

    st.markdown(
        f"""
<div class="info-card">

<div class="info-label">

Departure Date

</div>

<div class="info-value">

{departure_date.strftime("%d %B %Y")}

</div>

<br>

<div class="info-label">

Departure Time

</div>

<div class="info-value">

{departure_time.strftime("%H:%M")}

</div>

<br>

<div class="info-label">

Prediction Generated

</div>

<div class="info-value">

{prediction_time.strftime("%d %b %Y • %I:%M %p")}

</div>

</div>
""",
        unsafe_allow_html=True
    )

# =========================================================
# MODEL INFORMATION
# =========================================================

st.markdown(
    '<div class="section-header">Model Information</div>',
    unsafe_allow_html=True
)

m1, m2, m3 = st.columns(3)

with m1:

    st.markdown(
        """
<div class="metric-card">

<div class="metric-value">
RF
</div>

<div class="metric-title">
Model
</div>

</div>
""",
        unsafe_allow_html=True
    )

with m2:

    st.markdown(
        """
<div class="metric-card">

<div class="metric-value">
517K+
</div>

<div class="metric-title">
Training Flights
</div>

</div>
""",
        unsafe_allow_html=True
    )

with m3:

    st.markdown(
        """
<div class="metric-card">

<div class="metric-value">
25
</div>

<div class="metric-title">
Input Features
</div>

</div>
""",
        unsafe_allow_html=True
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
<div style="text-align:center;
padding:30px 0 10px 0;
color:#9BAEC1;
font-size:14px;">

Flight Operations Intelligence Dashboard

<br><br>

Powered by Python • Scikit-Learn • SQLite • Streamlit

</div>
""",
    unsafe_allow_html=True
)