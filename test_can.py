# test_can.py

from can.can_frame import CANFrame
from can.protocol import CANProtocol


# Create a CAN frame
frame = CANFrame(
    can_id=0x101,
    data={
        "rpm": 3500,
        "temperature": 87
    }
)

# Display the CAN frame
frame.display()

# Convert CAN frame to dictionary
message = frame.to_dict()

# Encode the message
encoded_message = CANProtocol.encode_message(message)

print("\nEncoded Message:")
print(encoded_message)

# Decode the message
decoded_message = CANProtocol.decode_message(encoded_message)

print("\nDecoded Message:")
print(decoded_message)

# Validate the message
is_valid = CANProtocol.validate_message(decoded_message)

print("\nMessage Validation:")
print(is_valid)