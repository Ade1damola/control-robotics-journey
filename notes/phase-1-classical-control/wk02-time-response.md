# Week 2: Time response & performance specs

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Map an overshoot and settling-time spec to a region of the s-plane
- [ ] Compute steady-state error for step/ramp inputs by system type
- [ ] Explain when the dominant-pole approximation is valid

## Key concepts
- First- and second-order responses
- Natural frequency, damping ratio and pole locations
- Rise time, overshoot, settling time, peak time
- Steady-state error, system type, final value theorem
- Effect of additional poles and zeros (dominant poles)

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. A spec says <10% overshoot and 2% settling time <2 s. Sketch the allowed pole region.
   - *My answer:*
2. Why does a right-half-plane zero cause an initial undershoot?
   - *My answer:*
3. What does integral action do to system type?
   - *My answer:*

## Hands-on
Use the Control Lab '2nd-order explorer' to verify the overshoot and settling-time formulas, then add a third pole and find when the 2nd-order approximation fails.

Code and results: [`exercises/wk02-time-response`](../../exercises/wk02-time-response/)

## Resources
- Nise - Ch. 4 & 7
- Brian Douglas / MATLAB Tech Talks - 'Control Systems Lectures' (YouTube)

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
