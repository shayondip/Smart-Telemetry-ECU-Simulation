# test_telemetry.py

from telemetry.packet import TelemetryPacket
from telemetry.transmitter import TelemetryTransmitter
from telemetry.receiver import TelemetryReceiver


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

# Transmit Packet
transmitter.transmit(packet_data)


# Create Receiver
receiver = TelemetryReceiver()

# Receive Packet
receiver.receive(packet_data)


# Show Packet Counts
print("\nPackets Sent:")
print(transmitter.get_packet_count())


print("\nPackets Received:")
print(receiver.get_packet_count())


# Display All Received Packets
print("\nAll Received Packets:")
print(receiver.get_all_packets())