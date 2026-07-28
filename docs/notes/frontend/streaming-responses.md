---
title: Streaming Responses from Server to UI
summary: Streaming does not make generation faster; it makes partial progress observable.
type: pattern
status: seed
difficulty: intermediate

topics:
  - streaming
  - http
  - frontend
course_sources:
  - web-development
projects: []
runtime:
  - typescript
  - python
last_tested:

tags:
  - topic/streaming
  - topic/http
---

# Streaming Responses from Server to UI

## 1. The Problem

A model takes nine seconds to produce its answer. Behind a normal request the
user stares at a spinner for nine seconds and half of them leave. Streamed, the
first words appear in four hundred milliseconds and the same nine seconds feels
like the machine is working.

Nothing got faster. What changed is that progress became observable — and the
whole stack, from the handler to the proxy to the component, has to cooperate to
keep it that way.

## 2. Mental Model

> Streaming does not make generation faster. It makes partial progress
> observable.

## 3. Minimal Build

<!-- Server-sent events end to end: a generator on the server, a reader on the
     client, tokens on the screen. No framework, so the mechanism is visible. -->

## 4. What Breaks

<!--
- a proxy buffers the whole response and delivers it at the end
- compression middleware defeats chunking for the same reason
- the client disconnects and the server keeps generating, billed and unread
- an error occurs after a 200 and the first bytes are already sent
- partial JSON is not parseable JSON
- retry logic replays a half-consumed stream
- the component re-renders per token and drops frames
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

## 8. Decision Record

## 9. References
