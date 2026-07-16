from ai.maintenance import MaintenancePredictor


predictor = MaintenancePredictor()


print(predictor.check_battery_health(20))

print(predictor.check_engine_service(7000))

print(predictor.check_cooling_system(105))

print(predictor.check_sensor_calibration(False))