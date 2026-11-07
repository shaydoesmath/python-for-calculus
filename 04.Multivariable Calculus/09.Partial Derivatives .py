#9. Partial Derivatives 
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 101)
y = np.linspace(-5, 5, 101)
X, Y = np.meshgrid(x, y)
Z = X**2 + 3*X*Y + 2*Y**2
dZ_dy, dZ_dx = np.gradient(Z, y, x)
#Important: np.gradient() returns derivatives in the order of the array's axes 
#Axis 0 corresponds to (y).
#Axis 1 corresponds to (x).
print(dZ_dy, dZ_dx)
