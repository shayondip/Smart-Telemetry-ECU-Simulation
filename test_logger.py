# test_logger.py

from telemetry.packet import TelemetryPacket
from logger.csv_logger import CSVLogger


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

# Display the packet (Optional)
packet.display()

# Convert packet to dictionary
packet_data = packet.to_dict()

# Create CSV Logger object
logger = CSVLogger()

# Save packet to CSV file
logger.save(packet_data)

# Show success message
print("\nTelemetry packet saved to CSV successfully.")