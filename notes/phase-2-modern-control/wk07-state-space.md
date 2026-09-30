# Week 7: State-space representation

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Write a cart-pole and a DC motor in state-space form
- [ ] Relate eigenvalues of A to poles and to the modal response
- [ ] Convert between TF and SS and explain why the SS form is not unique

## Key concepts
- State, input and output equations (A, B, C, D)
- Solution via the matrix exponential
- Eigenvalues/eigenvectors and modes
- Transfer function <-> state space, canonical forms
- Similarity transforms

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why do robotics people prefer state space over transfer functions?
   - *My answer:*
2. What does a complex eigenvalue pair of A look like in the time response?
   - *My answer:*

## Hands-on
Derive the linearised cart-pole A and B matrices by hand, then check them against a numerical Jacobian of the nonlinear model.

Code and results: [`exercises/wk07-state-space`](../../exercises/wk07-state-space/)

## Resources
- Astrom & Murray - Ch. 5-6
- Steve Brunton, 'Control Bootcamp' (YouTube) - first lectures

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
