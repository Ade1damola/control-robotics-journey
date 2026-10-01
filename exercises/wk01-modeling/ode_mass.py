# A short Python script that defines the RHS of the ODEs as a function for solve_ivp

import control
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# Define the physical parameters
m = 1.0  # mass (kg)
b = 0.5 # damping coefficient ( N.s/m)
k = 2.0 # stiffness coefficient (N/m)
F0 = 1.0 # applied force (N)

# Building the Transfer Function
num = [1.0]
den = [m, b, k]
G = control.TransferFunction(num, den)

# Analytical Step Response of the Transfer Function
t_axis = np.linspace(0, 10, 500)
t_tf, y_tf = control.step_response(G, t_axis) # this is solving the tf analytically

# ODE Block (state variables)
def mass_spring_damper(t, z):
    [x, xdot] = z
    
    F = F0
    xddot = (F - b*xdot - k*x) / m
    return [xdot, xddot]


z0 = [0.0, 0.0] # initial condition at rest

t_span = (0, 10) # time span
t_eval = np.linspace(t_span[0], t_span[1], 500)

sol = solve_ivp(mass_spring_damper, t_span, z0, t_eval=t_eval, method='RK45')

t_ode = sol.t
x_ode = sol.y[0]


# Plot the block
plt.figure(figsize=(8,4))
plt.plot(t_tf, y_tf, 'b', label='Transfer Function step')
plt.plot(t_ode, x_ode, 'r--', label='Numerical ODE step')
plt.title('Mass–Spring–Damper Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Displacement x(t) (m)')
plt.grid(True)
plt.legend()
plt.show()