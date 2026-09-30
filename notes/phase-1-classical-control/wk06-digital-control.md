# Week 6: Digital control & implementation

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Discretise a continuous controller and compare the methods
- [ ] Pick a control loop rate for a given closed-loop bandwidth
- [ ] Implement a fixed-rate control loop on Arduino/ESP32

## Key concepts
- Sampling, aliasing, zero-order hold
- z-transform and discrete-time stability (unit circle)
- Discretisation: forward/backward Euler, Tustin, ZOH
- Choosing a sample rate relative to bandwidth
- Quantisation, computational delay, fixed timing loops

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why does ZOH add roughly half a sample of delay?
   - *My answer:*
2. Map s-plane pole p to the z-plane. Where does the imaginary axis go?
   - *My answer:*

## Hands-on
Use control.c2d to discretise your PID with Tustin at 20x and 5x the bandwidth, and compare the step responses.

Code and results: [`exercises/wk06-digital-control`](../../exercises/wk06-digital-control/)

## Resources
- Franklin, Powell & Workman, *Digital Control of Dynamic Systems*
- python-control docs: c2d / sample_system

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
