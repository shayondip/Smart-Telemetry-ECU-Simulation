class Engine:
    def __init__(self):
        self.running = False
        self.rpm = 0
        self.temperature = 25.0

    def start(self):
        self.running = True
        self.rpm = 800
        print("Engine Started")

    def stop(self):
        self.running = False
        self.rpm = 0
        print("Engine Stopped")

    def accelerate(self, value):
        if self.running:
            self.rpm += value
            if self.rpm > 7000:
                self.rpm = 7000

    def update_temperature(self):
        if self.running:
            self.temperature += 0.2
        else:
            self.temperature -= 0.1

        if self.temperature < 25:
            self.temperature = 25