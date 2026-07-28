---
title: Foundations
summary: The layer everything else assumes — and only the parts that change how you build.
---

# Foundations

Everything above this layer assumes it works. Requests, concurrency, storage,
the network, the shape of a process — you can build without being able to
explain them, right up until something fails in a way that only makes sense one
level down.

This section is not a textbook rewrite. It only covers the parts that have
actually changed a decision I made. Probability is the clearest example: the
useful version is not the formula, it is the line from Bayes' rule to classifier
confidence, spam filtering, ranking, hallucination detection and how you read an
online experiment.

## In this section

| Note | Status | What it answers |
|---|---|---|
| [How an HTTP request moves through a fullstack application](http-request-lifecycle.md) | `seed` | Where does the time go, and who can drop your request? |
| [Async execution, concurrency and parallelism](async-concurrency-parallelism.md) | `seed` | Three different things one keyword hides. |

## Planned

Data structures and algorithms · Git · Linux and the shell · processes and
concurrency · networking · HTTP · security fundamentals · probability and
statistics · linear algebra · optimisation.

Course-shaped notes on several of these already exist under
[Reference](../../learn/foundations.md) — they are input to this section, not
a substitute for it.
