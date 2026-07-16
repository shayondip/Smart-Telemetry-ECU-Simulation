from database.database import TelemetryDatabase


db = TelemetryDatabase()


db.insert_telemetry(

    vehicle_id="ECU-001",

    timestamp="2026-07-17 10:30:00",

    rpm=3500,

    speed=120,

    temperature=87,

    battery=92,

    fuel=65,

    gps="22.5726,88.3639",

    gear=4,

    can_status="CONNECTED",

    cooling_fan="ON"

)


db.close_connection()