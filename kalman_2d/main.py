import numpy as np
import matplotlib.pyplot as plt
from filter import Kalman_2D
from imu_simulator import IMUSim

#SIMULATE
sim = IMUSim(mode="linear", noise_std=1.0)
time, position_true, velocity_true, noise_measurement = sim.simulator()

#kf
kf = Kalman_2D(Q=0.01, R=1.5, dt=time[1] - time[0])
kf.reset(position=noise_measurement[0], velocity=0)

filtered = kf.run_filter(noise_measurement)

# Plot
plt.plot(time, position_true, label="True Position")
plt.plot(time, velocity_true, label="True Velocity")
plt.plot(time, noise_measurement, label="Noisy Measurement", alpha=0.5)
plt.plot(time, filtered, label="Kalman Estimate")
plt.legend()
plt.grid()
plt.show()