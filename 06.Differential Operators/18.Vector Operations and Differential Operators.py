#18.Vector Operations and Differential Operators
#If we have 2 vectors A=a1,a2,a3,... & B=b1,b2,b3,...
#Then A·B = \sum_{i=1}^{n} a_i b_i 
#In numpy this is 
import numpy as np 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a, b))
#For einsum:
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [7, 8, 9],
    [1, 2, 3]
])
dots = np.einsum('...i,...i->...', A, B)
#... represents any number of batch dimensions.
#i represents the vector-component dimension.
#Repeated i means multiply corresponding components and sum over them.
# #->... means retain the batch dimensions in the output.
dots1 = np.sum(A * B, axis=-1) #Also works
#np.vdot(A,B)	Flattens everything into one scalar
#np.dot(A,B)	Performs dot/matrix multiplication; behavior depends on dimensions
#np.sum(A*B, axis=-1)	Dot product along the final axis
#np.einsum('...i,...i->...',A,B)	Generalized batched dot product (Useful for tensors)

#Now for Cross product review: 
result = np.cross(A, B, axis=-1) #Gets very complicated generalizing past 3D so we remain with this 

#Generalizing divergence to n dimensions 
#∇·f = ∑ᵢ₌₁ⁿ ∂Fᵢ / ∂xᵢ (We use a function to write this)
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
#e.g 
x = np.array([0, 1, 2])
y = np.array([0, 1, 2])
z = np.array([0, 1, 2])
w = np.array([0, 1, 2])
W, Z, Y, X = np.meshgrid(w, z, y, x, indexing='ij')

# Four vector components
F1 = X + 2*Y
F2 = Y + 3*Z
F3 = Z + 4*W
F4 = W + 5*X

eg = divergence(
    [F1, F2, F3, F4],
    [x, y, z, w]
)

print(eg)
print(eg.shape)
print(eg[1,1,1,1])
