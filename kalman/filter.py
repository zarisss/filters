class KalmanFilter1D:
    def __init__(self, Q, R, dt):
        self.Q = Q          #omega variance
        self.R = R          #accel_variance
        self.P = 1.0        #error covarience
        self.dt = dt
        self.angle = 0.0

    def reset(self, initial_angle):
        self.angle = initial_angle
        self.P = 1.0

    def update(self, gyro, accel):
        self.angle = self.angle + self.dt * gyro
        self.P = self.P + self.Q

        K = self.P / (self.P + self.R)
        self.angle = self.angle + K * (accel - self.angle)
        self.P = (1 - K) * self.P
        
        return self.angle
    
    def run_filter(self, gyro_data, accel_data):
        self.reset(accel_data[0])
        filtered = [self.angle]
        for i in range(1, len(gyro_data)):
            angle = self.update(gyro_data[i], accel_data[i])
            filtered.append(angle)
        return filtered
