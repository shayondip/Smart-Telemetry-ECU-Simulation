# dashboard/charts.py

import streamlit as st
import pandas as pd
import sqlite3


# -----------------------------
# Get RPM data from SQLite DB
# -----------------------------
def get_rpm_data():

    conn = sqlite3.connect("telemetry.db")

    query = "SELECT rpm FROM telemetry"

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# -----------------------------
# Show Graphs on Dashboard
# -----------------------------
def show_charts():

    st.header("Vehicle Performance Graphs")

    # RPM Graph
    st.subheader("RPM Graph")

    rpm_df = get_rpm_data()

    st.line_chart(rpm_df)