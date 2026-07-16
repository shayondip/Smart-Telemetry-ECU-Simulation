# test_can.py

from can.can_frame import CANFrame
from can.protocol import CANProtocol
from can.can_bus import CANBus


# Create CAN Bus
bus = CANBus()


# Create CAN Frame
frame = CANFrame(
    can_id=0x101,
    data={
        "rpm": 3500,
        "temperature": 87
    }
)


# Display CAN Frame
frame.display()


# Convert CAN Frame to Dictionary
message = frame.to_dict()


# Encode the Message
encoded_message = CANProtocol.encode_message(message)

print("\nEncoded Message:")
print(encoded_message)


# Decode the Message
decoded_message = CANProtocol.decode_message(encoded_message)

print("\nDecoded Message:")
print(decoded_message)


# Validate the Message
print("\nMessage Validation:")
print(CANProtocol.validate_message(decoded_message))


# Send Message to CAN Bus
bus.send(decoded_message)


# Broadcast all Messages
bus.broadcast()


# Receive Message from CAN Bus
received_message = bus.receive()

print("\nReceived Message:")
print(received_message)


# Error Detection Test
print("\nError Detection:")
print(bus.error_detection(decoded_message))