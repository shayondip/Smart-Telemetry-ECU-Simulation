# test_telemetry.py

from telemetry.packet import TelemetryPacket


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

print("\nDictionary Output:")
print(packet.to_dict())