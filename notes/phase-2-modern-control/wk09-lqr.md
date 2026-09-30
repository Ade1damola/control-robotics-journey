# Week 9: Optimal control - LQR

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Tune Q/R for the cart-pole and explain the resulting behaviour
- [ ] Compare LQR to pole placement for the same system
- [ ] Test the linear controller on the nonlinear model and find where it fails

## Key concepts
- Quadratic cost with Q and R and what they trade off
- The algebraic Riccati equation
- LQR robustness guarantees (60 deg phase margin, infinite gain margin)
- Bryson's rule for choosing Q and R
- Finite-horizon LQR, LQR for tracking

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. What happens to the gains as R -> 0? As R -> infinity?
   - *My answer:*
2. Why is LQR the default starting point for balancing robots?
   - *My answer:*

## Hands-on
In the Control Lab LQR tab, find the largest initial angle the controller recovers from with a +-10 N force limit. Explain the failure mode.

Code and results: [`exercises/wk09-lqr`](../../exercises/wk09-lqr/)

## Resources
- Steve Brunton, 'Control Bootcamp' (YouTube) - LQR lectures
- Tedrake, *Underactuated Robotics* (free: underactuated.csail.mit.edu) - LQR chapter

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
