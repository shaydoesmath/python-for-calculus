#10. Second partial derivatives and Mixed partial derivatives
import numpy as np 
x = np.linspace(-5,5,101)
y = np.linspace(-5,5,101)
X, Y = np.meshgrid(x, y)
T = 100 - 2*X**2 -Y**2
dT_dy, dT_dx = np.gradient(T, y, x, edge_order=2)
d2T_dx2 = np.gradient(dT_dx, x, axis=1, edge_order=2) #\partial_{x}^{2}f
d2T_dy2 = np.gradient(dT_dy, y, axis=0, edge_order=2) #\partial_{y}^{2}f
d2T_dxdy = np.gradient(dT_dx, y, axis=0, edge_order=2) #\partial_{y}\partial_{x}f

