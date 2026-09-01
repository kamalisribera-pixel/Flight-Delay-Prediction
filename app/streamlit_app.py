import streamlit as st
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


st.set_page_config(
    page_title="Flight Delay Prediction System",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("✈️ Flight Delay Prediction System")

st.markdown("""
Welcome to the **Flight Delay Prediction System**.

Select a page from the sidebar to begin.
""")