import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 10000)
def f(x):
    return ((np.sqrt(x) - x/2) * np.cos(x**2))

I = np.cumsum(f(x) * (x[1] - x[0]))

print (I[-1])