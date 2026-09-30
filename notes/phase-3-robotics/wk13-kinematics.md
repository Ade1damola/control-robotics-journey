# Week 13: Robot kinematics

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Compute forward kinematics for a 3-DOF arm
- [ ] Solve IK analytically for a 2-link planar arm and numerically for 3-DOF
- [ ] Derive the Jacobian and find the singular configurations

## Key concepts
- Rotation matrices, homogeneous transforms, SE(3)
- Denavit-Hartenberg and product-of-exponentials conventions
- Forward kinematics
- Inverse kinematics: analytic and numerical (Newton, damped least squares)
- The Jacobian, singularities and manipulability

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why are rotation matrices preferred over Euler angles for computation?
   - *My answer:*
2. What physically happens to a robot arm at a singularity?
   - *My answer:*

## Hands-on
Implement FK, the Jacobian and damped-least-squares IK for a planar 3-link arm in NumPy; animate reaching a target with matplotlib.

Code and results: [`exercises/wk13-kinematics`](../../exercises/wk13-kinematics/)

## Resources
- Lynch & Park, *Modern Robotics* (free PDF + videos) - Ch. 2-6
- Corke, *Robotics, Vision and Control* + Robotics Toolbox for Python

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
