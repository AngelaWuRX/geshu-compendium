# geshu-compendium

[![deploy](https://github.com/AngelaWuRX/geshu-compendium/actions/workflows/deploy.yml/badge.svg)](https://github.com/AngelaWuRX/geshu-compendium/actions/workflows/deploy.yml)

> Notes, experiments, and production patterns for building fullstack AI systems.

A documentation site built from private Obsidian vaults. Notes are filed by
engineering capability rather than by course, and every note has to answer the
same three questions: **what problem does this solve, how do I build it, and how
does it fail in production?**

**Live:** <https://angelawurx.github.io/geshu-compendium/>

The full design document — what the site is for, the content model, and the
reasoning behind the structure — is in [DESIGN.md](DESIGN.md). This file covers
how to run and contribute to it.

---

## Quickstart

Requires Python 3.12 (matching CI).

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

.venv/bin/mkdocs serve            # http://127.0.0.1:8000/geshu-compendium/
.venv/bin/mkdocs build --strict   # what CI runs; must stay green
```

`--strict`, combined with the `validation:` block in `mkdocs.yml`, turns a
broken internal link or a page missing from the nav into a failed build rather
than a silently broken site.

---

## Repository layout

```text
docs/                     Site content (the MkDocs source)
  index.md                Home
  learn/                  Five reading paths — order, not filing
  notes/
    foundations/  frontend/  backend/
    data/  ai-engineering/  production/     hand-written, by capability
    data-structures/  algorithms/
    machine-learning/  networks/            generated, published as Reference
  labs/  projects/  build-logs/  postmortems/
  now.md  changelog.md
  _templates/             Authoring templates; excluded from the build

frontend/                 Everything about how the site looks
  overrides/              theme.custom_dir — templates + the design system

backend/                  What the site will run on (not yet wired up)
  app/  agents/           HTTP surface and agent code
  data/vaults/            The private Obsidian vaults — gitignored

scripts/
  sync_vault.py           Vault -> docs/ converter
  vault_manifest.toml     Publish policy: what ships, what never does
  test_sync_vault.py      45 tests
```

Two directories carry their own README with more detail:
[`frontend/`](frontend/README.md) and [`backend/`](backend/README.md).

---

## Two taxonomies, crossed on purpose

This is the one structural idea worth understanding before editing anything.

- **Capability = folder.** `docs/notes/<capability>/` is *where a note belongs*,
  by the engineering capability it teaches.
- **Learn path = sequence.** `docs/learn/` is *what order to read in*. A path
  owns no pages and crosses folders freely.

So "Database transactions" is filed under `notes/data/` but appears third in the
Foundations path. Filing and reading order are different questions, and the site
answers both rather than compromising on one.

---

## Content types

Not everything is a "note". The `type:` frontmatter key distinguishes them.
There are five templates in `docs/_templates/` for six types — `concept` and
`pattern` share `note.md`, because they differ in what they explain, not in how
the page is shaped.

| Type | What it is |
|---|---|
| `concept` | Explains a model — how HTTP streaming works, what an embedding represents |
| `pattern` | Solves a recurring engineering problem — idempotent webhooks, hybrid retrieval |
| `lab` | A runnable experiment you change and re-run |
| `build-log` | What happened while building, wrong turns kept in |
| `postmortem` | An incident, written up properly |
| `project` | A built thing, linked back to the notes it exercises |

---

## Writing a note

Copy a template, fill it in, add one line to `nav:` in `mkdocs.yml`.

```sh
cp docs/_templates/note.md docs/notes/backend/rate-limiting.md
```

Every formal note follows the same nine sections. The order is deliberate: the
problem comes before the definition, and **What Breaks** is the section that
separates this from a tutorial.

```text
1. The Problem          5. Production Version    9. References
2. Mental Model         6. Live Lab
3. Minimal Build        7. Build Challenge
4. What Breaks          8. Decision Record
```

### Frontmatter

```yaml
title: Background Jobs and Idempotency
summary: Accepting work you cannot finish inside a request, exactly once.
type: pattern            # concept | pattern | lab | build-log | postmortem | project
status: seed             # seed | working | stable | production-tested
difficulty: intermediate # beginner | intermediate | advanced
topics: [queues, reliability, idempotency]
course_sources: [distributed-systems]
projects: [postmortem-agent]
runtime: [python, postgresql]
last_tested:             # YYYY-MM-DD; blank means never
tags: [topic/queues]     # drives the colour-coded facets
```

`topics` is the source of truth for what a note is about. `tags` exists only to
render the facet chips, so mirror across the ones worth showing and leave the
rest out — one authoritative key, not two.

### Status

Rendered above the title of every note by
`frontend/overrides/partials/note-meta.html`.

| Status | Means |
|---|---|
| `seed` | A problem statement and scattered thinking. Not yet worth reading. |
| `working` | Explanation and code exist, and may still change. |
| `stable` | Accurate enough to rely on. |
| `production-tested` | Runs in a real project, with tests or monitoring behind it. |

A note that declares a `runtime` but no `last_tested` renders **never**. That is
deliberate: code that has never been run is exactly what a reader wants flagged.

The strip is gated on `status`, so pages without it — index pages and every
generated note — render as if the partial did not exist.

---

## How generated content is published

The `Reference` section is **not** hand-edited. Its 57 pages are produced by
`scripts/sync_vault.py` from private Obsidian vaults, and every one carries an
`AUTOGENERATED` marker at the top.

```sh
python3 scripts/sync_vault.py --check    # report drift, write nothing
python3 scripts/sync_vault.py            # regenerate + rewrite the nav block
python3 -m pytest scripts/test_sync_vault.py -q
```

The converter resolves wikilinks, converts Obsidian callouts to admonitions,
copies embedded images, strips sections named in the manifest, and rewrites the
nav between the `BEGIN/END GENERATED NAV` sentinels in `mkdocs.yml`.

**Editing a generated page is pointless** — the next sync overwrites it. Edit
the vault note and re-run. Conversely, hand-written pages are never touched:
the cleanup pass only deletes files carrying the provenance marker, which is
what lets `notes/foundations/` and `notes/networks/` live side by side.

---

## Privacy model

The vaults contain staff solution sets, lecture material, copyrighted books and
personal documents. None of it can reach the site, and that is enforced in three
independent places rather than by care alone.

1. **`.gitignore`** — `/backend/data/vaults/` never enters the repository, plus
   blanket rules for `*.pdf`, `*.tex`, `*solution*`, `[Rr]esume*`.
2. **`scripts/vault_manifest.toml`** — the publish policy. Sections use explicit
   per-file include lists, not directory globs. The `[denylist]` is a hard gate:
   one hit aborts the entire run and writes nothing. `fail_patterns` are checked
   against every rendered byte, and a hit reports the file and line but never
   the matched text — printing it would copy the thing being protected into CI
   logs.
3. **`.github/workflows/deploy.yml`** — greps the committed tree for denied
   paths and private-info patterns, and fails the build on a match.

If you add a section to the manifest, run `sync_vault.py --check` first and read
what it reports before letting it write.

---

## Deployment

Push to `main`. The workflow installs pinned dependencies, runs the privacy
guard, builds with `--strict`, and publishes via `mkdocs gh-deploy`.

GitHub Pages serves static files only, which is the constraint the `backend/`
directory is designed around — see [`backend/README.md`](backend/README.md) for
what that implies for anything interactive.

---

## Current state

Honest, because the site itself claims to be:

- **Built** — the capability map, five Learn paths, the status system, content
  templates, and the vault pipeline with 57 generated pages.
- **Seeded** — the twelve first notes exist as stubs with a real problem
  statement and a `What Breaks` list, and nothing else.
- **Empty** — Labs, Build Logs and Postmortems have templates but no entries.
  The AI Infrastructure path lists what is planned and says it is empty.
- **Not started** — filtering by status or runtime, browser-runtime labs, the
  backend service, and any AI assistant over the notes. Ordinary search comes
  first; a chat box over a corpus you cannot search hides the problem instead of
  fixing it.

---

## Licence

Notes are [CC BY-NC-SA 4.0](LICENSE-CONTENT); the site's code is
[MIT](LICENSE).

If you are an instructor or TA and something here should not be public, open an
issue and it will be removed.
