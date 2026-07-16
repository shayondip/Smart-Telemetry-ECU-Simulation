class MaintenancePredictor:

    def check_battery_health(self, battery_level):

        if battery_level < 30:
            return "Battery Replacement Recommended"

        return "Battery Health is Good"



    def check_engine_service(self, rpm):

        if rpm > 6000:
            return "Engine Service Recommended"

        return "Engine Performance Normal"



    def check_cooling_system(self, temperature):

        if temperature > 95:
            return "Cooling System Inspection Recommended"

        return "Cooling System Normal"



    def check_sensor_calibration(self, sensor_status):

        if sensor_status is False:
            return "Sensor Calibration Required"

        return "Sensors Working Properly"