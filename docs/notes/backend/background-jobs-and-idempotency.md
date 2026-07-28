---
title: Background Jobs and Idempotency
summary: Accepting work you cannot finish inside a request, exactly once.
type: pattern
status: seed
difficulty: intermediate

topics:
  - queues
  - reliability
  - idempotency
course_sources:
  - distributed-systems
projects: []
runtime:
  - python
  - postgresql
last_tested:

tags:
  - topic/queues
  - topic/reliability
---

# Background Jobs and Idempotency

## 1. The Problem

Your API accepted a request that takes eight minutes to finish. The browser may
disconnect, the server may restart, and the user still expects a result. What
owns the work now?

## 2. Mental Model

> A queue separates accepting work from executing work.

## 3. Minimal Build

<!-- A jobs table, a worker loop, a status endpoint. Postgres only — no broker
     yet, because the broker is the thing this note has to justify. -->

## 4. What Breaks

<!--
- worker crashes after completing the work but before acknowledging it
- the job therefore runs twice
- a poison message fails forever and blocks the queue behind it
- the backlog grows faster than it drains
- database and queue state disagree about what happened
- the user cancels after execution has already started
- retries stampede when the downstream service recovers
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

<!-- Add cancellation without allowing a cancelled job to publish its result. -->

## 8. Decision Record

<!-- The DDIA-shaped question: at what scale does a database-backed queue stop
     being the right answer, and what measurement tells you that you crossed it? -->

## 9. References
