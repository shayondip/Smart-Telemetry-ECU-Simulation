# logger/csv_logger.py

import csv
import os


class CSVLogger:

    def __init__(self, filename="telemetry_log.csv"):
        self.filename = filename

    def save(self, packet: dict):
        """
        Save telemetry packet into a CSV file.
        """

        file_exists = os.path.isfile(self.filename)

        with open(self.filename, mode="a", newline="") as file:

            writer = csv.writer(file)

            # Write header only once
            if not file_exists:
                writer.writerow([
                    "Vehicle ID",
                    "Timestamp",
                    "Data"
                ])

            writer.writerow([
                packet["vehicle_id"],
                packet["timestamp"],
                packet["data"]
            ])

        print("\n[CSV LOGGER] Packet saved successfully.")