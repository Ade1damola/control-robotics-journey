# Week 16: Manipulator control

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Compare joint PD, PD + gravity compensation and computed torque on a 2-link arm
- [ ] Generate smooth joint trajectories and track them
- [ ] Explain when impedance control is preferred (contact tasks)

## Key concepts
- Independent joint PD/PID control
- PD + gravity compensation (with Lyapunov stability proof)
- Computed torque / inverse dynamics control
- Trajectory generation (cubic/quintic polynomials)
- Impedance and admittance control; operational-space control

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why does computed torque control degrade with model error?
   - *My answer:*
2. What does an impedance controller make the robot 'feel like'?
   - *My answer:*

## Hands-on
Implement computed-torque tracking of a quintic trajectory for your 2-link arm, then add 20% mass error and measure the tracking degradation.

Code and results: [`exercises/wk16-manipulator-control`](../../exercises/wk16-manipulator-control/)

## Resources
- Lynch & Park - Ch. 9 & 11
- Siciliano et al., *Robotics: Modelling, Planning and Control* - Ch. 8-9

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
