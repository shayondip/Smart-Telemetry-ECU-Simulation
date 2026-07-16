import streamlit as st
import pandas as pd
import sqlite3


# ----------------------------------
# Get RPM Data
# ----------------------------------
def get_rpm_data():

    conn = sqlite3.connect("telemetry.db")

    query = "SELECT rpm FROM telemetry"

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# ----------------------------------
# Get Speed Data
# ----------------------------------
def get_speed_data():

    conn = sqlite3.connect("telemetry.db")

    query = "SELECT speed FROM telemetry"

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# ----------------------------------
# Get Temperature Data
# ----------------------------------
def get_temperature_data():

    conn = sqlite3.connect("telemetry.db")

    query = "SELECT temperature FROM telemetry"

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# ----------------------------------
# Get Battery Data
# ----------------------------------
def get_battery_data():

    conn = sqlite3.connect("telemetry.db")

    query = "SELECT battery FROM telemetry"

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# ----------------------------------
# Get Fuel Data
# ----------------------------------
def get_fuel_data():

    conn = sqlite3.connect("telemetry.db")

    query = "SELECT fuel FROM telemetry"

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# ----------------------------------
# Display All Dashboard Charts
# ----------------------------------
def show_charts():

    st.header("Vehicle Performance Graphs")

    # RPM Graph
    st.subheader("RPM Graph")
    rpm_df = get_rpm_data()
    st.line_chart(rpm_df)

    # Speed Graph
    st.subheader("Speed Graph")
    speed_df = get_speed_data()
    st.line_chart(speed_df)

    # Temperature Graph
    st.subheader("Temperature Graph")
    temperature_df = get_temperature_data()
    st.line_chart(temperature_df)

    # Battery Graph
    st.subheader("Battery Graph")
    battery_df = get_battery_data()
    st.line_chart(battery_df)

    # Fuel Level Graph
    st.subheader("Fuel Level Graph")
    fuel_df = get_fuel_data()
    st.line_chart(fuel_df)