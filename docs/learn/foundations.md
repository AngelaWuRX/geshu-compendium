---
title: Foundations path
summary: Requests, concurrency and durable state — the layer every other path assumes.
---

# Foundations

Three notes, and they build in one direction: what happens to a single request,
then what happens when many of them overlap, then what the database promises
when they overlap on the same row.

## The path

1. **[How an HTTP request moves through a fullstack application](../notes/foundations/http-request-lifecycle.md)** · `seed`

    Start here because it is the map. Everything later in this path is one of
    these hops going wrong.

2. **[Async execution, concurrency and parallelism](../notes/foundations/async-concurrency-parallelism.md)** · `seed`

    Once you can see one request, look at a thousand. This is where "add
    `async`" stops being a reflex and starts being a decision.

3. **[Database transactions through real failure cases](../notes/data/database-transactions.md)** · `seed`

    Concurrency with durable state attached. The anomalies here are the reason
    the previous note matters — and the reason a correct-looking check can pass
    twice.

## Why it ends in Data Systems

The third note is filed under Data Systems, not Foundations, because that is the
capability it belongs to. Paths cross folders on purpose: the filing question
and the reading-order question have different right answers.

## Already on this site

Course-shaped notes covering parts of this ground exist under **Reference** —
data structures, algorithms, probability. They are input to these notes rather
than a replacement: same material, different question. Reference asks *what is
this*; Foundations asks *what does it change about how I build*.

## Next

[Fullstack Systems](fullstack-systems.md) — the same concerns, now with a user
attached.
