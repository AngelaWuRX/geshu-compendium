---
title: Evaluating an AI Feature Before Shipping
summary: How you know it works when the output is text and there is no right answer.
type: pattern
status: seed
difficulty: advanced

topics:
  - evaluation
  - testing
  - llm-judge
course_sources:
  - machine-learning
projects: []
runtime:
  - python
last_tested:

tags:
  - topic/evaluation
  - topic/testing
---

# Evaluating an AI Feature Before Shipping

## 1. The Problem

You changed the prompt and the three examples you keep re-running look better.
Ship it?

You have a sample size of three, chosen by you, on inputs you already knew about.
Every prompt change is a model change with no test suite behind it — and unlike a
failing assertion, a regression here comes back as slightly worse answers that
nobody reports.

## 2. Mental Model

<!-- Something like: evaluation converts taste into a number you can regress
     against. The number does not need to be correct; it needs to move in the
     same direction as quality, and it needs to exist before the change. -->

## 3. Minimal Build

<!-- Thirty labelled examples, a deterministic check where one is possible, a
     rubric-scored judge where it is not, and a single command that prints the
     score. Small enough to build in an afternoon, which is the point. -->

## 4. What Breaks

<!--
- a golden set drawn from the cases you already fixed
- an LLM judge that prefers its own writing style
- a judge scoring fluency while you care about correctness
- a metric that improves while users get worse answers
- test inputs leaking into the examples in the prompt
- averaging over a set too small to separate the conditions
- no cost or latency axis, so quality is bought at ten times the price
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

## 8. Decision Record

## 9. References
