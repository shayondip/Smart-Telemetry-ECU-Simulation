from can.can_frame import CANFrame

frame = CANFrame(
    can_id=0x101,
    data={
        "rpm": 3500,
        "temperature": 87
    }
)

frame.display()
print(frame.to_dict())