# MOTHER MONSTAR

> An English-language fantasy film — in development.

This repository is the **production hub** for the film: story, screenplay, characters,
world-building, concept art and production planning all live here, version-controlled.

---

## Status

| Area | State |
|---|---|
| Logline | ⬜ To be filled |
| Synopsis | ⬜ To be filled |
| Treatment / Outline | ⬜ To be filled |
| Screenplay | ⬜ Draft 0 |
| Characters | ⬜ To be imported |
| World bible | ⬜ To be filled |
| Concept art | ⬜ To be imported |
| Poster | ⬜ Not started |

---

## Repository map

```
.
├── story/                  The narrative core
│   ├── logline.md          One-sentence pitch
│   ├── synopsis.md         1–2 page story summary
│   ├── treatment.md        Full beat-by-beat outline (3 acts)
│   └── themes.md           Themes, tone, visual language
│
├── world/
│   ├── world-bible.md      Setting, rules of magic, history, factions
│   └── locations.md        Every location in the film
│
├── characters/
│   ├── index.md            Cast list at a glance
│   └── _template.md        Copy this for each new character
│
├── script/
│   └── mother-monstar.fountain    Screenplay (Fountain format — plain text, Git-friendly)
│
├── production/
│   ├── shot-list.md        Scene → shots breakdown
│   ├── storyboard.md       Panel descriptions / links to boards
│   └── production-notes.md Schedule, cast, crew, budget notes
│
├── assets/
│   ├── characters/         Character art  (e.g. 01-name.png)
│   ├── concept-art/        Mood & key frames
│   ├── locations/          Environment art
│   └── posters/            Poster / key art
│
└── reference/              Inspiration, mood boards, research
```

---

## Why Fountain for the screenplay?

[Fountain](https://fountain.io) is plain-text screenplay markup. It is readable as-is,
diffs cleanly in Git, and exports to industry-standard PDF/Final Draft from
free tools (Highland, Slugline, Afterwriting, `screenplain`).

```fountain
INT. THE HOLLOW CATHEDRAL - NIGHT

She steps into the light. It does not warm her.

ELARA
I was never your daughter.
```

---

## Working with this repo

- Drop character images into `assets/characters/` and reference them from each
  character's markdown file.
- Each character gets its own file: `characters/elara.md`, etc.
- Keep large video/render files **out of Git** (see `.gitignore`) or use Git LFS.
