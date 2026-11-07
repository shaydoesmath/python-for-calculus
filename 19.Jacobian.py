#19.Jacobian
#Suppose we have F(x, y) = [ F₁(x, y) , F₂(x, y) ]ᵀ
#Then 𝑱_𝐅 = [ ∂𝐹₁/∂𝓍   ∂𝐹₁/∂𝓎 ; ∂𝐹₂/∂𝓍   ∂𝐹₂/∂𝓎 ]
#Lets go through an example 
import numpy as np
x = np.linspace(-3, 3, 5)
y = np.linspace(-3, 3, 5)
X, Y = np.meshgrid(x, y, indexing="xy")
F1 = X**2 + Y
F2 = X*Y + Y**2
# Derivatives of F1
dF1_dy, dF1_dx = np.gradient(F1, y, x)
# Derivatives of F2
dF2_dy, dF2_dx = np.gradient(F2, y, x)
# Construct Jacobian
J = np.array([
    [dF1_dx, dF1_dy],
    [dF2_dx, dF2_dy]
])
print(J.shape)
print(J[:, :, 2, 2])
#Lets now construct a function that allows us to do this in multiple dimensions
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
#Test 2D
J1 = jacobian([F1, F2], [x, y])
print(J1.shape)
print(J1[:, :, 2, 2])
#Now test 3D
x = np.linspace(-3, 3, 5)
y = np.linspace(-3, 3, 5)
z = np.linspace(-3, 3, 5)
X, Y, Z = np.meshgrid(x, y, z,indexing="ij")
F1 = X**2 + Y - Z
F2 = X*Y + Y**2 
F3 = Z**4 - np.sin(X) - Y
J2 = jacobian([F1,F2,F3],[x,y,z])
print(J2.shape)
print(J2[:, :, 2, 2, 2])
