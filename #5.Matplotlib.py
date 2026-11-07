#5. Matplotlib
#Numerical output is much easier to understand when we can plot it.
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 101)
y = x**2
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x squared")
plt.grid()
plt.show()
#plt.plot(x, y) — plots the data.
#plt.xlabel(...) and plt.ylabel(...) — label the axes.
#plt.grid() — displays a grid.
#plt.show() — displays the figure.