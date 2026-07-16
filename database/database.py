import sqlite3


class TelemetryDatabase:

    def __init__(self, db_name="telemetry.db"):

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        print("\nDatabase Connected Successfully.")


    def close_connection(self):

        self.connection.close()

        print("Database Connection Closed.")