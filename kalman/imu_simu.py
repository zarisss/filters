###########################MODIFY THIS CODE FOR USING WITH MICROCONTROLLER##############################

import numpy as np

class IMUSimulator:
    def __init__(self, amplitude=30, freq=1, T=5, dt=0.01, gyro_noise_std_deviation=2, gyro_drift=8):
        self.amplitude = amplitude
        self.freq = freq
        self.T = T
        self.dt = dt
        self.gyro_noise_std_deviation = gyro_noise_std_deviation
        self.gyro_drift = gyro_drift
    
    def simulate(self):
        g = 9.81
        time= np.linspace(0, self.T, int(self.T / self.dt))
        angle_in_deg = self.amplitude * np.sin(2 * np.pi * self.freq * time)
        angle_in_rad = np.radians(angle_in_deg)
        true_omega = np.gradient(angle_in_rad, self.dt)
        drift = self.gyro_drift * np.linspace(0, 1, len(time))
        noise = np.random.normal(0, self.gyro_noise_std_deviation, len(time))
        gyro_measured = true_omega + drift + noise

        a_y = g * np.sin(angle_in_rad)
        a_z = g * np.cos(angle_in_rad)
        accel_angle = np.arctan2(a_y, a_z) * 180 / np.pi

        return time, angle_in_deg, gyro_measured, accel_angle
def from_csv(self, filepath):
    import pandas as pd
    data = pd.read_csv(filepath)
    time = data["time"].values
    gyro_measured = data["gyro"].values
    accel_angle = data["accel_angle"].values
    return time, None, gyro_measured, accel_angle
