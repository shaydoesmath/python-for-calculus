#6.Numerical integration (1D Array)
import numpy as np
x = np.array([0, 1, 2, 3])
f = np.array([2, 4, 5, 9])
result = np.trapezoid(f, x)
print(result)
#The syntax is:
#np.trapezoid(y, x)
# y: the measured values you're integrating.
# x: the coordinates where those measurements were taken.
# result: the approximate area under the curve.
