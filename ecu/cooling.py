class CoolingSystem:
    def __init__(self):
        self.fan_on = False

    def update(self, engine):
        if engine.temperature >= 90:
            self.fan_on = True
            engine.temperature -= 0.5
        else:
            self.fan_on = False