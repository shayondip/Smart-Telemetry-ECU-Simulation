# telemetry/transmitter.py


class TelemetryTransmitter:

    def __init__(self):
        self.packet_counter = 0

    def transmit(self, packet: dict):
        """
        Simulate transmitting a telemetry packet.
        """

        self.packet_counter += 1

        print("\n========== TELEMETRY TRANSMITTER ==========")
        print(f"Packet Number : {self.packet_counter}")
        print("Packet Successfully Transmitted.")
        print(packet)
        print("===========================================")

    def get_packet_count(self):
        """
        Returns the total number of packets sent.
        """

        return self.packet_counter