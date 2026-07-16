# logger/json_logger.py

import json
import os


class JSONLogger:

    def __init__(self, filename="telemetry_log.json"):
        self.filename = filename

    def save(self, packet: dict):
        """
        Save telemetry packet into a JSON file.
        """

        # Create file if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump([], file, indent=4)

        # Read existing data
        with open(self.filename, "r") as file:
            data = json.load(file)

        # Append new packet
        data.append(packet)

        # Write updated data
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

        print("\n[JSON LOGGER] Packet saved successfully.")