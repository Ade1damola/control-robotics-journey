# Week 20: Nonlinear control

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Prove stability of PD + gravity compensation with a Lyapunov function
- [ ] Design an energy-based swing-up and hand over to LQR for balancing

## Key concepts
- Phase portraits, equilibria and linearisation limits
- Lyapunov stability (direct method), LaSalle's invariance principle
- Feedback linearisation
- Sliding mode control basics
- Energy shaping (cart-pole swing-up)

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why is a Lyapunov function like an energy?
   - *My answer:*
2. What is chattering in sliding mode control and how is it mitigated?
   - *My answer:*

## Hands-on
Implement cart-pole energy swing-up plus LQR catch in simulation (the classic 'hybrid controller').

Code and results: [`exercises/wk20-nonlinear`](../../exercises/wk20-nonlinear/)

## Resources
- Slotine & Li, *Applied Nonlinear Control*
- Khalil, *Nonlinear Systems* (reference)
- Tedrake, *Underactuated Robotics*

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
