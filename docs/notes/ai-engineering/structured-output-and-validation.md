---
title: Structured Output and Validation
summary: Getting a shape back from a system that only emits text — and handling the times you don't.
type: pattern
status: seed
difficulty: intermediate

topics:
  - structured-output
  - validation
  - model-interfaces
projects: []
runtime:
  - python
  - typescript
last_tested:

tags:
  - topic/structured-output
  - topic/validation
---

# Structured Output and Validation

## 1. The Problem

You asked for JSON. You got JSON wrapped in a code fence, with a friendly
sentence above it. Then, once in a few hundred calls, you got JSON with a
trailing comma. Your parser raised, the request 500'd, and the user saw nothing.

The model is a text generator. A schema is a promise something else has to keep.

## 2. Mental Model

<!-- Something like: treat model output as untrusted input from a remote system.
     Parse, do not trust; validate at the boundary; have a defined behaviour for
     the invalid case, because there will be one. -->

## 3. Minimal Build

<!-- Schema-constrained generation, a validator on the way out, and one explicit
     path for the failure case — repair, retry, or degrade. -->

## 4. What Breaks

<!--
- valid JSON that violates the schema
- a required enum filled with a plausible value you never defined
- correct shape, hallucinated contents
- truncation at max_tokens producing a half object
- a repair retry that costs more than the original call
- streaming: partial JSON is not parseable until it is complete
- nested optionality the model resolves differently each time
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

## 8. Decision Record

## 9. References
