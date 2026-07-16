# telemetry/cloud.py


class CloudServer:

    def __init__(self):
        self.cloud_storage = []

    def upload(self, packet: dict):
        """
        Upload telemetry packet to the cloud.
        """

        self.cloud_storage.append(packet)

        print("\n========== CLOUD SERVER ==========")
        print("Telemetry Packet Uploaded Successfully.")
        print(packet)
        print("==================================")

    def get_total_packets(self):
        """
        Returns total packets stored in the cloud.
        """

        return len(self.cloud_storage)

    def get_all_packets(self):
        """
        Returns all cloud packets.
        """

        return self.cloud_storage