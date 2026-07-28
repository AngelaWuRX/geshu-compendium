---
title: From Prompt to Model Response
summary: What actually happens between your string and the text that comes back.
type: concept
status: seed
difficulty: beginner

topics:
  - model-interfaces
  - tokens
  - context-window
projects: []
runtime:
  - python
last_tested:

tags:
  - topic/model-interfaces
---

# From Prompt to Model Response

## 1. The Problem

The same prompt returns a good answer on Tuesday and a bad one on Wednesday. You
did not change it. Somewhere between your string and the response there is a
tokeniser, a context window with a limit, a sampling temperature, a system
prompt you did not write, and a model version that moved — and if you cannot
name which one changed, you are debugging by superstition.

## 2. Mental Model

<!-- Something like: the model sees a single token sequence. Roles, formatting
     and your careful structure are conventions rendered into that sequence
     before inference, not features of it. -->

## 3. Minimal Build

<!-- One raw API call with no SDK sugar: messages in, tokens counted, response
     and usage printed. Then the same call with temperature and max tokens
     varied, so the knobs are attached to observed behaviour. -->

## 4. What Breaks

<!--
- the context window fills and the earliest instructions fall out
- retries duplicate a request that already succeeded
- a rate limit arrives as a 429 mid-conversation
- the model version changes under a floating alias
- non-determinism read as a bug in your code
- cost grows with conversation length, quietly and quadratically
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

## 8. Decision Record

## 9. References
