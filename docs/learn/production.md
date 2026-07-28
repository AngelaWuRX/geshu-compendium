---
title: Production path
summary: How you know it works before shipping, and how you find out when it stops.
---

# Production

Two notes, and they are the same question at two different times: *how do you
know?* Before shipping, the answer is evaluation. After shipping, the answer is
observability. A system with neither is being assessed by whether anyone has
complained yet.

## The path

1. **[Evaluating an AI feature before shipping](../notes/ai-engineering/evaluating-an-ai-feature.md)** · `seed`

    Converting taste into a number that regresses. Thirty labelled examples and
    one command beat three examples and a good feeling, and the gap is not close.

2. **[Observability for model-backed applications](../notes/production/observability-for-model-backed-apps.md)** · `seed`

    The failure mode is a fast, confident, wrong answer with a 200 status. No
    conventional dashboard shows it. This is what to record so a bad answer can
    be reconstructed after the fact.

## Why the first note lives elsewhere

Evaluation is filed under [AI Engineering](../notes/ai-engineering/index.md)
because that is the capability it belongs to. It appears here because reading
order and filing order are different questions — the same reason the
[Foundations](foundations.md) path ends in a Data Systems note.

## The connection worth noticing

These two are one system, not two chores. The traces from the second note are
where the golden dataset in the first note comes from: real failures, captured
with enough context to be replayed. Teams that build them separately end up
evaluating against inputs they invented, which is how a metric improves while
users get worse answers.

## Prerequisites

[AI Applications](ai-applications.md). Evaluating a pipeline you have not built
is an academic exercise.
