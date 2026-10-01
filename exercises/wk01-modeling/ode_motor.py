# A short Python script that defines the RHS of the ODEs of the DC motor system as a function for solve_ivp

import control
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# Define the physical parameters
J = 0.01 # kg·m²
b = 0.1 # N·m·s/rad 
k = 0.01 # V·s/rad
R = 1 # Ω
L = 0.5 # H

# Building the Transfer Function
num = [k]
den = [J*L, J*R + L*b, R*b + k**2, 0]
G = control.TransferFunction(num, den)

# Analytical Step Response of the Transfer Function
t_axis = np.linspace(0, 10, 500)
t_tf, y_tf = control.step_response(G, t_axis) # this is solving the tf analytically

# ODE Block (state variables)
def dc_motor(t, z):
    [theta, thetadot, i] = z
    
    V = V0
    thetaddot = (k*i - b*thetadot) / J
    idot = (V - R*i - k*thetadot) / L
    return [thetadot, thetaddot, idot]

z0 = [0.0, 0.0, 0.0] # initial condition at rest

t_span = (0, 10) # time span
t_eval = np.linspace(t_span[0], t_span[1], 500)

sol = solve_ivp(dc_motor, t_span, z0, t_eval=t_eval, method='RK45')

t_ode = sol.t
theta_ode = sol.y[0]
thetadot_ode = sol.y[1]
i_ode = sol.y[2]

# Plot the block
plt.figure(figsize=(8,4))
plt.plot(t_tf, y_tf, 'b', label='Transfer Function step')
plt.plot(t_ode, theta_ode, 'r--', label='Numerical ODE step')
plt.title('DC Motor Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Angular Position θ(t) (rad)')
plt.grid(True)
plt.legend()
plt.show()