#21.Generalized Laplacian in n Dimensions 
#If you remember the laplacian from lesson 17 we have the identities 
#∇²f = ∇·(∇f) (1)
#∇²f = tr(Hբ) [Thats an f unicode is just weird at times] (2)
#Where tr is the trace of the matrix 
#Making a function with method one using the Gradient function from lesson 20 and the divergence function from Lesson 18
import numpy as np 
def gradient(f, coordinates):
    derivatives = np.gradient(f, *coordinates)
    return np.array(derivatives)
def divergence(components, coordinates):
    n = len(components)
    div = np.zeros_like(components[0], dtype=float)
    for i in range(n):
        derivatives = np.gradient(
            components[i],
            *coordinates
        )
        div += derivatives[i]
    return div
def laplacian_div(f,coordinates):
    grad_f = gradient(f,coordinates)
    L_div = divergence(grad_f,coordinates)
    return L_div 
#Method 2 using the Hessian from lesson 20
def jacobian(components, coordinates):
    n = len(components)
    jacobian_matrix = []
    for i in range(n):
        derivatives = np.gradient(
            components[i],
            *coordinates
        )
        jacobian_matrix.append(derivatives)
    return np.array(jacobian_matrix)
def hessian(f, coordinates):
    grad_f = gradient(f, coordinates)
    H = jacobian(grad_f, coordinates)
    return H
def laplacian_hes(f, coordinates):
    hes_f = hessian(f,coordinates)
    trace = np.trace(hes_f)
    return trace
#These methods are not optimized and rely on multiple functions to compute taking up RAM space so we use a more direct approach  
def laplacian_direct(f, coordinates):
    laplacian = np.zeros_like(f, dtype=float)
    for i in range(f.ndim):
        df_dxi = np.gradient(f, coordinates[i], axis=i)
        d2f_dxi2 = np.gradient(df_dxi, coordinates[i], axis=i)
        laplacian += d2f_dxi2
    return laplacian
#e.g 
x = np.linspace(-4, 4, 9)
y = np.linspace(-4, 4, 9)
z = np.linspace(-4, 4, 9)
X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
f1 = X**2 - 4*Y**3 + np.cos(Z)
L = laplacian_direct(f1, [x,y,z])
L1 = laplacian_div(f1, [x,y,z])
L2 = laplacian_hes(f1, [x,y,z])
print(L[2,2,2])
print(L1[2,2,2])
print(L2[2,2,2])
#Note that the 2 methods I had taught first aren't useless but act intuition for you
