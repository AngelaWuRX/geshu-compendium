---
title: The Agent Loop That Never Stopped
summary: A missing termination condition burned a day of API budget in forty minutes.
type: postmortem
status: seed
difficulty: intermediate

topics:
  - agents
  - reliability
  - cost
projects:
  - postmortem-agent
last_tested:

tags:
  - topic/agents
  - topic/reliability
---

# The Agent Loop That Never Stopped

<!--
Written for a personal project, but written seriously. The value is in the
discipline: a real postmortem separates what happened from why it happened,
and treats "we did not notice" as its own failure worth fixing.

Blameless applies even when the only person to blame is you.
-->

## Incident

<!-- One paragraph. What went wrong, when, and for how long. -->

## Impact

<!-- Quantified: requests, dollars, data, time. "Some" is not an impact. -->

## Timeline

<!-- Absolute timestamps. Include when you *noticed*, not just when it began. -->

| Time | Event |
|------|-------|
|      |       |

## Root cause

<!--
The condition that, removed, prevents this class of failure. Not the last
thing you touched before it broke.
-->

## Contributing factors

<!-- What made it possible, worse, or slower to spot. -->

## Detection failure

<!--
Why you did not find out sooner, and what signal would have told you. Often
the most valuable section — an incident you detect in thirty seconds is a
different incident.
-->

## Resolution

<!-- What actually stopped the bleeding, including anything you tried that did not. -->

## Preventive changes

<!--
Specific and checkable. "Be more careful" is not a change; a hard iteration
cap with a test that asserts it is.
-->

## What I misunderstood

<!--
The belief you held that turned out to be wrong. This is the section that
makes a postmortem worth reading twice.
-->
