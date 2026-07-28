---
title: AI Applications path
summary: From one model call to a retrieval pipeline that cites its sources.
---

# AI Applications

Four notes, ordered by what each one lets you stop worrying about. You cannot
build retrieval on a call you cannot make reliably, and you cannot build a
pipeline on output you cannot parse.

## The path

1. **[From prompt to model response](../notes/ai-engineering/prompt-to-model-response.md)** · `seed`

    The primitive. Tokens, context window, sampling, versioning — the variables
    that make "I didn't change anything" false.

2. **[Structured output and validation](../notes/ai-engineering/structured-output-and-validation.md)** · `seed`

    Turns the response from prose into something a program can act on. Required
    before the model can be a component rather than an endpoint.

3. **[Embeddings and semantic retrieval](../notes/ai-engineering/embeddings-and-semantic-retrieval.md)** · `seed`

    The other half of the system. What a vector represents, and the queries it
    reliably gets wrong — negation, identifiers, exact names.

4. **[Building a minimal RAG pipeline](../notes/ai-engineering/minimal-rag-pipeline.md)** · `seed`

    Assembles the previous three into something end to end, and makes the point
    the whole path exists for: retrieval augmentation is a search problem, and
    no prompt rescues a passage that was never retrieved.

## What this path deliberately skips

Agents. Tool use, planning and durable execution belong to
[AI Infrastructure](ai-infrastructure.md), and attempting them before structured
output and evaluation are solid is how you get a loop that never stops and a
bill you cannot explain.

## Prerequisites

[Fullstack Systems](fullstack-systems.md) for streaming — the first note
assumes you know why a response arrives in pieces.

## Next

[Production](production.md) for how to tell whether any of it actually works, or
[AI Infrastructure](ai-infrastructure.md) for what to build once it does.
