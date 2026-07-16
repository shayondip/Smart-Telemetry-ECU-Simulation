# reports/fault_report.py

import sqlite3


def generate_fault_report():

    conn = sqlite3.connect("telemetry.db")
    cursor = conn.cursor()

    query = """
    SELECT temperature,
           battery,
           fuel
    FROM telemetry
    ORDER BY id DESC
    LIMIT 1
    """

    cursor.execute(query)

    data = cursor.fetchone()

    conn.close()

    if data is None:
        return ["No telemetry data found."]

    temperature, battery, fuel = data

    faults = []

    # Engine Overheat
    if temperature > 100:
        faults.append("Engine Overheat Detected")

    # Low Battery
    if battery < 20:
        faults.append("Low Battery Warning")

    # Low Fuel
    if fuel < 15:
        faults.append("Low Fuel Warning")

    # No Fault Found
    if len(faults) == 0:
        faults.append("No Faults Detected")

    return faults