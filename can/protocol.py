# can/protocol.py

import json


class CANProtocol:
    """
    Handles CAN message encoding, decoding,
    and validation.
    """

    @staticmethod
    def encode_message(message: dict) -> str:
        """
        Convert Python dictionary into JSON string.
        """

        return json.dumps(message)

    @staticmethod
    def decode_message(message: str) -> dict:
        """
        Convert JSON string back into Python dictionary.
        """

        return json.loads(message)

    @staticmethod
    def validate_message(message: dict) -> bool:
        """
        Check whether the CAN message contains
        all required fields.
        """

        required_fields = [
            "can_id",
            "timestamp",
            "data"
        ]

        for field in required_fields:
            if field not in message:
                return False

        return True