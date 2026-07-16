from ai.anomaly_detection import AnomalyDetection


detector = AnomalyDetection()


print(detector.check_engine_temperature(110))

print(detector.check_battery(10))

print(detector.check_fuel(5))

print(detector.check_gps(False))

print(detector.check_can_bus(False))