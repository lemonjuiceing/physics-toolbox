# Calculus and Statistical functions for Physics
import numpy as np
import matplotlib.pyplot as plt
a1 = 2*np.random.randn(10000) + 10 # note np.random.rand(10000) generates random numbers with a mean of 0 and standard deviation of 1, so we multiply by 2 and add 10 to shift the mean to 10 and scale the standard deviation to 2
a2 = 3*np.random.randn(1000000)# note np.random.rand(10000) generates random numbers with a mean of 0 and standard deviation of 1, so we multiply by 3 which still equates to 0, and since there is no addition, the mean remains 0 and the standard deviation is scaled to 3
print (np.mean(a1)) # mean of the array
print (np.mean(a2)) # mean of the array
print (np.std(a1)) # standard deviation of the array
print (np.std(a2)) # standard deviation of the array
print (np.percentile(a1, 80)) # 80th percentile of the array, 80% of the numbers are less than this value
x1 = np.linspace(0, 10, 100) # generates 100 evenly spaced numbers between 0 and 10
y1 = 3*np.sin(x1) # calculates the sine of each element in x
plt.plot(x1, y1) # plots the sine function
dydx = np.gradient(y1, x1) # calculates the numerical derivative of y with respect to x
plt.plot(x1, dydx) # plots the derivative of the sine function
a3 = np.cumsum(np.array([1, 2, 3, 4, 5])) # calculates the cumulative sum of the array
print (a3[-1]) # prints the cumulative sum of the array
y1_int  = np.cumsum(y1) * (x1[1] - x1[0]) # calculates the numerical integral of y with respect to x using the cumulative sum and the spacing, where x[1] - x[0] is the spacing between x values or change in x "dx"
plt.plot(x1, y1_int) # plots the integral of the sine function

# Example 1:
x = np.linspace(0, 10, 10000) # generates 10000 evenly spaced numbers between 0 and 10
y = np.exp(-x/10) * np.sin(x) # calculates the function e^(-x/10) * sin(x)
plt.plot(x, y) # plots the function
plt.show() # displays the plot
alpha = np.mean(y[(x>=4) & (x<=7)]) # calculates the mean of the array, & acts as a logical AND operator, so this calculates the mean of the elements in y where the corresponding elements in x are between 4 and 7
beta = np.std(y[(x>=4) & (x<=7)]) # calculates the standard deviation of the array, & acts as a logical AND operator, so this calculates the standard deviation of the elements in y where the corresponding elements in x are between 4 and 7
gamma = (np.percentile(y[(x>=4) & (x<=7)], 80)) # calculates the 80th percentile of the array, & acts as a logical AND operator, so this calculates the 80th percentile of the elements in y where the corresponding elements in x are between 4 and 7
print (alpha)
print (beta)
print (gamma)
dydx = np.gradient (y, x) # calculates the numerical derivative of y with respect to x
plt.plot(x, dydx) # plots the derivative of the function
zero_cross_indices = np.where(dydx[:-1] * dydx[1:] <= 0)[0] # finds the indices where the derivative changes sign, indicating a zero crossing
x_zeros = x[zero_cross_indices] # gets the x values corresponding to the zero crossings
print (x_zeros) # prints the x values where the derivative changes sign

# Example 2:
sigma = np.cumsum(np.array([i for i in range(10001) if i % 4 != 0 and i % 7 != 0])) # calculates the cumulative sum of the array from 0 to 10000, excluding numbers that are divisible by 4 or 7
print(sigma[-1]) # prints the cumulative sum of the array

# Example 3:
theta = np.linspace(0, 2*np.pi, 10000) # generates 10000 evenly spaced numbers between 0 and 2*pi
r = 1 + 3/4 * np.sin(3*theta) # calculates the function 1 + 3/4 * sin(3*theta)
x = r * np.cos(theta) # calculates the x-coordinates of the polar function
y = r * np.sin(theta) # calculates the y-coordinates of the polar function
plt.plot(x, y) # plots the polar function
plt.show() # displays the plot
A_int = np.cumsum(1/2 * r**2) * (theta[1] - theta[0]) # calculates the numerical integral of the area under the polar curve using the cumulative sum and the spacing, where theta[1] - theta[0] is the spacing between theta values or change in theta "dtheta"
print(A_int[-1]) # prints the area under the polar curve
L_int = np.cumsum(np.sqrt(r**2 + (np.gradient(r,theta))**2)) * (theta[1] - theta[0]) # calculates the numerical integral of the length of the polar curve using the cumulative sum and the spacing, where theta[1] - theta[0] is the spacing between theta values or change in theta "dtheta"
print(L_int[-1]) # prints the length of the polar curve

# Example 4: Black body radiation
kt = np.linspace(0, 3, 100) # generates 100 evenly spaced numbers between 0 and 3
P_normalised = (1/(1 + np.exp(-kt)))**4 # calculates the function 1/(1 + e^(-kt)), this P_normalised = P/A * sigma * epsilon * To **4, where epsilon is the emissivity, sigma is the Stefan-Boltzmann constant, To is the temperature of the object, and P/A is the power per unit area, where P_prime and kt is dimesionless
plt.plot (kt, P_normalised) # plots the function
E = np.cumsum(P_normalised) * (kt[1] - kt[0]) # calculates the numerical integral of the energy using the cumulative sum and the spacing, where kt[1] - kt[0] is the spacing between kt values or change in kt "dkt"
plt.plot(kt, E) # plots the energy
plt.xlabel('$kt$', fontsize=12) # labels the x-axis
plt.ylabel(r'$\left( \frac{k}{A \sigma \epsilon T_0^4} \right) E(t)$', fontsize=12) # labels the y-axis
plt.show() # displays the plot