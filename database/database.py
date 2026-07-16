import sqlite3


class TelemetryDatabase:

    def __init__(self, db_name="telemetry.db"):

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        print("\nDatabase Connected Successfully.")

    def insert_telemetry(
            self,
            vehicle_id,
            timestamp,
            rpm,
            speed,
            temperature,
            battery,
            fuel,
            gps,
            gear,
            can_status,
            cooling_fan
    ):

        self.cursor.execute("""

        INSERT INTO telemetry(

            vehicle_id,
            timestamp,
            rpm,
            speed,
            temperature,
            battery,
            fuel,
            gps,
            gear,
            can_status,
            cooling_fan

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        """,

        (
            vehicle_id,
            timestamp,
            rpm,
            speed,
            temperature,
            battery,
            fuel,
            gps,
            gear,
            can_status,
            cooling_fan
        ))

        self.connection.commit()

        print("\nTelemetry data inserted successfully.")

    def get_all_telemetry(self):

        self.cursor.execute("SELECT * FROM telemetry")

        rows = self.cursor.fetchall()

        return rows

    def close_connection(self):

        self.connection.close()

        print("Database Connection Closed.")