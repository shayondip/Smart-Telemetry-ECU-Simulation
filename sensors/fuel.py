class FuelSensor:
    def __init__(self):
        self.level = 100

    def consume(self):
        if self.level > 0:
            self.level -= 0.2

    def read(self):
        return self.level