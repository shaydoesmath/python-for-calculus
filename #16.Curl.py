#16.Curl in 3D Arrays
#The normal curl formula is too long too write you should know this by now
import numpy as np 
x = np.array([0, 1, 2])
y = np.array([0, 1, 2])
z = np.array([0, 1, 2])
Fx = np.array([
    [[1, 2, 3], [2, 3, 4], [3, 4, 5]],
    [[2, 3, 4], [3, 4, 5], [4, 5, 6]],
    [[3, 4, 5], [4, 5, 6], [5, 6, 7]]
])
Fy = np.array([
    [[0, 1, 2], [1, 2, 3], [2, 3, 4]],
    [[1, 2, 3], [2, 3, 4], [3, 4, 5]],
    [[2, 3, 4], [3, 4, 5], [4, 5, 6]]
])
Fz = np.array([
    [[2, 2, 2], [3, 3, 3], [4, 4, 4]],
    [[3, 3, 3], [4, 4, 4], [5, 5, 5]],
    [[4, 4, 4], [5, 5, 5], [6, 6, 6]]
])
dFz_dz, dFz_dy, dFz_dx = np.gradient(Fz, z, y, x)
dFy_dz, dFy_dy, dFy_dx = np.gradient(Fy, z, y, x)
dFx_dz, dFx_dy, dFx_dx = np.gradient(Fx, z, y, x)
curl_x = dFz_dy - dFy_dz
curl_y = dFx_dz - dFz_dx
curl_z = dFy_dx - dFx_dy
curl_F = np.array([curl_x, curl_y, curl_z])
#Notice the ordering,NumPy returns derivatives in array-axis order: (z,y,x), not (x,y,z).
print(curl_F)
print(curl_F[:,1,1,1]) #Curl at (1,1,1)