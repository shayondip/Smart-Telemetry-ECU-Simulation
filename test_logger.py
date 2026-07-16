# test_logger.py

from telemetry.packet import TelemetryPacket
from logger.csv_logger import CSVLogger
from logger.json_logger import JSONLogger


# Create Telemetry Packet
packet = TelemetryPacket(
    vehicle_id="ECU-001",
    data={
        "rpm": 3500,
        "speed": 120,
        "temperature": 87,
        "fuel": 65
    }
)

# Display packet
packet.display()

# Convert packet to dictionary
packet_data = packet.to_dict()


# CSV Logger
csv_logger = CSVLogger()
csv_logger.save(packet_data)


# JSON Logger
json_logger = JSONLogger()
json_logger.save(packet_data)


print("\nTelemetry packet saved successfully.")