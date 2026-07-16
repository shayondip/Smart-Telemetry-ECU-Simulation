# dashboard/charts.py

import streamlit as st
import random


def show_charts():

    st.header("Vehicle Performance Graphs")

    # ----------------------------------
    # RPM Graph
    # ----------------------------------

    rpm_data = [random.randint(1000, 7000) for _ in range(20)]

    st.subheader("RPM Graph")
    st.line_chart(rpm_data)

    # ----------------------------------
    # Speed Graph
    # ----------------------------------

    speed_data = [random.randint(20, 180) for _ in range(20)]

    st.subheader("Speed Graph")
    st.line_chart(speed_data)

    # ----------------------------------
    # Temperature Graph
    # ----------------------------------

    temperature_data = [random.randint(70, 110) for _ in range(20)]

    st.subheader("Temperature Graph")
    st.line_chart(temperature_data)

    # ----------------------------------
    # Fuel Graph
    # ----------------------------------

    fuel_data = [random.randint(10, 100) for _ in range(20)]

    st.subheader("Fuel Level Graph")
    st.line_chart(fuel_data)

    # ----------------------------------
    # Battery Graph
    # ----------------------------------

    battery_data = [random.randint(20, 100) for _ in range(20)]

    st.subheader("Battery Graph")
    st.line_chart(battery_data)