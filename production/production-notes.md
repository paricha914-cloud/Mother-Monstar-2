# Production Notes — THE MOTHER'S MONSTER: PART 2

## Format

| | |
|---|---|
| **Title** | The Mother's Monster: Part 2 |
| **Draft** | Production Draft v03 |
| **Language** | English |
| **Genre** | Dark fantasy / romantic fantasy |
| **Runtime** | **28:00** (1,680s) |
| **Structure** | 4 acts · 12 scenes · **140 editorial shots** |
| **Shot length** | 12s planning target |
| **Method** | AI-generated visuals + synthetic voices |

### ✅ Timing verified

Re-run any time with `python3 production/make-shotlist.py`:

```
SC01  00:00-02:00   10 shots x 12s = 120s   OK
SC02  02:00-04:00   10 shots x 12s = 120s   OK
SC03  04:00-06:00   10 shots x 12s = 120s   OK
SC04  06:00-08:00   10 shots x 12s = 120s   OK
SC05  08:00-09:36    8 shots x 12s =  96s   OK
SC06  09:36-12:00   12 shots x 12s = 144s   OK
SC07  12:00-14:00   10 shots x 12s = 120s   OK
SC08  14:00-18:00   20 shots x 12s = 240s   OK
SC09  18:00-22:00   20 shots x 12s = 240s   OK
SC10  22:00-24:00   10 shots x 12s = 120s   OK
SC11  24:00-26:24   12 shots x 12s = 144s   OK
SC12  26:24-28:00    8 shots x 12s =  96s   OK
──────────────────────────────────────────────
TOTAL              140 shots      = 1,680s = 28:00
No gaps, no overlaps, no mismatches.
```

> ⚠️ 12s is a **planning target**, not a promise that every provider offers a 12-second setting.
> If your provider caps shorter, re-run the script with a different `SHOT` value and the whole
> plan re-times automatically.

---

## ⚠️ Production safeguards

> From Draft v03. These exist to stop AI drift from destroying continuity.

### 1. Background masters are mandatory inputs
Every scene frame must be composed from an approved **background master in its named state**.
**Never** request a fresh unrelated background per clip. See [`world/locations.md`](../world/locations.md)
for every location and its named states.

### 2. One completed scene frame per clip
For a simple image-to-video tool, upload **ONE completed scene frame** — not separate
portraits plus an empty background.

```
approved character refs  ┐
                         ├──→  ONE composed scene frame  ──→  image-to-video  ──→  clip
named background state   ┘
```

### 3. Prototype batch
The **first five scene frames** are the initial prototype batch. The remaining **135** still
need rendering and approval.

### 4. Drift is expected — review and reject
A text-only generator **cannot** be forced to reproduce the same face and geography exactly.
Model drift remains possible even with reference input. **Review every take and reject wrong ones.**

### 5. The transformation is a match cut, not a morph
SC10: white-gold light transition + **match cut** from an approved dragon frame to an
approved, fully clothed human frame. **Do not** let a generic model invent the human face
during a long morph.

### 6. The camp destruction is a state change, not a simulation
SC09: cut from controlled fire **to the prebuilt scorched background state**. Do not ask one
clip to simulate an entire collapsing camp.

### 7. No readable generated text
The King's illustrated book (SC03): closed, angled, shallow-focus, or illustration-only
inserts. **No readable AI-generated page text.**

### 8. Break action into readable beats
SC06 and SC09 especially: single readable beats per shot, **not one overloaded generation.**

---

## Fixed cast — ⚠️ approved references, do not redesign

| Character | Reference | Speaking |
|---|---|---|
| **Ember — dragon** | approved | ✅ (see continuity R1) |
| **Ember — human** | approved · ivory tunic + dusty-rose cloak | ✅ |
| **Elara — human** | approved | ✅ memory |
| **Elara — spirit** | approved · same face & clothes | ✅ SC08 |
| **Aurelia** | approved | ✅ |
| **The King** | approved | ✅ |
| **Royal Captain** | approved | ✅ |
| **Bandit leader** | approved | ✅ |
| **Bandit scout** | approved | minimal |
| **Bandit enforcer** | approved | minimal |
| **Royal-knight uniform** | approved | ❌ background only |

**Rules**
- **No new speaking characters.**
- Knights are background adults with **varied faces and fixed uniforms**.
- **Same voice actor for both forms of Ember.**
- Keep approved outfits through the simple wedding — **no new costume redesign.**

---

## Voice cast

| Character | Voice | Lines | Status |
|---|---|---|---|
| Ember (both forms) | **same actor for both** | SC01, 08, 09, 10, 11, 12 | ⬜ |
| Aurelia | | SC02, 03, 04, 06, 08, 10, 11 | ⬜ |
| Elara | | SC01 (memory), SC08 (spirit) | ⬜ |
| The King | | SC03, 07, 11 | ⬜ |
| Royal Captain | | SC09, 11 | ⬜ |
| Bandit leader | | SC05, 06, 09 | ⬜ |
| Bandit scout / enforcer | | minimal | ⬜ |

---

## Pipeline

| Stage | Status |
|---|---|
| Story treatment v03 | ✅ Locked for review |
| Continuity check vs. Part 1 | ✅ Done — **2 red items need your decision** |
| Shot list scaffold (140) | ✅ Generated |
| Shot descriptions | ⬜ 0 / 140 |
| Screenplay (Fountain) | ⬜ Draft 0 |
| Background masters + named states | ⬜ |
| Scene frames — prototype batch | ⬜ 0 / 5 |
| Scene frames — remainder | ⬜ 0 / 135 |
| Image-to-video clips | ⬜ 0 / 140 |
| Voice / dialogue | ⬜ |
| Edit | ⬜ |
| Sound & score | ⬜ |
| Colour | ⬜ |

---

## Open decisions

See [`reference/continuity-check.md`](../reference/continuity-check.md) for the full checklist.

| # | Decision | Priority |
|---|---|---|
| 1 | Does dragon-Ember speak aloud, or is every line `(V.O.)`? | 🔴 |
| 2 | Is the burned village visible in your Part 1 cut? | 🔴 |
| 3 | Lock the grave slugline — "valley" or "ridge" | 🟡 |
| 4 | Headstone origin | 🟡 |
| 5 | Account for Marta / Father Elden / Ram | 🟡 |
| 6 | Time gap since Part 1 | 🟡 |
| 7 | Was Part 1's village inside this kingdom? | 🟡 |
