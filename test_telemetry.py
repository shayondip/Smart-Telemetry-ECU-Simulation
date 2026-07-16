# test_telemetry.py

from telemetry.packet import TelemetryPacket
from telemetry.transmitter import TelemetryTransmitter
from telemetry.receiver import TelemetryReceiver
from telemetry.cloud import CloudServer


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

packet.display()

# Convert packet to dictionary
packet_data = packet.to_dict()


# Create transmitter
transmitter = TelemetryTransmitter()

# Send packet
transmitter.transmit(packet_data)


# Create receiver
receiver = TelemetryReceiver()

# Receive packet
receiver.receive(packet_data)


# Create cloud server
cloud = CloudServer()

# Upload packet
cloud.upload(packet_data)


# Display statistics
print("\nPackets Sent:")
print(transmitter.get_packet_count())

print("\nPackets Received:")
print(receiver.get_packet_count())

print("\nCloud Packets:")
print(cloud.get_total_packets())


print("\nAll Cloud Data:")
print(cloud.get_all_packets())