#8. NumPy's gradient() function
import numpy as np
#np.gradient(f, *varargs, axis=None, edge_order=1)
#f	- Your array of function values
#varargs - Spacing between points, or coordinate arrays
#axis - Which array axis to differentiate along
#edge_order - Accuracy of the one-sided boundary approximation
x = np.linspace(-3, 3, 100)
f = x**3 + 2*x**2 - 5*x
df = np.gradient(f, x)
df_exact = 3*x**2 + 4*x - 5
error = np.abs(df - df_exact)
print(df)
print(error)