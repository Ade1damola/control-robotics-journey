# Week 3: Stability & root locus

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Determine the stable gain range of a closed loop with Routh-Hurwitz
- [ ] Sketch a root locus by hand and verify it in Python
- [ ] Place a lead compensator to pull the locus into a desired region

## Key concepts
- BIBO stability and pole locations
- Routh-Hurwitz criterion
- Root locus construction rules
- Designing lead/lag compensators with root locus

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why do root locus branches start at open-loop poles and end at zeros?
   - *My answer:*
2. What does adding a pole at the origin (integrator) do to the locus?
   - *My answer:*

## Hands-on
In the Control Lab root-locus view, find the gain at which a P-controlled DC motor position loop becomes oscillatory, and confirm it with Routh-Hurwitz by hand.

Code and results: [`exercises/wk03-stability-rootlocus`](../../exercises/wk03-stability-rootlocus/)

## Resources
- Nise - Ch. 6, 8, 9
- Franklin, Powell & Emami-Naeini, *Feedback Control of Dynamic Systems* - Ch. 5

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
