---
title: Data Systems
summary: Storage, retrieval and the schema an AI product actually needs.
---

# Data Systems

Two halves. The first is ordinary and non-negotiable: schemas, transactions,
indexes, query plans, migrations. The second is what an AI product adds —
vector search, hybrid retrieval, and the fact that model output is now data you
have to store, version, evaluate and eventually delete.

The failure mode this section exists to prevent is putting everything in one
`messages` JSON column. The tables an AI system actually needs look closer to:

```text
users            conversations    messages
runs             tool_calls       artifacts
documents        chunks           embeddings
evaluations      feedback         usage_events
```

Each of those exists because something needs to be queried, evaluated, retried
or deleted independently. A blob answers none of those.

## In this section

| Note | Status | What it answers |
|---|---|---|
| [Database transactions through real failure cases](database-transactions.md) | `seed` | What isolation actually buys you, shown by breaking it. |

## Planned

PostgreSQL · schema design · indexing · query planning · migrations · object
storage · Redis · event logs · analytics · vector databases · hybrid search ·
data retention · privacy and deletion.
