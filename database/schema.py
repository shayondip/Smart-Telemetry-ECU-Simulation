import sqlite3


def create_telemetry_table():

    connection = sqlite3.connect("telemetry.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            vehicle_id TEXT NOT NULL,

            timestamp TEXT NOT NULL,

            rpm INTEGER,

            speed INTEGER,

            temperature REAL,

            battery INTEGER,

            fuel INTEGER,

            gps TEXT,

            gear INTEGER,

            can_status TEXT,

            cooling_fan TEXT

        )
    """)

    connection.commit()

    connection.close()

    print("\nTelemetry table created successfully.")