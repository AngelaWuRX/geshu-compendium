---
title: AI Infrastructure path
summary: Routing, fallback, context management and durable agent execution — nothing written yet.
---

# AI Infrastructure

!!! warning "This path has no notes yet"

    Listed because it is the plan, not because it is done. Everything below is
    a title. Nothing here is written, and this page will say so until it isn't.

The distinction from [AI Applications](ai-applications.md): that path is about
making a model useful. This one is about treating a model call as what it
actually is — a slow, expensive, occasionally unavailable network dependency
that sometimes returns nonsense — and building the layer that absorbs it.

## Planned, in the order I expect to need them

1. **Model routing and fallback** — more than one provider, chosen per request,
    with a defined answer for when the first one is down.

2. **Context management** — what to keep, what to summarise, what to drop, and
    how to make that decision without silently deleting the instruction that
    mattered.

3. **Retries and rate limits** — the client-side half of somebody else's
    capacity planning, including why naive retries make an outage worse.

4. **Tools and tool validation** — the model asking for an action, and the
    boundary that decides whether it gets one.

5. **Agent state and memory** — what persists between turns, where it lives, and
    who is allowed to read it.

6. **Durable execution** — an agent run that survives a deploy, a crash and a
    thirty-minute gap, which is the point where this path meets
    [background jobs](../notes/backend/background-jobs-and-idempotency.md).

7. **Approval and termination** — a human in the loop before consequential
    actions, and a hard guarantee that the loop ends.

## Why it is empty

Per the site's own plan, the first twelve notes are deliberately the
application layer, not this one. Building agent infrastructure before evaluation
exists means having no way to tell whether any of it helped. Evaluation comes
first, in [Production](production.md).

## Prerequisites

[AI Applications](ai-applications.md) in full, plus
[Fullstack Systems](fullstack-systems.md) for durable execution.
