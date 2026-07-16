import streamlit as st


def show_gauges():

    st.header("Live Vehicle Metrics")

    # First Row
    col1, col2 = st.columns(2)

    with col1:
        st.metric("RPM", "3500 RPM")

    with col2:
        st.metric("Speed", "120 km/h")

    # Second Row
    col3, col4 = st.columns(2)

    with col3:
        st.metric("Temperature", "87 °C")

    with col4:
        st.metric("Fuel Level", "65 %")

    # Third Row
    col5, col6 = st.columns(2)

    with col5:
        st.metric("Battery", "92 %")

    with col6:
        st.metric("Gear Position", "4")

    # Last Row
    st.metric("Telemetry Packets", "1")