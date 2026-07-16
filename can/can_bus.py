# can/can_bus.py

from can.protocol import CANProtocol


class CANBus:

    def __init__(self):
        self.messages = []

    def send(self, message: dict):
        """
        Send a CAN message.
        """

        if CANProtocol.validate_message(message):
            self.messages.append(message)
            print("\n[CAN BUS] Message Sent Successfully.")
        else:
            print("\n[CAN BUS ERROR] Invalid Message.")

    def receive(self):
        """
        Receive the oldest CAN message.
        """

        if self.messages:
            return self.messages.pop(0)

        return None

    def broadcast(self):
        """
        Display all CAN messages currently
        stored in the CAN bus.
        """

        print("\n========== CAN BUS ==========")

        if not self.messages:
            print("No Messages Found.")
            return

        for message in self.messages:
            print(message)

        print("=============================")

    def error_detection(self, message: dict):
        """
        Detect invalid CAN messages.
        """

        return not CANProtocol.validate_message(message)