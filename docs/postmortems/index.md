---
title: Postmortems
summary: Incidents written up properly, personal projects included.
---

# Postmortems

Something broke, and the write-up treats it seriously: what happened, what it
cost, why it happened, why it was not caught sooner, and what changed as a
result.

Doing this for a personal project is not theatre. The discipline is what
transfers — separating the root cause from the last thing you touched, treating
*we did not notice for two hours* as its own failure, and naming the belief that
turned out to be wrong. Blameless still applies when the only person to blame is
me.

!!! note "No entries yet"

    Which is not a claim that nothing has broken. Entries appear as the
    [projects](../projects/index.md) accumulate real usage.

## The template

Every entry answers the same nine things, in this order:

```text
Incident
Impact
Timeline
Root cause
Contributing factors
Detection failure
Resolution
Preventive changes
What I misunderstood
```

Two of those carry most of the weight. **Detection failure** is where the
durable improvement usually hides — an incident you catch in thirty seconds is a
different incident. **What I misunderstood** is the one that makes the page
worth re-reading, and the one that is hardest to write honestly.

## Related

The machinery that is supposed to prevent these lives under
[Production Engineering](../notes/production/index.md). A postmortem that ends
in a preventive change should link the note that change belongs to — and if no
such note exists yet, that is a note worth writing.
