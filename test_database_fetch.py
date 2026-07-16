from database.database import TelemetryDatabase


db = TelemetryDatabase()


rows = db.get_all_telemetry()


print("\nTelemetry Records:\n")

for row in rows:
    print(row)


db.close_connection()