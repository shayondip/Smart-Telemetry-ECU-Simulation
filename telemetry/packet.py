# telemetry/packet.py

from datetime import datetime


class TelemetryPacket:

    def __init__(self, vehicle_id: str, data: dict):

        self.vehicle_id = vehicle_id
        self.data = data
        self.timestamp = datetime.now()

    def to_dict(self):

        return {
            "vehicle_id": self.vehicle_id,
            "timestamp": self.timestamp.isoformat(),
            "data": self.data
        }

    def display(self):

        print("\n========== TELEMETRY PACKET ==========")
        print(f"Vehicle ID : {self.vehicle_id}")
        print(f"Timestamp  : {self.timestamp}")
        print(f"Data       : {self.data}")
        print("======================================")