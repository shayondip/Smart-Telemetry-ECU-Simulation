class GPSSensor:
    def __init__(self):
        self.latitude = 22.5726
        self.longitude = 88.3639

    def update(self):
        self.latitude += 0.0001
        self.longitude += 0.0001

    def read(self):
        return self.latitude, self.longitude