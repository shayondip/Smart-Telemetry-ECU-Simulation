from telemetry.packet import TelemetryPacket
from logger.log_manager import LogManager


# Create Telemetry Packet
packet = TelemetryPacket(
    vehicle_id="ECU-001",
    data={
        "rpm": 3500,
        "speed": 120,
        "temperature": 87,
        "battery": 92,
        "fuel": 65,
        "gps": "22.5726,88.3639",
        "gear": 4,
        "can_status": "CONNECTED",
        "cooling_fan": "ON"
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


# Close database connection
log_manager.close()


print("\nTelemetry packet saved successfully.")