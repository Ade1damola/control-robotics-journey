# Week 21: Model Predictive Control

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Formulate and solve a linear MPC for a double integrator with input limits
- [ ] Implement nonlinear MPC for diff-drive trajectory tracking with CasADi
- [ ] Compare MPC and LQR under constraints

## Key concepts
- Receding-horizon optimal control
- Constraints on inputs and states
- Linear MPC as a QP; nonlinear MPC
- Tools: CasADi, do-mpc, acados, OSQP
- Stability ideas: terminal cost and terminal constraint

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why does MPC handle constraints naturally when LQR does not?
   - *My answer:*
2. What limits the MPC horizon in practice?
   - *My answer:*

## Hands-on
Write a linear MPC with CasADi for the cart-pole with a +-10 N force limit and compare it with a saturated LQR on the same initial condition.

Code and results: [`exercises/wk21-mpc`](../../exercises/wk21-mpc/)

## Resources
- Rawlings, Mayne & Diehl, *Model Predictive Control: Theory, Computation, and Design* (free PDF)
- CasADi docs (web.casadi.org)
- do-mpc docs (do-mpc.com)

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
