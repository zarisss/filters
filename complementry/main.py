import matplotlib.pyplot as plt
from imu_simulator import IMUSimulator
from filter import Complementry_filter

# Simulate IMU
sim = IMUSimulator()
time, true_angle, gyro_measured, accel_angle = sim.simulate()
dt = time[1] - time[0]

# Run complementary filter
cf = Complementry_filter(alpha=0.8, dt=0.01)
filtered_angle = cf.run_filter(gyro_measured, accel_angle)
# Plot
plt.plot(time, true_angle, label="ground truth")
#plt.plot(time, accel_angle, label="Accel Angle")
#plt.plot(time, gyro_measured.cumsum() * dt, label="Gyro Integrated Angle") #gyro measures angular velocity, gyro_measured.cumsum() * dtprovides angular displacemnt
plt.plot(time, filtered_angle, label="Filtered Angle")
plt.legend()
plt.grid()
plt.title("Complementary Filter Sensor Fusion (OOP)")
plt.show()
