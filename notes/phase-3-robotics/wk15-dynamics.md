# Week 15: Robot dynamics

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Derive the equations of motion for a 2-link arm with the Lagrangian
- [ ] Simulate the arm and verify energy conservation without friction

## Key concepts
- Lagrangian mechanics
- Manipulator equation M(q)q'' + C(q,q')q' + g(q) = tau
- Properties: symmetry and positive-definiteness of M, skew-symmetry of M' - 2C
- Forward vs inverse dynamics

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Where does the Coriolis term come from physically?
   - *My answer:*
2. Why does M(q) depend on configuration?
   - *My answer:*

## Hands-on
Derive the 2-link arm dynamics with SymPy, simulate free motion and check that total energy stays constant.

Code and results: [`exercises/wk15-dynamics`](../../exercises/wk15-dynamics/)

## Resources
- Lynch & Park - Ch. 8
- Spong, Hutchinson & Vidyasagar, *Robot Modeling and Control* - Ch. 7

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
