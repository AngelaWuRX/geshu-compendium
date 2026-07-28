---
title: Authentication Is Identity Plus Authority
summary: Who are you, and what are you allowed to do — two questions, routinely collapsed into one.
type: concept
status: seed
difficulty: intermediate

topics:
  - auth
  - security
  - api-design
course_sources:
  - web-development
projects: []
runtime:
  - typescript
  - postgresql
last_tested:

tags:
  - topic/auth
  - topic/security
---

# Authentication Is Identity Plus Authority

## 1. The Problem

The endpoint checks that the caller is logged in and returns the document. It
never checks whether *this* logged-in user is allowed to read *that* document.
Every authenticated user can now read every document by changing a number in the
URL, and the code looks completely reasonable.

The check that was written answers "who are you". The check that was needed
answers "what are you allowed to do".

## 2. Mental Model

<!-- Something like: authentication establishes identity; authorisation is a
     decision made per resource, per action, with that identity as one input. -->

## 3. Minimal Build

<!-- Sessions, then a token, then one authorisation check that takes the
     resource as an argument rather than only the user. -->

## 4. What Breaks

<!--
- an object reference the user was never meant to name
- a token that cannot be revoked before it expires
- permissions checked in the UI and nowhere else
- a role check that passes for a resource in another tenant
- expiry, clock skew, and refresh races
- a background job running with more authority than the user who queued it
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

## 8. Decision Record

## 9. References
