---
title: Compare Chunk Sizes on Retrieval Quality
summary: Vary the chunk size, measure recall, and find where it stops helping.
type: lab
status: seed
difficulty: intermediate

# Every lab declares where it runs, because that decides whether the reader can
# do anything at all:
#   browser-python  — runs in the page, no install, no key
#   browser-node    — runs in the page, no install, no key
#   local-docker    — clone and `docker compose up`
#   cloud-api       — needs a model API key; costs money
runtime:
  - local-docker

topics:
  - retrieval
  - chunking
  - evaluation
projects:
  - postmortem-agent
last_tested:

tags:
  - topic/retrieval
  - topic/evaluation
---

# Compare Chunk Sizes on Retrieval Quality

## The question

<!--
One question with a measurable answer. "Explore chunking" is not a question.
"Does recall keep improving past 512 tokens on this corpus?" is.
-->

## What you need

<!--
Runtime, dependencies, dataset, and roughly how long a run takes. If it needs
a key, say which provider and give the rough cost of one full run.
-->

## Setup

```bash
```

## Run it

<!--
The default run, with the output the reader should see. If the numbers move
between runs, say by how much — otherwise they cannot tell a real effect from
noise.
-->

## Now change something

<!--
The actual lab. Name the knob, the range worth sweeping, and the shape of the
result you expect. Then give one setting that produces a *surprising* result,
because that is what makes the concept stick.
-->

## Break it

<!--
How to make the experiment produce a confidently wrong answer — leaked test
data, a metric that rewards the wrong thing, a corpus too small to separate
the conditions. Reading a broken result correctly is the transferable skill.
-->

## What I concluded

<!--
The finding, its limits, and what you would need to run before trusting it on
a different corpus.
-->
