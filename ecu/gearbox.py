class Gearbox:
    def __init__(self):
        self.gear = 1

    def shift_up(self):
        if self.gear < 6:
            self.gear += 1

    def shift_down(self):
        if self.gear > 1:
            self.gear -= 1