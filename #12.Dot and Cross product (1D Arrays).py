#12. Dot and Cross product (1D Arrays)
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
#To take the dot product
# Method 1: Using np.dot()
result1 = np.dot(a, b)
# Method 2: Using the @ operator (cleaner and preferred)
result2 = a @ b
print(result1)  # Output: 32  --> (1*4 + 2*5 + 3*6)
#To take the cross product
# Define two 3D vectors
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
# Compute cross product
result = np.cross(u, v)
print(result)
