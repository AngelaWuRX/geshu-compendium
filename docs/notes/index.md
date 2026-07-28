---
title: Notes
summary: Every formal note, filed by engineering capability.
---

# Notes

Filed by capability, not by course. A database course does not stay a database
course — it gets decomposed into data modelling, indexes and query plans,
transactions, connection pooling, vector search. The question this site answers
is not *which classes did I take*, it is *which engineering capabilities do I
have*.

Reading order lives on the [Learn paths](../learn/index.md) instead.

## Status, and what it means

Every note carries one. They are honest labels, not decoration:

| Status | Means |
|---|---|
| `seed` | A problem statement and scattered thinking. Not yet worth your time. |
| `working` | Explanation and code exist, and may still change. |
| `stable` | Accurate enough that you can rely on it. |
| `production-tested` | The approach runs in a real project, with tests or monitoring behind it. |

## By capability

### [Foundations](foundations/index.md)

| Note | Status | Difficulty |
|---|---|---|
| [How an HTTP request moves through a fullstack application](foundations/http-request-lifecycle.md) | `seed` | beginner |
| [Async execution, concurrency and parallelism](foundations/async-concurrency-parallelism.md) | `seed` | intermediate |

### [Frontend Engineering](frontend/index.md)

| Note | Status | Difficulty |
|---|---|---|
| [Streaming responses from server to UI](frontend/streaming-responses.md) | `seed` | intermediate |

### [Backend Engineering](backend/index.md)

| Note | Status | Difficulty |
|---|---|---|
| [Authentication is identity plus authority](backend/authentication.md) | `seed` | intermediate |
| [Background jobs and idempotency](backend/background-jobs-and-idempotency.md) | `seed` | intermediate |

### [Data Systems](data/index.md)

| Note | Status | Difficulty |
|---|---|---|
| [Database transactions through real failure cases](data/database-transactions.md) | `seed` | advanced |

### [AI Engineering](ai-engineering/index.md)

| Note | Status | Difficulty |
|---|---|---|
| [From prompt to model response](ai-engineering/prompt-to-model-response.md) | `seed` | beginner |
| [Structured output and validation](ai-engineering/structured-output-and-validation.md) | `seed` | intermediate |
| [Embeddings and semantic retrieval](ai-engineering/embeddings-and-semantic-retrieval.md) | `seed` | intermediate |
| [Building a minimal RAG pipeline](ai-engineering/minimal-rag-pipeline.md) | `seed` | intermediate |
| [Evaluating an AI feature before shipping](ai-engineering/evaluating-an-ai-feature.md) | `seed` | advanced |

### [Production Engineering](production/index.md)

| Note | Status | Difficulty |
|---|---|---|
| [Observability for model-backed applications](production/observability-for-model-backed-apps.md) | `seed` | advanced |

## Reference

The course-shaped notes — Networks, Machine Learning, Data Structures,
Algorithms — are still here, under **Reference** in the navigation. Seventy-nine
of them, and the Networks section is the most developed writing on this site by
some distance.

They are input to the notes above rather than part of them, and they are not
being migrated wholesale. Per the site's own plan, spending months re-filing old
course notes is how you end up with a tidy archive and no engineering system of
your own.

## Browse by topic

<!-- material/tags -->

## Not built yet

Filtering by status, difficulty, runtime and project needs a generated index
plus a small client-side widget. It is deliberately not half-built: the tag
listing above is real and works, and the rest arrives when there are enough
notes for filtering to beat scrolling.
