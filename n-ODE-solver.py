import numpy as np 
import scipy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ==========================================
# Define physical constants
# ==========================================
g = 9.81  # Acceleration due to gravity (m/s^2)
L = 2.3957 # Length of the pendulum (m)
pi = np.pi
T = 2 * pi * np.sqrt(L / g)  # Period of the pendulum (s)
