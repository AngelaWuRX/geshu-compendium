---
title: Observability for Model-Backed Applications
summary: The service is healthy, every span is green, and the answers are wrong.
type: pattern
status: seed
difficulty: advanced

topics:
  - observability
  - tracing
  - cost
  - evaluation
projects:
  - postmortem-agent
runtime:
  - python
last_tested:

tags:
  - topic/observability
  - topic/evaluation
---

# Observability for Model-Backed Applications

## 1. The Problem

Every dashboard is green. Latency is flat, the error rate is zero, no alert has
fired in a week. A user emails to say the assistant has been citing the wrong
document since Tuesday.

Conventional observability answers "did it respond". The failure mode of a
model-backed system is that it responded perfectly, quickly, with a 200, and was
wrong — and no counter you currently export can see that.

## 2. Mental Model

<!-- Something like: for a model-backed system the trace is the unit of debugging,
     not the log line. What you need to reconstruct is the whole decision:
     inputs, retrieved context, prompt version, model version, output, cost. -->

## 3. Minimal Build

<!-- Trace one request end to end — retrieval, assembly, generation, validation —
     with prompt version, model version, token counts and cost as span
     attributes. Then reconstruct a single bad answer from the trace alone. -->

## 4. What Breaks

<!--
- logs full of prompts, which is now a data retention and privacy problem
- sampling that drops exactly the rare failures worth reading
- no prompt or model version recorded, so a regression cannot be attributed
- cost attributed per service instead of per feature or per user
- an alert on error rate when the failure mode is silent wrongness
- a trace that stops at the API boundary and hides the retrieval step
- quality measured only by user reports, which arrive late and biased
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

## 8. Decision Record

## 9. References
