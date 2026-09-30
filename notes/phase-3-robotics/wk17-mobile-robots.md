# Week 17: Mobile robot kinematics & control

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Simulate a diff-drive robot and implement pure pursuit
- [ ] Quantify odometry drift and correct it with an EKF

## Key concepts
- Unicycle and differential-drive kinematics; nonholonomic constraints
- Wheel odometry and its error growth
- Go-to-goal, path following, pure pursuit, Stanley controller
- Localisation with EKF (odometry + IMU / landmarks)

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why can't a diff-drive robot move sideways, and why does that make control harder?
   - *My answer:*
2. How does the lookahead distance in pure pursuit affect tracking?
   - *My answer:*

## Hands-on
Write a Python simulation of a diff-drive robot following a figure-8 with pure pursuit; plot the cross-track error for three lookahead distances.

Code and results: [`exercises/wk17-mobile-robots`](../../exercises/wk17-mobile-robots/)

## Resources
- Siegwart, Nourbakhsh & Scaramuzza, *Introduction to Autonomous Mobile Robots*
- Corke, *Robotics, Vision and Control* - mobile robot chapters

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
