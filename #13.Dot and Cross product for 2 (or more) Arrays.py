# #13. True Dot Products for 2D Arrays (Batches of Vectors)
import numpy as np 

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Method 1: The Total Dot Product (Flattens the arrays) 
# np.vdot flattens 2D arrays into a 1D vector and finds the overall scalar dot product.
total_dot = np.vdot(A, B)

print("Total Dot Product (Flattened):", total_dot)
# Calculation: (1*5) + (2*6) + (3*7) + (4*8) = 5 + 12 + 21 + 32
# Output: 70


# Method 2: Row-by-Row Dot Products (Batch Processing) 
# Often, a 2D array represents a list of separate vectors. 
# To get the dot product of Row A[0] • B[0] and Row A[1] • B[1]:
row_dots = np.sum(A * B, axis=1)

print("Row-wise Dot Products:", row_dots)
# Row 1: (1*5) + (2*6) = 17
# Row 2: (3*7) + (4*8) = 53
# Output: [17 53]


# Method 3: (Using Einstein Summation) ---
# np.einsum is highly optimized. 'ij,ij->i' means: take 2D arrays (i=rows, j=cols),
# multiply corresponding elements, and sum over the columns (j), leaving a 1D array of rows (i).
einsum_dots = np.einsum('ij,ij->i', A, B)

print("Row-wise Dot Products (einsum):", einsum_dots)
# Output: [17 53]

C = np.array([[1, 2, 3], 
              [4, 5, 6]])

# Another batch of two vectors
D = np.array([[7, 8, 9], 
              [1, 0, 2]])
#For cross product
result1 = np.cross(C, D)
#If your vectors are structured as columns instead of rows, 
#you can use the axis parameter to tell NumPy where the 3-element vector coordinates reside.
#if your arrays are shaped as (3, n), the calculation will fail unless you explicitly designate axis=0
# Vectors stored as columns (shape 3x2)
X = np.array([[1, 4],
              [2, 5],
              [3, 6]])
Y = np.array([[7, 1],
              [8, 0],
              [9, 2]])
# Compute along the rows (axis 0)
result2 = np.cross(X, Y, axis=0)
print(result1)
print(result2)
# Output matches the batch example, but formatted as columns
