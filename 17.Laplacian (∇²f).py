#17.Laplacian (∇²f)
#The Laplacian is defined as ∇²f = ∇·(∇f)
# Or ∂²f/∂x² + ∂²f/∂y² + ∂²f/∂z²
import numpy as np 
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 2])
z = np.array([0, 1, 2])
P = np.array([
    [[101, 103, 106, 110],
     [102, 105, 109, 114],
     [104, 108, 113, 119]],

    [[103, 105, 109, 114],
     [104, 108, 113, 119],
     [106, 111, 117, 124]],

    [[106, 109, 114, 120],
     [107, 112, 118, 125],
     [109, 115, 122, 130]]
])
dP_dz, dP_dy, dP_dx = np.gradient(P, z, y, x)
d2P_dz2 = np.gradient(dP_dz, z, axis=0)
d2P_dy2 = np.gradient(dP_dy, y, axis=1)
d2P_dx2 = np.gradient(dP_dx, x, axis=2)
laplacian = d2P_dx2 + d2P_dy2 + d2P_dz2
print(laplacian)
print(laplacian[1,1,1]) #Laplacian at (1,1,1)
