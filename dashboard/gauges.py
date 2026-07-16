import streamlit as st


def show_gauges():

    st.header("Live Vehicle Metrics")

    # Row 1
    col1, col2 = st.columns(2)

    with col1:
        st.metric("RPM", "3500 RPM")

    with col2:
        st.metric("Speed", "120 km/h")

    # Row 2
    col3, col4 = st.columns(2)

    with col3:
        st.metric("Temperature", "87 °C")

    with col4:
        st.metric("Fuel Level", "65 %")

    # Row 3
    col5, col6 = st.columns(2)

    with col5:
        st.metric("Battery", "92 %")

    with col6:
        st.metric("Gear Position", "4")

    # Row 4
    col7, col8 = st.columns(2)

    with col7:
        st.metric("CAN Bus Status", "CONNECTED")

    with col8:
        st.metric("Cooling Fan", "ON")

    # Row 5
    col9, col10 = st.columns(2)

    with col9:
        st.metric("GPS Coordinates",
                  "22.5726 , 88.3639")

    with col10:
        st.metric("Telemetry Packets", "10")

    # Row 6
    st.metric(
        "Last Packet Timestamp",
        "2026-07-16 20:30:45"
    )