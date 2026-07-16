from datetime import datetime


class CANFrame:

    def __init__(self, can_id: int, data: dict):
        self.can_id = can_id
        self.data = data
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            "can_id": self.can_id,
            "timestamp": self.timestamp.isoformat(),
            "data": self.data
        }

    def display(self):
        print("\n========== CAN FRAME ==========")
        print(f"CAN ID     : {hex(self.can_id)}")
        print(f"Timestamp  : {self.timestamp}")
        print(f"Data       : {self.data}")
        print("================================")