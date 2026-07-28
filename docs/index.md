---
hide:
  - navigation
  - toc
---

<div class="gx-home" markdown>

# geshu-compendium

Notes, experiments, and production patterns for building fullstack AI systems.
{: .gx-lede }

I'm building toward fullstack AI engineering: frontend interfaces, backend
systems, data infrastructure, model integration, evaluation, and production
reliability. This site is my live notebook — part field manual, part laboratory,
and part record of what broke along the way.

Every note answers the same three questions: **what problem does this solve,
how do I build it, and how does it fail in production?** The third one is where
most of the value is, and it is the one tutorials skip.

## Current focus

The structure is in place and most of it is empty — deliberately. The work now
is the [first twelve notes](notes/index.md): three foundations, three fullstack,
four AI, two production. Twelve real ones beat fifty stubs, and the failure mode
here is a beautifully organised vault with nothing written in it.

Alongside that: reading into agent safety, and hardening a postmortem agent into
something production-shaped. More detail on [Now](now.md).

## The capability map

Organised by what I can build, not by which classes I took. A database course
does not stay a database course; it gets decomposed into the capabilities it
actually teaches.

<div class="grid cards" markdown>

-   **[Foundations](notes/foundations/index.md)**

    ---

    Requests, concurrency, storage, the network. Only the parts that have
    changed a decision — probability as classifier confidence and evaluation,
    not as a formula sheet.

-   **[Frontend Engineering](notes/frontend/index.md)**

    ---

    The standard layer, plus what AI products need and ordinary UIs never did:
    token streaming, tool-call progress, human approval, citation rendering.

-   **[Backend Engineering](notes/backend/index.md)**

    ---

    APIs, auth, queues, idempotency, rate limits. Each note has to answer when
    *not* to build the thing, and where it fails — not just how to write one.

-   **[Data Systems](notes/data/index.md)**

    ---

    Schemas, transactions, indexes, migrations — and the tables an AI product
    actually needs, instead of everything crammed into one JSON column.

-   **[AI Engineering](notes/ai-engineering/index.md)**

    ---

    The core layer: model interfaces, prompt systems, retrieval, agents,
    evaluation, safety. Everything else is the ground under it or the machinery
    around it.

-   **[Production Engineering](notes/production/index.md)**

    ---

    Deployment, cost, tracing, rollbacks, SLOs — plus model migrations and the
    fact that a wrong answer still returns a 200.

</div>

## Recently

**2026-07-28** — Cut the home page back to the capability map: the featured
projects block and the blog / build-log cards are gone.

**2026-07-27** — Restructured the whole site around capability instead of
course; added the Learn paths, the status system, and the twelve first note
stubs. Full entry in the [changelog](changelog.md).

## Also here

<div class="grid cards" markdown>

-   **[Learn](learn/index.md)**

    ---

    Five reading paths through the notes, in the order the ideas actually depend
    on each other. Start here if the capability map looks like a list of words.

-   **[Labs](labs/index.md)**

    ---

    Experiments you run and change rather than code you read. No API key ever
    reaches the browser, and mock mode is the default.

</div>

## Reference

<!-- Intentionally blank for now. The 57 course-shaped pages are still reachable
     from the Reference branch of the nav; what this section should say about
     them is undecided. -->

---

Notes are [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/);
the site's code is MIT. If you're an instructor or TA and something here
shouldn't be public, open an issue and I'll remove it.
{: .gx-fine }

</div>
