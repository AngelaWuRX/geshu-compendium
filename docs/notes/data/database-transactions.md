---
title: Database Transactions Through Real Failure Cases
summary: What isolation levels buy you, demonstrated by breaking them on purpose.
type: concept
status: seed
difficulty: advanced

topics:
  - transactions
  - postgresql
  - reliability
course_sources:
  - databases
  - distributed-systems
projects:
  - postmortem-agent
runtime:
  - postgresql
  - python
last_tested:

tags:
  - topic/transactions
  - topic/reliability
---

# Database Transactions Through Real Failure Cases

## 1. The Problem

Two requests read the same balance, both see enough funds, and both withdraw.
The code has a check. The check passed twice. The account is negative.

Nothing was written incorrectly and no constraint was violated — the two
transactions simply could not see each other. Which is exactly what the default
isolation level promises, and almost nobody reads.

## 2. Mental Model

<!-- Something like: an isolation level is a list of anomalies the database
     promises to prevent. Everything not on the list is your problem. -->

## 3. Minimal Build

<!-- Two concurrent sessions against one Postgres instance, reproducing lost
     update, non-repeatable read, phantom read and write skew — each in a few
     lines, each provoked deliberately. -->

## 4. What Breaks

<!--
- read committed permits a lost update between your SELECT and your UPDATE
- write skew survives even under repeatable read
- serialisable turns the anomaly into a serialisation error the app must retry
- a retry loop that is itself not idempotent
- a long-running transaction pins the vacuum horizon and bloats the table
- a transaction held open across a network call to a model API
-->

## 5. Production Version

## 6. Live Lab

## 7. Build Challenge

## 8. Decision Record

## 9. References
