import streamlit as st
import pandas as pd
import random


def show_charts():

    st.header("Vehicle Performance Graphs")

    # RPM Data
    rpm_data = [random.randint(1000, 7000) for _ in range(20)]

    st.subheader("RPM Graph")
    st.line_chart(rpm_data)

    # Speed Data
    speed_data = [random.randint(20, 180) for _ in range(20)]

    st.subheader("Speed Graph")
    st.line_chart(speed_data)

    # Temperature Data
    temperature_data = [random.randint(70, 110) for _ in range(20)]

    st.subheader("Temperature Graph")
    st.line_chart(temperature_data)