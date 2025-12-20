import numpy as np

# damped harmonic motion
class damped_shm:
    def __init__(self, A, w, phi, gamma):
        self.A = A
        self.w = w
        self.phi = np.deg2rad(phi)
        self.gamma = gamma
        self.t = np.linspace(0, 2*np.pi, 100)

    # displacement
    def x(self, t):
        return self.A * np.exp(-self.gamma*t) * np.sin(self.w*t + self.phi)

    # velocity
    def v(self, t):
        return self.A * np.exp(-self.gamma*t) * (
            self.w*np.cos(self.w*t + self.phi)
            - self.gamma*np.sin(self.w*t + self.phi)
        )

    # acceleration
    def a(self, t):
        return self.A * np.exp(-self.gamma*t) * (
            (self.gamma**2 - self.w**2) * np.sin(self.w*t + self.phi)
            - 2*self.w*self.gamma * np.cos(self.w*t + self.phi)
        )

    # kinetic energy
    def ke(self, t):
        return 0.5 * self.w * (
            self.A**2 * np.exp(-2*self.gamma*t) - self.x(t)**2
        )

    # potential energy
    def pe(self, t):
        return 0.5 * self.w * self.x(t)**2

    # total energy
    def te(self, t):
        return self.ke(t) + self.pe(t)
