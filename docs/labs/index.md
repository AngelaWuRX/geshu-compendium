---
title: Labs
summary: Experiments you run and change, not code you read.
---

# Labs

A lab is not a code sample. The difference is that you are expected to change
something and watch the result move — the parameter sweep *is* the content, and
the explanation exists to tell you what to look for.

!!! note "No labs yet"

    The template and the runtime rules are in place; the experiments are not.
    Meanwhile the [notes](../notes/index.md) each carry a **Live Lab** section
    with the experiment they are heading toward.

## Runtimes

Every lab declares where it runs, because that decides whether you can do
anything with it at all:

| Runtime | What it needs from you | Cost |
|---|---|---|
| `browser-python` | Nothing. It runs in the page. | Free |
| `browser-node` | Nothing. It runs in the page. | Free |
| `local-docker` | Clone the repo, `docker compose up`. | Free |
| `cloud-api` | A model API key. | Real money — the lab states the estimate |

## Planned

- Compare chunk sizes on retrieval quality
- Simulate a retry storm and watch it prolong an outage
- Visualise an embedding space, then find two points it places wrongly
- Break a naive rate limiter
- Measure token streaming latency end to end

## The rule about model calls

No API key ever reaches the browser. A lab that calls a model calls an endpoint
on this site's own backend, and that endpoint must:

- cap the number of calls
- cap the maximum tokens
- allow no arbitrary tool execution
- validate input and output
- show the estimated cost before running
- offer a mock mode that works with no key at all

Mock mode is not a fallback, it is the default. A lab that only works when
someone is paying for it is a lab most readers cannot run.

## Interaction serves the concept

Not every page needs to become an IDE. Embedded execution earns its place where
the output is a number or a picture that changes — embeddings, probability,
evaluation metrics, chunking, ranking. Where the point is an architecture or a
failure mode, prose and a diagram are better, and adding a Run button just makes
the page slower.
