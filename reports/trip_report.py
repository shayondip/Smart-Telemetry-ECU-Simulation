# reports/trip_report.py

import sqlite3


def generate_trip_report():

    conn = sqlite3.connect("telemetry.db")
    cursor = conn.cursor()

    # Total records
    cursor.execute("SELECT COUNT(*) FROM telemetry")
    total_records = cursor.fetchone()[0]

    # Maximum speed
    cursor.execute("SELECT MAX(speed) FROM telemetry")
    max_speed = cursor.fetchone()[0]

    # Average speed
    cursor.execute("SELECT AVG(speed) FROM telemetry")
    avg_speed = cursor.fetchone()[0]

    # Maximum temperature
    cursor.execute("SELECT MAX(temperature) FROM telemetry")
    max_temperature = cursor.fetchone()[0]

    # Average RPM
    cursor.execute("SELECT AVG(rpm) FROM telemetry")
    avg_rpm = cursor.fetchone()[0]

    conn.close()

    report = {
        "Total Records": total_records,
        "Maximum Speed": max_speed,
        "Average Speed": round(avg_speed, 2) if avg_speed else 0,
        "Maximum Temperature": max_temperature,
        "Average RPM": round(avg_rpm, 2) if avg_rpm else 0
    }

    return report