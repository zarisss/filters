import numpy as np

class Kalman_2D:
    def __init__(self, Q, R, dt):
        self.dt = dt
        self.Q = Q * np.eye(2)                     # Process noise covariance
        self.R = np.array([[R]])                   # Measurement noise covariance
        self.H = np.array([[1, 0]])                # Measurement matrix
        self.P = np.eye(2)                         # Estimate error covariance
        self.x = np.zeros((2, 1))                  # State vector [position, velocity]
        self.A = np.array([[1, dt],                # State transition matrix
                           [0, 1]])

    def reset(self, position, velocity=0.0):
        self.x = np.array([[position],
                           [velocity]])
        self.P = np.eye(2)

    def predict(self):
        self.x = self.A @ self.x
        self.P = self.A @ self.P @ self.A.T + self.Q

    def update(self, z):
        z = np.array([[z]])                      # ensure z is a 1x1 column vector, since only position
        y = z - self.H @ self.x                  # Innovation (residual)
        S = self.H @ self.P @ self.H.T + self.R  # Innovation covariance
        K = self.P @ self.H.T @ np.linalg.inv(S) # Kalman Gain
        self.x = self.x + K @ y                  # State update
        self.P = (np.eye(2) - K @ self.H) @ self.P  # Covariance update
        return self.x
    def run_filter(self, measurements):
        filtered = []
        for z in measurements:
            self.predict()
            self.update(z)
            filtered.append(self.x[0, 0])  # store position only
        return filtered
