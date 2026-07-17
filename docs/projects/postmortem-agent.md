# Postmortem Memory Agent

A project I'm hardening from a 12-hour hackathon prototype into something that
could actually run in production — using *Designing Data-Intensive
Applications* (DDIA) as the engineering lens.

## What it does

The agent ingests incident **postmortems**, builds a searchable **memory** of
past failures, and uses that memory to review pull requests and generate
follow-up artifacts — flagging changes that look like they could repeat a
mistake the team has already made and paid for.

The prototype worked as a demo. The interesting part — and the reason it pairs
so well with DDIA — is everything that stands between "works in a demo" and
"won't quietly corrupt its own memory at 3 a.m."

## The core idea

One principle ties the whole redesign together:

> Store the facts as an append-only **log of incidents** (the source of truth).
> Everything else — the vector memory, the generated artifacts, the review
> decisions — is **derived data** that can be rebuilt from that log. Every
> action that touches the outside world must be idempotent, replayable, and
> bounded in blast radius.

Get that right and the agent stops being a fragile demo and becomes a small
data system.

## Two kinds of failure

A reviewer agent can fail in two directions, and they don't cost the same:

- **False-block** — it flags a safe change. Annoying; slows people down.
- **False-safe** — it lets a dangerous change through. This is the expensive
  one: the incident it was supposed to prevent happens again.

So the whole thing is tuned to spend false-blocks to buy down false-safes — and
that trade-off is written down rather than left implicit.

## What DDIA changes, theme by theme

| DDIA theme | What it fixes in the agent |
|---|---|
| Reliability — fault ≠ failure | A single bad model response shouldn't crash an ingest. Wrap the fragile boundaries so a fault degrades instead of taking the system down. |
| Storage & the vector index | Understand what the vector store is actually doing — approximate nearest-neighbour recall can *miss*, and a miss here is a false-safe. |
| Encoding & evolution | The memory schema will change. Old records have to keep loading, so every field is versioned and read defensively. |
| Transactions & the dual-write problem | Writing to two stores can diverge. Pick one authority and rebuild the other from it; make record IDs content-addressed so re-ingesting the same postmortem is a no-op. |
| Unreliable systems | Every external call gets a timeout, bounded retries, and a blast-radius limit, so one hung dependency can't stall everything. |
| Batch & stream processing | Reframe the memory as a *derived view* of the incident log, with a rebuild path that replays the log — which is also how schema upgrades and embedding swaps happen safely. |
| Derived data & architecture | Write the reliability targets and the architecture down: source of truth, derived views, blast radius, and the rebuild story. |

## Where it's going

The end state isn't "more features" — it's engineering stability: a system whose
failure modes I can name, whose memory I can rebuild from scratch, and whose
architecture I can explain end to end. The same backbone — an append-only log
with everything else derived and replayable — is the foundation I want under the
other agent-tooling ideas I'm circling.
