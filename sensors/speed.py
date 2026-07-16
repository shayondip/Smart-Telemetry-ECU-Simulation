class SpeedSensor:
    def calculate(self, rpm, gear):
        return (rpm / 100) * gear * 0.25