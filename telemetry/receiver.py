# telemetry/receiver.py


class TelemetryReceiver:

    def __init__(self):
        self.received_packets = []

    def receive(self, packet: dict):
        """
        Receive and store a telemetry packet.
        """

        self.received_packets.append(packet)

        print("\n========== TELEMETRY RECEIVER ==========")
        print("Packet Successfully Received.")
        print(packet)
        print("========================================")

    def get_packet_count(self):
        """
        Returns the total number of packets received.
        """

        return len(self.received_packets)

    def get_all_packets(self):
        """
        Returns all received packets.
        """

        return self.received_packets