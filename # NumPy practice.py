# NumPy practice
import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
print(a1[1:3])  # This will print elements at index 1 and 2 (values 2 and 3)
print(a1[2:4])  # This will print elements at index 2 and 3 (values 3 and 4)
print(a1[1:-1])  #  This will print elements at index 2, 3, and 4 (values 3, 4, and 5)
print(a1>2)  # This will print a boolean array indicating which elements are greater than 2
print(a1[a1>2])  # This will print elements that are greater than 2 (values 3, 4, and 5)
names = np.array(['John', 'Jane', 'Hayden', 'Alice', 'Bob'])
print(names)
first_letter_j = np.vectorize(lambda x: x[0])(names)=='J'  # This will create a vectorized function to check if the first letter is 'J'
f = lambda x: x[0]
print(first_letter_j)
print(names[first_letter_j])  # This will print names that start with 'J' (John and Jane)
print(a1%4) # This will print the remainder of each element in a1 when divided by 4
print(a1%4 ==0) # This will print a boolean array indicating which elements in a1 are divisible by 4
print(a1[a1%4 ==0])  # This will print elements in a1 that are divisible by 4 (value 4)