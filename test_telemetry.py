# test_telemetry.py

from telemetry.packet import TelemetryPacket
from telemetry.transmitter import TelemetryTransmitter


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


# Display Packet
packet.display()


# Convert Packet to Dictionary
packet_data = packet.to_dict()


# Create Transmitter
transmitter = TelemetryTransmitter()


# Send Packet
transmitter.transmit(packet_data)


# Show Total Packets Sent
print("\nTotal Packets Sent:")
print(transmitter.get_packet_count())