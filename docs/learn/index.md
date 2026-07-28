---
title: Learn
summary: Five reading paths through the notes, in the order the ideas actually depend on each other.
---

# Learn

The [notes](../notes/index.md) are filed by capability — where a thing belongs.
These paths are the other question: what order to read them in.

A path owns no pages. It is a sequence with an argument for why each step comes
where it does, and it crosses folders freely: the Foundations path ends in a
Data Systems note because you cannot reason about failure without transactions,
whatever folder they live in.

<div class="grid cards" markdown>

-   **[Foundations](foundations.md)**

    ---

    Requests, concurrency, and durable state. The layer every other path
    assumes. Start here if the rest looks like vocabulary.

-   **[Fullstack Systems](fullstack-systems.md)**

    ---

    Identity and authority, streaming, and work that outlives its request.
    The three things almost every real product needs and no tutorial covers
    together.

-   **[AI Applications](ai-applications.md)**

    ---

    From a single model call to a retrieval pipeline that cites its sources.
    The path from "it responds" to "it responds usefully".

-   **[AI Infrastructure](ai-infrastructure.md)**

    ---

    Routing, fallback, context management, durable agent execution. What holds
    up when a model call is a normal, unreliable dependency.

-   **[Production](production.md)**

    ---

    Evaluation before shipping, observability after. How you know it works, and
    how you find out when it stops.

</div>

## Which one

Reading in order is fine, but rarely what people need. Pick by the sentence
that sounds most like your current problem:

| If this is your problem | Start here |
|---|---|
| "I can build it but I can't explain why it's slow" | [Foundations](foundations.md) |
| "It works on my machine and falls over with two users" | [Fullstack Systems](fullstack-systems.md) |
| "The model answers, but the answers aren't good" | [AI Applications](ai-applications.md) |
| "It's good in the demo and flaky in the product" | [AI Infrastructure](ai-infrastructure.md) |
| "I don't know whether my change made it better" | [Production](production.md) |
