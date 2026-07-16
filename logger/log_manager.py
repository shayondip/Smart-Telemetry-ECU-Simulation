from logger.csv_logger import CSVLogger
from logger.json_logger import JSONLogger
from database.database import TelemetryDatabase


class LogManager:

    def __init__(self):

        self.csv_logger = CSVLogger()
        self.json_logger = JSONLogger()
        self.database = TelemetryDatabase()

    def save_all(self, packet: dict):

        # Save CSV
        self.csv_logger.save(packet)

        # Save JSON
        self.json_logger.save(packet)

        # Save SQLite Database
        self.database.insert_telemetry(

            vehicle_id=packet["vehicle_id"],
            timestamp=packet["timestamp"],

            rpm=packet["data"]["rpm"],
            speed=packet["data"]["speed"],
            temperature=packet["data"]["temperature"],
            battery=packet["data"]["battery"],
            fuel=packet["data"]["fuel"],

            gps=packet["data"]["gps"],
            gear=packet["data"]["gear"],

            can_status=packet["data"]["can_status"],
            cooling_fan=packet["data"]["cooling_fan"]

        )

        print("\n[LOG MANAGER] All logs saved successfully.")

    def close(self):

        self.database.close_connection()