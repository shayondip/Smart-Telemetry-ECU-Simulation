class Battery:
    def __init__(self):
        self.voltage = 12.6
        self.level = 100

    def consume(self):
        if self.level > 0:
            self.level -= 0.05

    def charge(self):
        if self.level < 100:
            self.level += 0.1