# Week 8: Controllability, observability, pole placement & observers

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Test controllability/observability and interpret a failure physically
- [ ] Design state feedback + observer for the cart-pole
- [ ] Add integral action for zero steady-state error

## Key concepts
- Controllability and observability matrices, rank tests
- State feedback u = -Kx and pole placement (Ackermann)
- Luenberger observer design; duality
- Separation principle
- Reference tracking with integral action

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Can you stabilise the cart-pole if you only measure the cart position? Why?
   - *My answer:*
2. Why should observer poles be faster than controller poles, and by how much?
   - *My answer:*

## Hands-on
Use control.place to stabilise the cart-pole, then design an observer that measures only x and theta; simulate with noisy measurements.

Code and results: [`exercises/wk08-pole-placement`](../../exercises/wk08-pole-placement/)

## Resources
- Astrom & Murray - Ch. 7-8
- Ogata, *Modern Control Engineering* - Ch. 10

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
