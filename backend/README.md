# backend/

Everything the site *runs on*: the content store, and the agent systems the
frontend calls. Nothing in here is served directly — the frontend talks to it
over HTTP.

```
backend/
  app/        <- HTTP surface the frontend calls (routes, schemas, auth)
  agents/     <- agent systems: prompts, tools, orchestration, evals
  data/       <- the dataset: three Obsidian vaults + the publish policy
    vaults/   <- gitignored; see data/README.md
  README.md
```

`app/` and `agents/` are **tracked**. Only `data/vaults/` is gitignored —
ignoring the code would mean no version control on it, which is not the same
thing as keeping it private. If the backend needs to be private *and*
versioned, that is a separate private repo, not an ignore rule.

## Why this folder exists

Today the site is a static MkDocs build: `scripts/sync_vault.py` converts two
private Obsidian vaults into `docs/`, `mkdocs build` renders it, and GitHub
Pages serves the result. That has no place to put state and no place to run
code, so anything interactive — an agent answering questions about the notes,
a generated daily log, search that isn't a client-side index — has nowhere to
live. This is that place.

## The constraint to design around

**GitHub Pages serves static files only.** It cannot host this. The moment the
frontend calls a backend, the site needs a second deploy target (a small always-on
host, or serverless functions) and a CORS/origin story between the two. That is
the real cost of the split, and it should be paid deliberately — not discovered
after the code is written.

## Privacy rules carry over

`data/` holds the source vaults, so the existing guards now apply here too —
see [`data/README.md`](data/README.md) for the full picture:

- the vaults are gitignored (`/backend/data/vaults/`) and never reach CI;
  `scripts/vault_manifest.toml` is the publish policy
- `.github/workflows/deploy.yml` greps the tree for private-info patterns and
  fails the build on a hit — that grep now covers `backend/` as well as `docs/`
- the postmortem-agent material is hand-scrubbed; its private source
  (`data/vaults/python/learning/System Design (DDIA)/`) is denylisted so no
  future include glob can reach it

## Decided

**The frontend stays MkDocs.** The site keeps building to static HTML on GitHub
Pages exactly as it does now. Interactivity arrives as a small client in
`frontend/overrides/javascripts/` that `fetch()`es this backend. The 57 generated pages,
the design system, LaTeX, tag facets and CJK search all keep working untouched.

**The first agent writes the daily work-log.** It reads the day's git activity
and vault changes and drafts the entry.

### What that combination implies

A static site cannot be written to at request time, so the log agent's output
**lands as a commit, not as a database row**: agent drafts → human reviews →
markdown is committed to `docs/` → the existing deploy workflow rebuilds the
site. Git is the publish path.

Which means the frontend JS layer is *not* rendering the log — MkDocs already
does. It exists to **trigger a draft and review one**. Keep that boundary
sharp; blurring it is how this turns into the rewrite we just decided against.

## Still open

1. **What runs the API** — FastAPI is the default (repo is Python 3.12, and
   `scripts/` is already Python). Nothing yet argues against it.
2. **Where the draft lives before it's committed** — SQLite in `data/` is
   enough for one author. The notes themselves stay files in git.
3. **Where the backend is hosted**, and whether the review UI is public at all.
   If review is author-only, the backend can stay local and the whole hosting
   question goes away for now — worth considering before paying for a host.
4. **How a draft is evaluated.** "The agent wrote something" is not the bar;
   define what a good entry looks like before generating one.
