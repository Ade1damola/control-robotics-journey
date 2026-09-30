# Week 5: PID control in practice

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Tune a PID for a DC motor to a spec and justify every gain
- [ ] Implement anti-windup and show the difference under saturation
- [ ] Write a discrete PID loop that runs on a microcontroller

## Key concepts
- P, I and D action and their frequency-domain meaning
- Tuning: Ziegler-Nichols, pole placement, loop shaping
- Derivative filtering and derivative-on-measurement
- Integrator windup and anti-windup (clamping, back-calculation)
- Feedforward + feedback, cascade control

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why is a pure derivative term never implemented as-is?
   - *My answer:*
2. Describe a scenario where integral windup causes a large overshoot.
   - *My answer:*
3. When would you use cascade control on a robot joint?
   - *My answer:*

## Hands-on
Write a discrete PID class in Python with a derivative filter and back-calculation anti-windup; test it on a saturated DC motor simulation.

Code and results: [`exercises/wk05-pid`](../../exercises/wk05-pid/)

## Resources
- Astrom & Murray - Ch. 10
- Brett Beauregard, 'Improving the Beginner's PID' blog series

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
