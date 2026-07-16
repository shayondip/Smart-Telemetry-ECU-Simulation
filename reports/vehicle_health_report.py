# reports/vehicle_health_report.py

import sqlite3


def generate_vehicle_health_report():

    conn = sqlite3.connect("telemetry.db")

    cursor = conn.cursor()

    query = """
    SELECT rpm, speed, temperature, battery, fuel
    FROM telemetry
    ORDER BY id DESC
    LIMIT 1
    """

    cursor.execute(query)

    data = cursor.fetchone()

    conn.close()

    if data is None:
        return "No telemetry data found."

    rpm, speed, temperature, battery, fuel = data

    report = {
        "RPM": rpm,
        "Speed": speed,
        "Temperature": temperature,
        "Battery": battery,
        "Fuel": fuel
    }

    return report