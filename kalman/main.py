import matplotlib.pyplot as plt
from imu_simu import IMUSimulator
from filter import KalmanFilter1D

# Simulate IMU
sim = IMUSimulator()
time, true_angle, gyro_measured, accel_angle = sim.simulate()
# time, _, gyro_measured, accel_angle = sim.from_csv("imu_data.csv") ##used when using csv files

dt = time[1] - time[0]

# Run complementary filter
kf = KalmanFilter1D(Q=0.001, R=0.1, dt=0.01)
filtered_angle = kf.run_filter(gyro_measured, accel_angle)

# Plot
plt.plot(time, true_angle, label="ground truth")
plt.plot(time, accel_angle, label="Accel Angle")
plt.plot(time, gyro_measured.cumsum() * dt, label="Gyro Integrated Angle") #gyro measures angular velocity, gyro_measured.cumsum() * dtprovides angular displacemnt
plt.plot(time, filtered_angle, label="Filtered Angle")
plt.legend()
plt.grid()
plt.title("Kalman Filter Sensor Fusion (OOP)")
plt.show()
