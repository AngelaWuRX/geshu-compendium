---
# ─── Identity ────────────────────────────────────────────────────────────────
title: Background Jobs and Idempotency
summary: Accepting work you cannot finish inside a request, exactly once.

# ─── Classification ──────────────────────────────────────────────────────────
# type:       concept | pattern | lab | build-log | postmortem | project
# status:     seed | working | stable | production-tested
# difficulty: beginner | intermediate | advanced
type: pattern
status: seed
difficulty: intermediate

# ─── Graph edges ─────────────────────────────────────────────────────────────
# `topics` is the source of truth for what this note is about. `tags` exists
# only to drive the colour-coded facets in the theme — mirror the topics you
# want visible as chips, prefixed `topic/`, and leave the rest out.
topics:
  - queues
  - reliability
  - idempotency
course_sources:
  - distributed-systems
projects:
  - postmortem-agent
runtime:
  - python
  - postgresql

# Set the day you last actually ran the code on this page. Blank means never.
last_tested:

tags:
  - topic/queues
  - topic/reliability
---

# Background Jobs and Idempotency

## 1. The Problem

<!--
Open with the situation, never the definition. The reader should feel the
problem before they meet the vocabulary.

Not this:
    A queue is a data structure that follows FIFO.

This:
-->

Your API accepted a request that takes eight minutes to finish. The browser may
disconnect, the server may restart, and the user still expects a result. What
owns the work now?

## 2. Mental Model

<!--
One sentence, accurate enough to reason with and short enough to remember.
It should let the reader predict behaviour they have not read about yet.

    A queue separates accepting work from executing work.
    Streaming does not make generation faster. It makes partial progress observable.
-->

> A queue separates accepting work from executing work.

## 3. Minimal Build

<!--
The smallest thing that runs. Complete enough to paste and execute — imports,
schema, entry point. Three suggestive lines are not a build; if the reader has
to guess the missing half, this section has failed.

State the runtime and how to start it.
-->

```python
# runnable: python 3.12, postgresql 16
```

## 4. What Breaks

<!--
The most important section on the page, and the one that separates this from a
tutorial. Enumerate concrete failures, not the abstract risk of failure.

    - worker crashes after completing work but before acknowledging
    - job runs twice
    - poison messages
    - queue backlog grows faster than it drains
    - database and queue state disagree
    - user cancels after execution has started
-->

## 5. Production Version

<!--
Upgrade the minimal build into something you would actually deploy:
validation, authentication, retries, idempotency, observability, cleanup,
rate limits, tests. Show the diff in thinking, not just the diff in code —
say which failure from §4 each addition answers.
-->

## 6. Live Lab

<!--
Something the reader operates, not just reads. Give exact steps and say what
they should observe.

    - change the concurrency and watch throughput plateau
    - inject latency and find the timeout cliff
    - kill the worker mid-job
    - send the same request twice
    - read the trace
-->

## 7. Build Challenge

<!--
A small engineering task with a real constraint — not a quiz question.

    Add cancellation without allowing a cancelled job to publish its result.
-->

## 8. Decision Record

<!--
Your own judgement, stated plainly, with the condition that would change it.
This is the section a reader cannot get from documentation, and the one that
shows engineering judgement rather than recall.

    I would use a database-backed queue below this scale because operational
    simplicity matters more than theoretical throughput.
-->

## 9. References

<!--
Only what you actually used. Official docs, papers, source code, specs, and
engineering writeups that earned their place. A link you skimmed is noise.
-->
