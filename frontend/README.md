# frontend/

Everything about how the site *looks* lives here. Content is generated into
`docs/notes/` by `scripts/sync_vault.py` and must never be edited for
presentation reasons.

```
frontend/
  overrides/                  <- mkdocs.yml: theme.custom_dir
    main.html                 <- extends Material's base.html (head-level tweaks)
    partials/tags.html        <- adds data-md-tag so tag facets can be colour-coded
    stylesheets/extra.css     <- the whole design system
  README.md
```

## How it is wired

- `mkdocs.yml` sets `theme.custom_dir: frontend/overrides`. Besides enabling
  the two template overrides, MkDocs copies every non-HTML file in the
  custom dir into the built site — that is how
  `overrides/stylesheets/extra.css` ends up at `stylesheets/extra.css`,
  which is what `extra_css` points at. (This is also why the stylesheet
  lives *inside* `overrides/` rather than a sibling `styles/` folder:
  files outside the custom dir or `docs/` never reach the site.)
- `theme.palette` uses `primary: custom` / `accent: custom`, which tells
  Material to emit no colours of its own; both schemes are defined entirely
  in `extra.css`.
- `theme.font: false` disables Material's default Google-Fonts request for
  Roboto. The stylesheet uses system font stacks (with explicit CJK
  families for the Chinese prose), so readers make no font requests at all.

## The palette

Ported from the author's Obsidian snippet
(`spring2026 copy/.obsidian/snippets/networks-ui.css`) — that file is the
source of truth for the site's visual identity. Every colour is a `--gx-*`
token declared twice, once per scheme, at the top of `extra.css`; Material's
`--md-*` variables are mapped onto the tokens right below. To retune the
palette, edit only those two blocks.

Tag facets are colour-coded like the vault: `area/` teal, `method/` blue,
`model/` gold, `topic/` pink. Light-mode variants keep the hue but are
darkened to hold WCAG AA (all tag/text colours were checked at >= 4.5:1;
body text is ~14:1 in both schemes). Stock Material renders tags with
nothing to select on, so `partials/tags.html` adds a `data-md-tag`
attribute — to add a new facet, add one line in the tags section of
`extra.css`.

## How to preview

```sh
.venv/bin/mkdocs serve          # live-reloads on frontend/ changes too
.venv/bin/mkdocs build --strict # what CI runs; must stay green
```

Check any change against:

- `notes/networks/06-giant-component/` — dense maths, tags, tables
- `notes/machine-learning/09-transformers-and-attention/` — Q&A cards
- `notes/data-structures/asymptotic/` — Chinese prose, wide table, `==mark==`
- a ~360 px viewport — tables, display equations and long inline formulas
  must scroll inside their own boxes; the page body must never scroll
  sideways
- both themes — the toggle must look right in each direction

## External requests

Exactly one, which predates this folder: MathJax from `unpkg.com`
(`extra_javascript` in mkdocs.yml). `main.html` adds a `preconnect` hint for
it; if the CDN is unreachable the page still renders, just with raw LaTeX.
This redesign *removed* a request (Google Fonts) and added none — no
analytics, no tracking, no webfonts.

## Upgrading mkdocs-material

`partials/tags.html` is a copy of the stock partial (9.6.x) plus one
attribute. After a Material upgrade, re-diff it against
`.venv/lib/python*/site-packages/material/templates/partials/tags.html`.
Everything in `extra.css` targets stable Material selectors and CSS
variables, but a quick pass over the checklist above after upgrades is
cheap insurance.
