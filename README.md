# geshu-compendium
> A living notebook recording my daily work progress related to AI.

Sections appear here when there are notes worth reading in them, not before.

I'm making this public to keep myself honest: the point is to make real
progress every single day, where anyone can see whether I actually did.

I'm *not* publishing solutions or staff materials. These are my own
explanations, diagrams, and mental models. Because these notes follow my own
understanding, they don't mirror any official course structure or cover every
topic from class.

## Why this exists

Modern AI systems — LLMs, agents, tools — can "hold" far more surface detail
than any human. For a while that made me feel like I couldn't keep up with what
the agent was even trying to do, which was genuinely frustrating. I've come to
believe the best way to learn is by implementing: powerful agents are a
multiplier *once you have a solid foundation of your own*, never a substitute
for one.

The trend is that an engineer should understand the full stack. But
"understanding the full stack" shouldn't mean staying a code implementer
forever — it should mean growing into the senior-engineer role, where the job
is to review the work and ship the high-level architecture, and to keep the
coding agent on the right track.

If it helps other people along the way, even better.

## What's inside

### 🧮 Projects

Where I actually build things and apply what I'm learning.

- **Postmortem agent** — my implementation track for *Designing Data-Intensive
  Applications*: hardening a real agent repo one DDIA chapter at a time.
- **LeetCode** — the practice plan in my `python` folder, worked problem by
  problem.

### 📝 Blog — Paper Notes

Short writeups on papers I'm reading: the key idea in plain language, focused on
the key result. What I care about most right now is learning how to recognise a
genuinely valuable idea — and staying ahead of where AI is going.

- I'm about to start as an agent-safety intern, so I'm reading into that area.
- Plus notable papers from the top conferences.

**I'm not pretending to be an expert; this is a record of my own learning process.**

### 📚 Notes

Reference material — useful, but not the point of this repo.

- **Networks**
  Random graphs, concentration, the giant component, branching processes,
  configuration models, small worlds, preferential attachment, PageRank and
  mixing, spectral clustering, cascades, SIR. The most complete section by
  some distance — each note follows the same shape: what it is → definitions →
  how to recognise it → standard proof moves → lemmas → common mistakes.

- **Machine Learning**
  Probability and MLE/MAP through regression, clustering, classifiers,
  optimisation, neural nets, CNNs/ResNet, transformers, language models and
  self-supervised learning. Each note carries interview Q&A cards.

- **Data Structures**
  Lists, trees, heaps, hashing, sorting, union-find. Intuition → invariants →
  complexity.

- **Algorithms**
  Divide and conquer, linear programming, reductions, MSTs, shortest paths,
  graph traversal.

## Website

This repo builds into a small documentation site (MkDocs + GitHub Pages). I'm
also using it as a way to learn UI/UX, so it shouldn't look like generic,
AI-generated web design.

Once deployed, it's available at:

> [geshu-compendium](https://angelawurx.github.io/geshu-compendium/)

---

Notes are [CC BY-NC-SA 4.0](LICENSE-CONTENT); the site's code is [MIT](LICENSE).
If you're an instructor or TA and something here shouldn't be public, open an
issue and I'll remove it.
