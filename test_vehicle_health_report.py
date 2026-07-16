# test_vehicle_health_report.py

from reports.vehicle_health_report import generate_vehicle_health_report


report = generate_vehicle_health_report()


print("\n========== VEHICLE HEALTH REPORT ==========\n")

if isinstance(report, str):
    print(report)

else:
    print(f"RPM         : {report['RPM']}")
    print(f"Speed       : {report['Speed']} km/h")
    print(f"Temperature : {report['Temperature']} °C")
    print(f"Battery     : {report['Battery']} %")
    print(f"Fuel        : {report['Fuel']} %")

print("\n===========================================\n")