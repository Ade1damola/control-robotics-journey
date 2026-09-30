# Week 1: Modelling dynamic systems

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Derive the transfer function of a mass-spring-damper and a DC motor from first principles
- [ ] Linearise a nonlinear pendulum about upright and hanging equilibria
- [ ] Reduce a block diagram with feedback loops to a single transfer function

## Key concepts
- ODE models of mechanical, electrical and electromechanical systems
- Laplace transform and transfer functions
- Block diagram algebra
- DC motor model (electrical + mechanical coupling)
- Linearisation about an equilibrium (Jacobians)

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why does a DC motor speed model become second order when inductance is included?
   - *My answer:*
2. What does linearisation assume, and when does it break down?
   - *My answer:*
3. What is the physical meaning of a pole of a transfer function?
   - *My answer:*

## Hands-on
Write a Python function that builds the DC motor speed transfer function from (J, b, K, R, L) with python-control, and compare its step response to a numerical ODE simulation with scipy.integrate.solve_ivp.

Code and results: [`exercises/wk01-modeling`](../../exercises/wk01-modeling/)

## Resources
- Astrom & Murray, *Feedback Systems* (free: fbswiki.org) - Ch. 2-3
- Control Tutorials for MATLAB & Simulink (ctms.engin.umich.edu) - Modeling sections
- Nise, *Control Systems Engineering* - Ch. 2

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
