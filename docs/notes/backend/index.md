---
title: Backend Engineering
summary: The service layer, written so each note also answers when *not* to build the thing.
---

# Backend Engineering

Every note in this section has to get past "how do you write one". That part is
usually a library call and a page of documentation. The parts worth writing down
are the other six:

- why it is needed
- when it is *not* needed
- where it fails
- how to test it
- how to observe it in production
- how to recover

A note that only answers the first question is a tutorial, and there are already
enough of those.

## In this section

| Note | Status | What it answers |
|---|---|---|
| [Authentication is identity plus authority](authentication.md) | `seed` | Two questions people collapse into one, and the bugs that follow. |
| [Background jobs and idempotency](background-jobs-and-idempotency.md) | `seed` | Work you cannot finish inside a request, run exactly once. |

## Planned

API design · background jobs · queues · webhooks · rate limiting · caching ·
idempotency · file uploads · real-time systems · observability · error
handling · API testing.
