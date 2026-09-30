# Week 4: Frequency response, Bode & Nyquist

**Status:** Not started · **Confidence:** -/5 · **Dates:** -

## Objectives
- [ ] Read gain/phase margins from a Bode plot and relate phase margin to overshoot
- [ ] Explain the waterbed effect and the S + T = 1 trade-off
- [ ] Show how a time delay limits achievable bandwidth

## Key concepts
- Bode magnitude/phase plots and asymptotes
- Gain and phase margins, crossover frequency
- Nyquist stability criterion
- Sensitivity S and complementary sensitivity T; bandwidth
- Loop shaping; effect of time delay on phase

## My notes
<!-- Summarise in your own words. GitHub renders LaTeX: inline $G(s)$, display $$ ... $$ -->

## Self-check (answer before looking anything up)
1. Why is phase margin a better robustness measure than 'the poles are stable'?
   - *My answer:*
2. What does a peak in |S(jw)| tell you about disturbance amplification?
   - *My answer:*

## Hands-on
Tune the PID in the Control Lab to get phase margin > 60 deg, then read off the crossover frequency and compare it with the closed-loop rise time.

Code and results: [`exercises/wk04-frequency-response`](../../exercises/wk04-frequency-response/)

## Resources
- Astrom & Murray - Ch. 9-12
- Steve Brunton, 'Control Bootcamp' (YouTube) - robustness lectures

## Reflection
- What clicked:
- What is still fuzzy:
- How it connects to robotics:
