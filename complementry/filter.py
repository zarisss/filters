class Complementry_filter:
    def __init__(self, alpha=0.8, dt=0.01):
        self.alpha = alpha
        self.dt = dt
        self.angle = 0.0

    def reset(self, initial_angle):
        self.initial_angle = initial_angle

    def update(self, gyro, accel):
        self.angle = self.alpha * (self.angle + gyro * self.dt) + ((1 - self.alpha) * accel)
        return self.angle
    
    def run_filter(self, accl_data, gyro_data):
        self.reset(accl_data[0])
        filtered = [self.angle]
        for i in range(1, len(gyro_data)):
            angle = self.update(gyro_data[i], accl_data[i])
            filtered.append(angle)
        return filtered