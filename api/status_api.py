# api/status_api.py

import sqlite3


def get_vehicle_status():

    conn = sqlite3.connect("telemetry.db")
    cursor = conn.cursor()

    query = """
    SELECT can_status
    FROM telemetry
    ORDER BY id DESC
    LIMIT 1
    """

    cursor.execute(query)

    data = cursor.fetchone()

    conn.close()

    if data is None:
        return {
            "message": "No status data found."
        }

    can_status = data[0]

    return {
        "can_status": can_status
    }