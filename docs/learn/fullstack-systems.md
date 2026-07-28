---
title: Fullstack Systems path
summary: Identity and authority, streaming, and work that outlives the request that started it.
---

# Fullstack Systems

Three problems every real product hits, which tutorials cover separately and
never together. They belong in one path because they share a shape: the request
is not a closed transaction. Someone else's authority is involved, the response
arrives over time, or the work outlasts the connection.

## The path

1. **[Authentication is identity plus authority](../notes/backend/authentication.md)** · `seed`

    First, because every later decision is scoped by it. A background job runs
    as *someone*, and a streamed response is streamed *to* someone.

2. **[Streaming responses from server to UI](../notes/frontend/streaming-responses.md)** · `seed`

    The response stops being a single value and becomes a sequence. Errors,
    retries and cancellation all have to be rethought once the first byte is
    already gone.

3. **[Background jobs and idempotency](../notes/backend/background-jobs-and-idempotency.md)** · `seed`

    The work outlives the request entirely. Everything from the Foundations
    path — concurrency, transactions, failure — arrives at once here, which is
    why it comes last.

## The thread

Read in order, the three notes are one escalating question: *what happens when
the request ends before the work does?* Streaming answers "the response is
partial". Background jobs answer "the response is a receipt". Authentication is
what makes both of them safe rather than merely possible.

## Prerequisites

[Foundations](foundations.md), particularly concurrency and transactions. You
can read this path first, but the third note will feel like a list of rules
rather than consequences.

## Next

[AI Applications](ai-applications.md) — the same systems, now with a
probabilistic dependency in the middle.
