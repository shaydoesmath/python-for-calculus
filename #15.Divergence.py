#15. Divergence
#For a 2D Vector field the divergence is ∂u/∂x + ∂v/∂y
import numpy as np 
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 2])
u = np.array([
    [2.0, 2.4, 2.8, 3.1],
    [2.1, 2.5, 2.9, 3.3],
    [2.2, 2.6, 3.0, 3.5]
    ])
v = np.array([
    [1.0, 1.1, 1.2, 1.3],
    [1.4, 1.5, 1.6, 1.7],
    [1.8, 1.9, 2.0, 2.1]
])
dudy, dudx = np.gradient(u, y, x)
dvdy, dvdx = np.gradient(v, y, x)
div_F = dudx + dvdy 
print(div_F)
print(div_F[1,2])

