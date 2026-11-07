#4. NumPy 
import numpy as np
x = np.array([0, 1, 2, 3, 4])
y = x**2
print(y)
#np.linspace(start, stop, number_of_points) creates evenly spaced points, including both endpoints.
x = np.linspace(0, 10, 101)
print(x[0])    # 0.0
print(x[-1])   # 10.0
print(len(x))  # 101
#Here, we're creating 101 points between 0 and 10. The spacing between adjacent points is
#\Delta x=\frac{10-0}{101-1}=0.1
#Or d=\frac{stop-start}{num-1}
