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
x = np.linspace(0, 10, 10000) # generates 100 evenly spaced numbers between 0 and 10
y = np.exp(-x/10) * np.sin(x) # calculates the function e^(-x/10) * sin(x)
plt.plot(x, y) # plots the function
plt.show() # displays the plot
mean y = np.mean(y[(x>=4) & (x<=7)]) # calculates the mean of the array, & acts as a logical AND operator, so this calculates the mean of the elements in y where the corresponding elements in x are between 4 and 7
std y = np.std(y[(x>=4) & (x<=7)]) # calculates the standard deviation of the array, & acts as a logical AND operator, so this calculates the standard deviation of the elements in y where the corresponding elements in x are between 4 and 7
