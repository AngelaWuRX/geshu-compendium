---
title: Frontend Engineering
summary: The interface layer — plus everything AI products need that ordinary UIs never did.
---

# Frontend Engineering

Most of this layer is the standard set: rendering model, state, forms,
accessibility, performance, testing. What makes AI products different is that
the response arrives *over time* and may be *wrong*, and almost every unusual
requirement below follows from one of those two facts.

A form submits and gets an answer. A model call streams tokens, may call a tool
halfway through, may need a human to approve something before it continues, and
may produce a citation the user should be able to check. Those are interface
problems before they are model problems.

## In this section

| Note | Status | What it answers |
|---|---|---|
| [Streaming responses from server to UI](streaming-responses.md) | `seed` | How partial output reaches the screen, and what it costs. |

## Planned

The standard layer: React mental model · server and client components · state
management · forms and validation · optimistic updates · accessibility · design
systems · performance · browser storage · offline behaviour · testing.

The AI-specific layer, which is the reason this section exists: token
streaming · partial structured output · tool-call progress · interrupt and
resume · citation rendering · message branching · human approval UI ·
long-running task state · generated artifact previews.
