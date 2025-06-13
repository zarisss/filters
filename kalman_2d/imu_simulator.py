import numpy as np

class IMUSim:

    def __init__(self, T=5, dt=0.01, noise_std=1.0, mode="sine"):
        self.T = T
        self.dt = dt
        self.noise_std = noise_std
        self.mode = mode
    def simulator(self):
        time = np.arange(0, self.T, self.dt)
        if self.mode == "sine":
            position_true = 10 * np.sin(2 * np.pi * time)
            velocity_true = np.gradient(position_true * self.dt)

        elif self.mode == "linear":
            velocity_true = 2 * np.ones_like(time)
            position_true = np.cumsum(velocity_true * self.dt)
        
        else:
            raise ValueError("Unsupported mode. Use 'sine' or 'linear'.")
        
        noise = position_true + np.random.normal(0, self.noise_std, size=len(position_true))

        return time, position_true, velocity_true, noise
