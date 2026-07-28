---
title: How an HTTP Request Moves Through a Fullstack Application
summary: One click, a dozen hops, and every place the request can quietly die.
type: concept
status: seed
difficulty: beginner

topics:
  - http
  - networking
  - latency
course_sources:
  - networking
  - web-development
projects: []
runtime:
  - typescript
  - python
last_tested:

tags:
  - topic/http
  - topic/networking
---

# How an HTTP Request Moves Through a Fullstack Application

## 1. The Problem

A button in the browser is slow and nobody can say why. The frontend engineer
says the API is slow, the backend engineer sees a 40 ms handler, and the
database shows a 3 ms query. Everyone is reading a real number, and the user is
still waiting two seconds.

The request passed through roughly a dozen places between the click and the
handler. Until you can name them, you cannot say which one is lying.

## 2. Mental Model

<!-- One sentence. Something like: a request is a chain of handoffs, and latency
     lives in the handoffs, not the handlers. -->

## 3. Minimal Build

<!-- Smallest end-to-end path: browser fetch -> server -> database -> response.
     Instrument each hop so the timings are visible. -->

## 4. What Breaks

<!--
- DNS resolves slowly or to something stale
- TLS handshake on every request because connections are not reused
- the connection pool is exhausted and the handler waits to even start
- a proxy timeout that is shorter than the handler's timeout
- the client gives up but the server keeps working
- the response is correct and the browser still blocks on rendering
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

## 8. Decision Record

## 9. References
