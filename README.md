# geshu-compendium
> A living notebook for understanding core CS + math ideas deeply enough that AI tools become amplifiers, not replacements.

This repo hosts my personal notes for a small “curriculum”:

- **Networks** – random graphs, branching processes, epidemics, spectral methods  
- **Machine Learning** – probability through transformers, with interview Q&A  
- **Data Structures** – lists, trees, heaps, hashing, sorting  
- **Algorithms** – divide and conquer, LP, reductions, graphs  

Sections appear here when there are notes worth reading in them, not before.

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

### 📚 Notes

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

### 🧮 Resources – Math / ML Prereqs

Short refreshers for people who are **not** math majors but need the tools:
linear algebra, probability, optimisation basics.

### 📝 Blog – Paper Notes

Very short writeups on papers I’m reading: key ideas in plain language, what I
found interesting or weird, what I don’t fully understand yet.

**I’m not pretending to be an expert; this is a record of my own learning process.**

## How to use this

- **Starting from zero?**  
  Begin with **Data Structures**, then **Algorithms**. Treat them like lecture + discussion notes, not a textbook — I start from intuition and work up to formalism, not the other way around.

- **Here for the deep end?**  
  **Networks** is the most developed section: random graphs and the giant component, through epidemics on configuration models.

- **Brushing up for interviews / research / work?**  
  The **Machine Learning** notes end in collapsible Q&A cards — read the question, answer it yourself, then expand.

- **Reading papers?**  
  Check the blog for quick takes, or use it as an example of how to write your own reading notes.

## License & academic integrity

- **No official solutions.**  
  I don’t publish homework, exam, or project solutions, or material that belongs to instructors.

- **All explanations are my own words.**  
  If something accidentally looks too close to an official handout or book, that’s a mistake, not the goal.

- **If you’re an instructor / TA and see a problem:**  
  Open an issue or contact me, and I’ll remove or edit content as needed.

**Licensing.** The prose (everything under `docs/`, plus this README) is
[CC BY-NC-SA 4.0](LICENSE-CONTENT) — share and adapt with attribution, non-commercially,
under the same terms. The code (`mkdocs.yml`, `scripts/`, stylesheets) is [MIT](LICENSE).

The split is deliberate: MIT is a software licence, and applying it to prose
granted the right to *sell* these notes, which contradicted the non-commercial
intent stated right here. It also asks anyone quoting a page to reproduce a
21-line warranty disclaimer — which nobody does, so you get non-compliance
instead of attribution.


## Website

This repo is designed to build into a small documentation site (via MkDocs + GitHub Pages).

Once deployed, it will be available at:

> [geshu-compendium](https://angelawurx.github.io/geshu-compendium/)


## How this is built

The notes are written in Obsidian and live in local vaults that are **not** in
this repo — they hold course PDFs, staff material and personal files that must
never be published. `scripts/sync_vault.py` converts the publishable subset
into `docs/`:

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
git config core.hooksPath scripts/githooks     # once per clone

python3 scripts/sync_vault.py                  # vault -> docs/
python3 scripts/sync_vault.py --check          # report drift, write nothing
.venv/bin/mkdocs serve                         # preview
```

`scripts/vault_manifest.toml` decides what publishes and what never can. The
denylist is a gate, not a filter: the script renders everything, checks every
byte against it, and only then writes — so nothing lands half-done. Pages under
`docs/notes/` are generated; edit the vault note and re-run.

## Status

A living notebook, not a polished textbook — expect gaps and rough edges.

- ✅ Networks — 18 notes, the most complete section  
- ✅ Machine Learning — 11 notes with interview Q&A  
- 🚧 Data Structures / Algorithms — the substantive notes are up; several
     stubs still to write, and the ADT pages want consolidating  
- 🚧 Resources — math prereq pages  
- 🚧 Blog — paper notes
