#22. Forward Euler 
#We now begin solving ODEs 
# we use the most basic one i.e y_{n+1}=y_n+hf(t_n,y_n)
#This is called Forward Euler or RK1 (we will learn this later)
import numpy as np
import matplotlib.pyplot as plt
t_data = np.array([0, 1, 2, 3, 4, 5], dtype=float)
N_data = np.array([1000, 819, 670, 549, 449, 368], dtype=float)
k = 0.2
h = 0.1
t = np.arange(0, 5 + h, h)
N = np.zeros(len(t))
N[0] = 1000
#Our Ode will be dN/dt = -kN 
for i in range(len(t) - 1 ):
    N[i+1] = N[i]-h*k*N[i]
print(N[-1])    
#Derivation if you did not understand the math (Paste into a tex viewer)
#d_tN=-kN\\
#\frac{N(t+\Delta t)-N(t)}{\Delta t} \approx -kN(t)\\
#N_{i+1}-N_i =-k\Delta t N_i\\
#N_{i+1}=N_i-k\Delta t N_i
#Or using the more general forward difference
for i in range(len(t) - 1):
    dN_dt = -k * N[i]
    N[i+1] = N[i] + h*dN_dt
#and to plot the data 
# Plotting the results
plt.figure(figsize=(8, 5))
# Plot the continuous numerical approximation as a line
plt.plot(t, N, label='Forward Euler (h = 0.1)', color='blue', linewidth=2)
# Plot the discrete supplied data as scatter points
plt.scatter(t_data, N_data, label='Supplied Data', color='red', zorder=5)
# Formatting the plot
plt.title('Radioactive Decay: Numerical Solution vs. Supplied Data')
plt.xlabel('Time (t)')
plt.ylabel('Quantity (N)')
plt.legend()
plt.grid(True)
plt.show()
