# Week 12: System identification

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Identify a DC motor model from logged encoder data
- [ ] Fit physical parameters (J, b, K) with scipy.optimize.least_squares
- [ ] Validate a model on data that was not used for fitting

## Key concepts
- Step-response and frequency-sweep identification
- Least-squares parameter estimation (ARX models)
- Grey-box fitting of physical parameters
- Validation on held-out data

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why is a step input often a poor excitation signal?
   - *My answer:*
2. What is overfitting in system identification?
   - *My answer:*

## Hands-on
Generate noisy data from a 'true' DC motor, then identify it by (a) first-order step fit and (b) least-squares ARX. Compare the fits.

Code and results: [`exercises/wk12-sysid`](../../exercises/wk12-sysid/)

## Resources
- Ljung, *System Identification: Theory for the User* (reference)
- MATLAB Tech Talks - System Identification series

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
