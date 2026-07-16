# test_logger.py

from telemetry.packet import TelemetryPacket
from logger.log_manager import LogManager


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


# Create Log Manager
log_manager = LogManager()


# Save packet to all loggers
log_manager.save_all(packet_data)


print("\nTelemetry packet saved successfully.")