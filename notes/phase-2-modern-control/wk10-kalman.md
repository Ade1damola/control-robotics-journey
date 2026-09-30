# Week 10: State estimation - Kalman filters

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Fuse accelerometer and gyro data to estimate tilt (complementary and Kalman)
- [ ] Implement a KF from scratch in NumPy
- [ ] Implement an EKF for a differential-drive robot's pose

## Key concepts
- Probability review: Gaussian, covariance
- Complementary filter for IMU tilt
- Discrete Kalman filter predict/update
- Tuning Q and R noise covariances
- Extended Kalman Filter (EKF) for nonlinear systems; LQG

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why can't you just integrate the gyro to get the angle?
   - *My answer:*
2. What does the Kalman gain do when measurement noise R is large?
   - *My answer:*

## Hands-on
Work through chapters 1-8 of Labbe's 'Kalman and Bayesian Filters in Python', then write a 1D constant-velocity KF from scratch.

Code and results: [`exercises/wk10-kalman`](../../exercises/wk10-kalman/)

## Resources
- Roger Labbe, *Kalman and Bayesian Filters in Python* (free, GitHub: rlabbe)
- Thrun, Burgard & Fox, *Probabilistic Robotics* - Ch. 3

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
