import streamlit as st
from gauges import show_gauges
from charts import show_charts


# ------------------------------------
# Page Configuration
# ------------------------------------

st.set_page_config(
    page_title="Smart Telemetry ECU Dashboard",
    layout="wide"
)


# ------------------------------------
# Dashboard Title
# ------------------------------------

st.title("Smart Telemetry ECU Simulation")

st.subheader(
    "Professional Automotive Telemetry Dashboard"
)


# ------------------------------------
# Vehicle Information
# ------------------------------------

st.header("Vehicle Information")

vehicle_id = "ECU-001"

st.write(f"Vehicle ID : {vehicle_id}")


# ------------------------------------
# System Status
# ------------------------------------

st.header("System Status")

st.success("Telemetry System Running")

st.success("CAN Bus Connected")

st.success("Cloud Server Connected")


# ------------------------------------
# Live Vehicle Metrics
# ------------------------------------

show_gauges()


# ------------------------------------
# Vehicle Performance Charts
# ------------------------------------

show_charts()


# ------------------------------------
# Footer
# ------------------------------------

st.markdown("---")

st.write(
    "Smart Telemetry ECU Simulation Project"
)