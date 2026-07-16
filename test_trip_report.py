# test_trip_report.py

from reports.trip_report import generate_trip_report


report = generate_trip_report()


print("\n========== TRIP REPORT ==========\n")

print(f"Total Records        : {report['Total Records']}")
print(f"Maximum Speed        : {report['Maximum Speed']} km/h")
print(f"Average Speed        : {report['Average Speed']} km/h")
print(f"Maximum Temperature : {report['Maximum Temperature']} °C")
print(f"Average RPM          : {report['Average RPM']}")

print("\n=================================\n")