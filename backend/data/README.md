# backend/data/

The dataset the site is generated from: three Obsidian vaults, plus the policy
that decides which parts of them are allowed to become public pages.

```
backend/data/
  vaults/          <- gitignored. The raw source. Never committed.
    cs/            <- CS61B / CS170 / CS189 notes
    python/        <- hello-algo, ML notes, DDIA track, job-search material
    spring2026/    <- networks + machine_learning coursework
  README.md
```

## What's in it

Measured against the current manifest. "pub" is what `sync_vault.py` actually
emits; "denied" is what the denylist gate refuses to touch.

| vault | iCloud twin | files | size | .md | published | denied |
|---|---|---:|---:|---:|---:|---:|
| `cs` | `Computer Science` | 69 | 6.7 MB | 50 | 26 | 6 |
| `python` | — none — | 98 | 53.2 MB | 54 | 12 | 28 |
| `spring2026` | `spring2026` | 119 | 224.1 MB | 44 | 19 | 77 |
| **total** | | **286** | **283.9 MB** | **148** | **57** | **111** |

**57 of 286 files publish.** By bytes it is far starker: the published output is
under 0.2 MB against 284 MB of source, because 224 MB of `spring2026` is
`networks/lecture_notes/` and `machine_learning/lec/` — staff lecture PDFs that
are denylisted and can never publish by construction.

Nothing here has been pruned. That is deliberate: the vaults are kept whole so
they stay usable as study material, and the denylist — not deletion — is what
keeps the unpublishable parts unpublishable.

## The three guards

They are independent on purpose; each one alone is not enough.

1. **`.gitignore`** ignores `/backend/data/vaults/`. Nothing in here is ever
   tracked, so nothing here can be pushed.
2. **The denylist** in `scripts/vault_manifest.toml` is a *gate*, not a filter.
   A hit anywhere stops the whole run and writes nothing. An include that
   selects a denylisted path raises `PolicyViolation` — a manifest that
   contradicts itself is an error, not a silent skip.
3. **The CI guard** in `.github/workflows/deploy.yml` greps the committed tree
   for vault paths, PDFs, `.tex`, resumes and private-info patterns, and fails
   the build on a hit. It exists because CI never sees the vaults and so cannot
   run `sync_vault.py --check` itself.

## Refreshing from iCloud

`cs` and `spring2026` mirror live Obsidian vaults under
`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/`. The vault's
`icloud` key in the manifest names its twin, and `sync_vault.py` warns when the
copy here is behind it. To refresh, re-copy the vault and re-run the sync.

**`python` has no twin.** It is not in iCloud and exists only at this path — so
it is the one vault with no upstream to recover from. Back it up before doing
anything destructive to it.

## Working on it

```sh
.venv/bin/python scripts/sync_vault.py --check   # report drift, write nothing
.venv/bin/python scripts/sync_vault.py           # regenerate docs/ + nav
.venv/bin/python -m unittest discover scripts    # 45 tests, incl. the policy gate
```

Every generated page under `docs/notes/` carries a provenance marker naming the
vault file it came from. Those files are outputs: edit the vault note and re-run,
never the page.

## A rename cost us this once

These vaults used to sit at the repo root as `<name> copy`. The suffix was
load-bearing — it keyed an `ICLOUD_TWINS` dict inside `sync_vault.py` — and the
`python` vault's own reorganization silently broke its manifest paths. The
result: `sync_vault.py` warned `vault 'python' not found` and would have
**deleted 12 published pages** (the whole Machine Learning section plus the
hello-algo note) on the next run, rewriting the nav to match.

Hence the shape here: directory names match the manifest's `name` field, the
iCloud mapping lives in the manifest rather than in code, and two policy-gate
tests assert against explicit paths that no blanket pattern would catch — so
the next rename fails loudly instead of quietly.
