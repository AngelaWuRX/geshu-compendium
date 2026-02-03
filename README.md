# geshu-compendium
> A living notebook for understanding core CS + math ideas deeply enough that AI tools become amplifiers, not replacements.

This repo hosts my personal notes for a small “curriculum”:

- UC Berkeley **CS61B** – data structures  
- UC Berkeley **CS170** – efficient algorithms (with pointers to LeetCode-style problems)  
- UC Berkeley **CS194** – advanced algorithms / networks / graphs  
- **CMU 15-850(C)** – Algorithms in the “Real World”  
- Plus **math + ML prerequisites** and a short **paper-reading blog**

The goal: make these concepts **approachable from zero**, while still honest about the real technical content.

I’m *not* publishing solutions or staff materials. These are my own explanations, diagrams, and mental models. Because these notes follow my understanding, they don’t mirror the official course structure or cover every topic from class.

## Why this exists

Modern AI systems (LLMs, agents, tools) can “hold” way more surface detail than any human.  
But if you don’t understand:

- how data structures and algorithms actually work,
- what the math behind “ML intuition” really is,
- and how to read/criticize a paper,

then AI looks like a black box that replaces you instead of a tool you can direct.

**geshu-compendium** is my attempt to:

- write CS/algorithms notes that don’t assume you’re already good at CS,
- connect course content to practical problem-solving (e.g., LeetCode, systems, industry),
- track my learning as I read papers and revisit math.

If it helps other people along the way, even better.

## What’s inside

The content is split into a few top-level sections (mirrored in the website navigation):

### 📚 Course Notes

- **CS61B – Data Structures**  
  Intuition → invariants → complexity → “how this shows up in interviews and real systems”.  
  Arrays, lists, trees, hashmaps, graphs, etc.

- **CS170 – Efficient Algorithms**  
  Proof patterns, DP/greedy/flows, reductions, and how these ideas map to typical problem sets / LeetCode-style questions.

- **CS194 – Advanced Algorithms / Networks**  
  Graph/network algorithms beyond the basics, cut/flow, spectral-style thinking, and how to reason about networks at scale.

- **CMU 15-850(C) – Algorithms in the Real World**  
  Approximation, streaming, large-scale graphs, and the “systems view” of algorithms.

### 🧮 Resources – Math / ML Prereqs

Short refreshers for people who are **not** math majors but need the tools:

- Linear algebra for ML  
- Probability / random variables  
- Optimization basics  
- Notes tied to things like “Math for Machine Learning” and similar resources

The idea: if you vaguely remember these topics but forgot the details, you can quickly rebuild the mental model.

### 📝 Blog – Paper Notes

Very short writeups on papers I’m reading:

- key ideas in plain language  
- what I found interesting or weird  
- what I don’t fully understand yet  
- one possible extension or question, even if it’s naive

**I’m not pretending to be an expert; this is a record of my own learning process.**

## How to use this

- **Starting from zero?**  
  Jump into the Course Notes section and treat it like lecture + discussion notes, not a textbook. I try to start from intuition and work up to formalism, not the other way around.

- **Brushing up for interviews / research / work?**  
  Use the CS61B/CS170 pages + math refreshers as “recalibration” tools — remind yourself *why* things work, not just how to code them.

- **Reading papers?**  
  Check the blog for quick takes, or use it as an example of how to write your own reading notes.

## License & academic integrity

- **No official solutions.**  
  I don’t publish homework, exam, or project solutions, or material that belongs to instructors.

- **All explanations are my own words.**  
  If something accidentally looks too close to an official handout or book, that’s a mistake, not the goal.

- **If you’re an instructor / TA and see a problem:**  
  Open an issue or contact me, and I’ll remove or edit content as needed.

Content is provided **as-is** for learning and discussion, not for commercial use.


## Website

This repo is designed to build into a small documentation site (via MkDocs + GitHub Pages).

Once deployed, it will be available at:

> [geshu-compendium](https://angelawurx.github.io/geshu-compendium/)


## Status

This is very much a work-in-progress:

- ✅ Skeleton and basic structure  
- 🚧 Migrating/cleaning existing notes from Obsidian  
- 🚧 Adding more math prereq pages  
- 🚧 Writing more paper notes

Expect gaps, TODOs, and rough edges — this is a living notebook, not a polished textbook.
