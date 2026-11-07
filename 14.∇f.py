#14.∇f 
#We code ∇f as the array of all the partials  
import numpy as np
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 2])
f = np.array([
    [12, 14, 17, 19],
    [13, 16, 18, 22],
    [15, 17, 21, 25]
])
df_dy, df_dx = np.gradient(f, y, x)
grad_f = np.array([df_dx, df_dy])
print(grad_f)
#Small problem: From below find  dC/dx,dC/dy,∇C and |∇C|, find ĝ for x & y = 2
x1 = np.array([0, 2, 4, 6])
y1 = np.array([0, 2, 4])

C = np.array([
    [10, 13, 17, 22],
    [12, 16, 21, 27],
    [15, 19, 25, 32]
])
dCdy,dCdx = np.gradient(C,y1,x1) #dC/dx,dC/dy
grad_C = np.array([dCdx,dCdy]) #∇C
mag_C = np.hypot(dCdx,dCdy) #np.hypot = sqrt(a^2+b^2)
norm_g = grad_C / mag_C #ĝ
unit_x = norm_g[0]
unit_y = norm_g[1]
print(dCdx,dCdy)
print(grad_C)
print(mag_C)
print(unit_x,unit_y)
print(unit_x[1, 1])
print(unit_y[1, 1])
