---
title: Embeddings and Semantic Retrieval
summary: What a vector actually represents, and the queries it reliably gets wrong.
type: concept
status: seed
difficulty: intermediate

topics:
  - embeddings
  - retrieval
  - vector-search
course_sources:
  - machine-learning
projects: []
runtime:
  - python
  - postgresql
last_tested:

tags:
  - topic/embeddings
  - topic/retrieval
---

# Embeddings and Semantic Retrieval

## 1. The Problem

Semantic search returns three documents that are clearly about the right topic
and do not contain the answer. Meanwhile a plain keyword search for the exact
error code finds it immediately.

Similar is not the same as relevant, and an embedding only knows about the first
one.

## 2. Mental Model

<!-- Something like: an embedding places text by usage, not by meaning you chose.
     Nearest neighbours are neighbours in that space — which encodes topic well,
     negation badly, and rare identifiers hardly at all. -->

## 3. Minimal Build

<!-- Embed a small corpus, store the vectors, query by cosine similarity, print
     the neighbours. Then run the same queries through keyword search and put the
     two result lists side by side. -->

## 4. What Breaks

<!--
- negation: "not covered by warranty" retrieves the warranty page
- exact identifiers, error codes and names, which keyword search finds instantly
- chunks split mid-argument so no single chunk holds the answer
- the query and documents embedded by different models or versions
- similarity scores compared across models as if they meant the same thing
- an index that silently goes stale after documents change
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

## 8. Decision Record

## 9. References
