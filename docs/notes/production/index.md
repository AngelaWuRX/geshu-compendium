---
title: Production Engineering
summary: The layer that separates a working demo from a system someone else depends on.
---

# Production Engineering

A demo has to work once, for you, on your machine, on an input you chose. A
production system has to work repeatedly, for someone else, on inputs nobody
anticipated, while you are asleep — and it has to tell you when it stops.

Model-backed systems add their own version of each concern. Deployment now
includes model migrations. Cost tracking is per-token rather than per-instance.
Rollback has to cover a prompt as well as a binary. An SLO on a probabilistic
output needs defining before it can be measured.

## In this section

| Note | Status | What it answers |
|---|---|---|
| [Observability for model-backed applications](observability-for-model-backed-apps.md) | `seed` | What to log when the output is text and the bug is quality. |

## Planned

Deployment · CI/CD · environments · secrets · logging · metrics · tracing ·
cost tracking · feature flags · incident response · load testing · model
migrations · data migrations · rollbacks · SLOs.

Incidents get written up under [Postmortems](../../postmortems/index.md) rather
than here — this section is the machinery, those are the times it was not enough.
