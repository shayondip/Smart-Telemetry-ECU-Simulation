# api/telemetry_api.py

import sqlite3


def get_latest_telemetry():

    conn = sqlite3.connect("telemetry.db")

    cursor = conn.cursor()

    query = """
    SELECT rpm,
           speed,
           temperature,
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
        return {
            "message": "No telemetry data found."
        }

    rpm, speed, temperature, battery, fuel = data

    return {
        "rpm": rpm,
        "speed": speed,
        "temperature": temperature,
        "battery": battery,
        "fuel": fuel
    }