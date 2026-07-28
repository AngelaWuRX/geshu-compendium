---
title: Async Execution, Concurrency and Parallelism
summary: Three different things, one overloaded keyword, and the bug that comes from conflating them.
type: concept
status: seed
difficulty: intermediate

topics:
  - concurrency
  - async
  - processes
course_sources:
  - operating-systems
projects: []
runtime:
  - python
  - typescript
last_tested:

tags:
  - topic/concurrency
---

# Async Execution, Concurrency and Parallelism

## 1. The Problem

You add `async` to a slow endpoint and it does not get faster. You add threads
to a CPU-bound loop in Python and it gets slower. Both outcomes are correct, and
both surprise people who learned the three words as synonyms.

## 2. Mental Model

<!-- Something like: concurrency is about structure — dealing with many things
     at once; parallelism is about execution — doing many things at once; async
     is one way to get concurrency without threads. -->

## 3. Minimal Build

<!-- The same workload three ways — sequential, async, multiprocess — over both
     an I/O-bound and a CPU-bound task, so the crossover is visible rather than
     asserted. -->

## 4. What Breaks

<!--
- one blocking call in an async handler stalls the whole event loop
- shared mutable state across threads with no lock
- an unbounded task group opens ten thousand connections
- exceptions in a fire-and-forget task vanish silently
- cancellation leaves a half-written row behind
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

## 8. Decision Record

## 9. References
