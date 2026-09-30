# Exercise - Week 1: Modelling dynamic systems

## Task
Write a Python function that builds the DC motor speed transfer function from (J, b, K, R, L) with python-control, and compare its step response to a numerical ODE simulation with scipy.integrate.solve_ivp.

## Approach
<!-- What you did and why -->
### Monday 
I reviewed the kinetic and potential energy of a mass-spring-damper system, as well a the electromechanical equations for a DC motor. Skecthed the clock diagrams for a mass-spring-damper system and a DC motor (electrial + mechanical), stating the state variables. 

### Tuesday
I derived the ODE equations for teh systems from first principles. Wrote a python script taht defines the RHS of the ODEs as a function for solve_ivp

## Results
<!-- Plots (save PNGs in this folder and embed them: ![step response](step_response.png)) and key numbers -->

### Mass-spring-damper system
![block diagram 1](mass-spring-damper-1.jpg)
![block diagram 2](mass-spring-damper-2.jpg)

### DC Motor 
![block diagram 3](dc-motor-1.jpg)
![block diagram 4](dc-motor-2.jpg)

## Takeaways
-
