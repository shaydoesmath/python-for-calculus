#20.Generalized Gradient and Hessian
#First we generalize the gradient from lesson 14
import numpy as np
def gradient(f, coordinates):
    derivatives = np.gradient(f, *coordinates)
    return np.array(derivatives)
#Lets go through an example 
x = np.linspace(-3, 3, 5)
y = np.linspace(-3, 3, 5)
z = np.linspace(-3, 3, 5)
X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
f = X**2 + Y**2 + Z**2
grad_f = gradient(f, [x, y, z])
print(grad_f.shape)
print(grad_f[:, 2, 2, 2])
#Question: Use the function above, then test it with:
#f(x,y,z)=x^2+3y^2+4z^2
x = np.linspace(-3, 3, 5)
y = np.linspace(-3, 3, 5)
z = np.linspace(-3, 3, 5)
X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
f1 = X**2+3*Y**2+4*Z**2
grad_f1 = gradient(f1, [x,y,z])
print(grad_f1.shape)
print(grad_f1[:, 1, 1, 1])
#To build the Hessian function
#H_f = J_{\nabla{f}}
#So we need the jacobian remebering our def
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
#Then our Hessian is 
def hessian(f, coordinates):
    grad_f = gradient(f, coordinates)
    H = jacobian(grad_f, coordinates)
    return H
#e.g 
Hessian = hessian(f1, [x,y,z])
print(Hessian[:, :, 2, 2, 2])
#Another e.g
f2 = X**2 + 3*Y**2 + 4*Z**2 + 5*X*Y + 2*Y*Z
Hessian2 = hessian(f2, [x,y,z])
print(Hessian2[:, :, 2, 2, 2])
