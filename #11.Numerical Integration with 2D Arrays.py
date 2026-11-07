#11. Numerical Integration with 2D Arrays
#When your data lives on a grid, you can integrate along one axis at a time.
#np.trapezoid(data, x, axis=1)
#data - Your 2D measurements
#x - Coordinates along the integration direction
#axis=1 - Integrate across columns
#axis=0 - Integrate down rows
import numpy as np
# 1. Define 1D coordinate arrays (e.g., x from 0 to 2, y from 0 to 3)
x = np.linspace(0, 2, 100)
y = np.linspace(0, 3, 100)
# 2. Create the 2D grid 
# indexing='ij' forces x to align with axis 0 and y to align with axis 1
X, Y = np.meshgrid(x, y, indexing='ij')
# 3. Define your 2D function matrix: Z = f(X, Y)
# Example: f(x, y) = x^2 * y
Z = X**2 * Y
# 4. Integrate sequentially 
# Step A: Integrate Z along the rows (axis=0) using the x coordinates.
# This collapses the 2D array of shape (100, 100) into a 1D array of shape (100,).
integral_step1 = np.trapezoid(Z, x, axis=0)
# Step B: Integrate the resulting 1D array using the y coordinates.
# Since it is now a 1D array, you don't need to specify an axis.
final_result = np.trapezoid(integral_step1, y)
print(f"Final 2D Integral Result: {final_result:.4f}")
# Analytical solution for comparison: (2^3 / 3) * (3^2 / 2) = 12.0




