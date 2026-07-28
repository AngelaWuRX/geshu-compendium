---
title: Building a Minimal RAG Pipeline
summary: Ingest, chunk, embed, retrieve, assemble, answer, cite — the smallest honest version.
type: pattern
status: seed
difficulty: intermediate

topics:
  - retrieval
  - rag
  - citations
  - chunking
projects: []
runtime:
  - python
  - postgresql
last_tested:

tags:
  - topic/retrieval
  - topic/rag
---

# Building a Minimal RAG Pipeline

## 1. The Problem

The model does not know about your documents, and you cannot fit them in the
context window. So you retrieve a few and paste them in — which works on the
first demo, and then produces a confident answer citing a passage that says the
opposite.

Retrieval augmentation is seven decisions in a trench coat. Each one can fail
independently, and the failures all look identical from the outside: a fluent,
wrong answer.

## 2. Mental Model

<!-- Something like: RAG is a search problem wearing a generation costume. If the
     right passage is not in the assembled context, no prompt fixes it. -->

## 3. Minimal Build

<!-- Ingest -> chunk -> embed -> store -> retrieve -> assemble -> generate, with
     citations attached to spans. Every stage inspectable, because debugging the
     pipeline means reading its intermediate output. -->

## 4. What Breaks

<!--
- the answer exists in the corpus and never enters the context
- retrieved passages contradict each other and the model picks one
- a citation points at a chunk that does not support the sentence
- chunk boundaries orphan the sentence that carried the qualifier
- context assembled in an order that buries the best passage
- the model answers from pretraining and cites your document anyway
- a document is deleted upstream and its embedding lives on
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

## 8. Decision Record

## 9. References
