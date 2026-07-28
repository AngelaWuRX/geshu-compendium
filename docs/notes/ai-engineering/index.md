---
title: AI Engineering
summary: The core layer — model interfaces, prompts, retrieval, agents, evaluation, safety.
---

# AI Engineering

The centre of this site. Everything else is either the ground this stands on or
the machinery that keeps it running.

Six sub-areas, and the ordering is deliberate: you cannot evaluate a retrieval
system you cannot call reliably, and you cannot make an agent safe before you
can make its output structured.

**Model interfaces** — text generation, structured generation, streaming, tool
calling, multimodal input, routing, fallback, retries, context management.

**Prompt systems** — prompt anatomy, system and developer instructions,
few-shot examples, versioning, structured prompts, injection, context conflicts.

**Retrieval** — ingestion, chunking, embeddings, metadata filters, keyword
search, hybrid retrieval, reranking, context assembly, citation grounding.

**Agents** — tools, planning, state, memory, approval, retries, termination,
durable execution, agent evaluation.

**Evaluation** — golden datasets, rubrics, deterministic checks, LLM judges,
retrieval metrics, regression testing, latency and cost, human feedback,
failure taxonomies.

**Safety and reliability** — prompt injection, data leakage, permission
boundaries, tool validation, output validation, sandboxing, rate limits, audit
trails, graceful degradation.

## In this section

| Note | Status | What it answers |
|---|---|---|
| [From prompt to model response](prompt-to-model-response.md) | `seed` | What actually happens across that API call. |
| [Structured output and validation](structured-output-and-validation.md) | `seed` | Getting a shape back, and what to do when you don't. |
| [Embeddings and semantic retrieval](embeddings-and-semantic-retrieval.md) | `seed` | What a vector represents, and what it cannot. |
| [Building a minimal RAG pipeline](minimal-rag-pipeline.md) | `seed` | The smallest honest version, end to end. |
| [Evaluating an AI feature before shipping](evaluating-an-ai-feature.md) | `seed` | How you know it works before users tell you. |
