# Control & Robotics Journey

My structured path from a BSc in Systems Engineering to robotics MS/PhD readiness: revising classical control, learning modern control and estimation, and applying it to robot arms, mobile robots and balancing robots. Everything is built hands-on, from simulation to hardware.

> **Started:** September 2026 · **Plan:** 24 weeks · **Current week:** 1

## Roadmap
- **Phase 1 - Classical control revision** (weeks 1-6): Refresh the undergraduate core fast: modelling, time/frequency response, stability, PID, digital implementation.
- **Phase 2 - Modern control & estimation** (weeks 7-12): State-space methods, optimal control (LQR), Kalman filtering, and system identification - the language of grad-level robotics.
- **Phase 3 - Robotics** (weeks 13-19): Kinematics, dynamics and control of manipulators and mobile robots, and the ROS 2 toolchain.
- **Phase 4 - Advanced control & capstone** (weeks 20-24): Nonlinear control and MPC, then finish a capstone project and polish the portfolio.

| Week | Phase | Topic | Hands-on | Status |
|---:|:-:|---|---|---|
| 1 | 1 | [Modelling dynamic systems](notes/phase-1-classical-control/wk01-modeling.md) | [exercise](exercises/wk01-modeling/) | Not started |
| 2 | 1 | [Time response & performance specs](notes/phase-1-classical-control/wk02-time-response.md) | [exercise](exercises/wk02-time-response/) | Not started |
| 3 | 1 | [Stability & root locus](notes/phase-1-classical-control/wk03-stability-rootlocus.md) | [exercise](exercises/wk03-stability-rootlocus/) | Not started |
| 4 | 1 | [Frequency response, Bode & Nyquist](notes/phase-1-classical-control/wk04-frequency-response.md) | [exercise](exercises/wk04-frequency-response/) | Not started |
| 5 | 1 | [PID control in practice](notes/phase-1-classical-control/wk05-pid.md) | [exercise](exercises/wk05-pid/) | Not started |
| 6 | 1 | [Digital control & implementation](notes/phase-1-classical-control/wk06-digital-control.md) | [exercise](exercises/wk06-digital-control/) | Not started |
| 7 | 2 | [State-space representation](notes/phase-2-modern-control/wk07-state-space.md) | [exercise](exercises/wk07-state-space/) | Not started |
| 8 | 2 | [Controllability, observability, pole placement & observers](notes/phase-2-modern-control/wk08-pole-placement.md) | [exercise](exercises/wk08-pole-placement/) | Not started |
| 9 | 2 | [Optimal control - LQR](notes/phase-2-modern-control/wk09-lqr.md) | [exercise](exercises/wk09-lqr/) | Not started |
| 10 | 2 | [State estimation - Kalman filters](notes/phase-2-modern-control/wk10-kalman.md) | [exercise](exercises/wk10-kalman/) | Not started |
| 12 | 2 | [System identification](notes/phase-2-modern-control/wk12-sysid.md) | [exercise](exercises/wk12-sysid/) | Not started |
| 13 | 3 | [Robot kinematics](notes/phase-3-robotics/wk13-kinematics.md) | [exercise](exercises/wk13-kinematics/) | Not started |
| 15 | 3 | [Robot dynamics](notes/phase-3-robotics/wk15-dynamics.md) | [exercise](exercises/wk15-dynamics/) | Not started |
| 16 | 3 | [Manipulator control](notes/phase-3-robotics/wk16-manipulator-control.md) | [exercise](exercises/wk16-manipulator-control/) | Not started |
| 17 | 3 | [Mobile robot kinematics & control](notes/phase-3-robotics/wk17-mobile-robots.md) | [exercise](exercises/wk17-mobile-robots/) | Not started |
| 18 | 3 | [ROS 2 & simulation toolchain](notes/phase-3-robotics/wk18-ros2.md) | [exercise](exercises/wk18-ros2/) | Not started |
| 20 | 4 | [Nonlinear control](notes/phase-4-advanced-control/wk20-nonlinear.md) | [exercise](exercises/wk20-nonlinear/) | Not started |
| 21 | 4 | [Model Predictive Control](notes/phase-4-advanced-control/wk21-mpc.md) | [exercise](exercises/wk21-mpc/) | Not started |

## Portfolio projects
Each project lives in its own repository (linked below as they start), with simulation, hardware, results and a write-up.

| # | Project | Weeks | Key skills | Status / repo |
|---|---|---|---|---|
| P1 | DC motor speed & position control | 4-7 | System identification, PID tuning & anti-windup, Bode / margins | Not started |
| P2 | Self-balancing robot (inverted pendulum) | 9-13 | State-space modelling, LQR, Complementary & Kalman filtering | Not started |
| P3 | Robot arm: kinematics, dynamics & control | 15-18 | Rigid-body kinematics, Lagrangian dynamics, Computed torque control | Not started |
| P4 | ROS 2 differential-drive robot with EKF localisation | 17-22 | ROS 2 (rclpy/rclcpp), URDF/TF2, EKF sensor fusion | Not started |
| P5 | Capstone: MPC for a constrained robot | 21-24 | Nonlinear MPC, Numerical optimisation (CasADi, IPOPT, acados), Real-time constraints | Not started |

## Weekly log
Short weekly entries (what I studied, what I built, what broke, what's next) are in [`log/weekly-log.md`](log/weekly-log.md).

## Tools
Python (NumPy, SciPy, python-control, CasADi), MATLAB/Simulink, ROS 2, MuJoCo / PyBullet / Gazebo, Arduino / ESP32, Raspberry Pi / Jetson.

I study with [Control Engineering Tutor](https://github.com/Ade1damola/control-engineering-tutor), a Streamlit app I built with an LLM tutor, an interactive control lab (PID, Bode, root locus, LQR) and progress tracking.

## Repository layout
```
notes/        one page per topic: objectives, my notes, self-check answers, reflection
exercises/    code + plots for each topic's hands-on exercise
log/          weekly progress log
```

## Contact
Website: [ade1damola.github.io](https://ade1damola.github.io)
