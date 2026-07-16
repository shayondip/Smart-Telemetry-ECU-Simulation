class AnomalyDetection:

    def check_engine_temperature(self, temperature):

        if temperature > 100:
            return "WARNING : ENGINE OVERHEAT"

        return "Engine Temperature Normal"



    def check_battery(self, battery):

        if battery < 20:
            return "WARNING : LOW BATTERY"

        return "Battery Level Normal"



    def check_fuel(self, fuel):

        if fuel < 15:
            return "WARNING : LOW FUEL"

        return "Fuel Level Normal"



    def check_gps(self, gps_status):

        if gps_status is False:
            return "WARNING : GPS FAILURE"

        return "GPS Working Properly"



    def check_can_bus(self, can_status):

        if can_status is False:
            return "WARNING : CAN BUS FAILURE"

        return "CAN BUS CONNECTED"