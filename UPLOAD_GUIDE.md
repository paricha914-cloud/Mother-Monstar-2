# How to get your files into this repo

> **তোমার file গুলো আমার কাছে কীভাবে পাঠাবে**

Chat-e attach kora file gulo amar sandbox-e **pouchacche na** (platform-er ekta limitation).
Image gulo ami chat-e **dekhte pari**, kintu `.json` / `.txt` / `.csv` / `.md` file gulo
ami **dekhteo pari na**. Tai nicher upay gulo.

---

# 🟢 METHOD A — GitHub website, drag & drop

**Kono software lagbe na. Shobcheye soja. Eta use koro.**

### Step 1 — Repo-te jao, branch bodlao

Open: **https://github.com/paricha914-cloud/Mother-Monstar-2**

Upore-bame ekta dropdown button ache jekhane lekha **`main`**.
Setay click kore **`arena/01a10062-mother-monstar-2`** select koro.

> ⚠️ **Eta shobcheye important step.** Ei branch-e na dile ami file gulo pabo na.

### Step 2 — Folder-e dhoko

Je folder-e file rakhbe setar upor click koro:

| Ki upload korcho | Kon folder |
|---|---|
| Character reference | `assets/characters` |
| Background master | `assets/backgrounds` |
| Storyboard sheet (B01–B12) | `assets/storyboards` |
| manifest / prompt / csv | `reference/source-files` |

### Step 3 — Upload

Upore-dane সবুজ **`Add file ▾`** button → **`Upload files`**

Tarpor file gulo **drag kore chere dao** (ekshathe onek gulo dile-o cholbe).

### Step 4 — Commit

Niche **`Commit changes`** button-e click koro.

> Jodi "Create a new branch" option dekhay — **NA**. *"Commit directly to the
> `arena/01a10062-mother-monstar-2` branch"* select koro.

### Step 5 — Amake bolo

Chat-e likho **"upload done"**. Ami `git pull` kore shob file-e link kore debo.

---

## 🔗 Direct upload links

Branch select kora obosthay ei link gulo shoja upload page khulbe:

| Folder | Link |
|---|---|
| Characters | https://github.com/paricha914-cloud/Mother-Monstar-2/upload/arena/01a10062-mother-monstar-2/assets/characters |
| Backgrounds | https://github.com/paricha914-cloud/Mother-Monstar-2/upload/arena/01a10062-mother-monstar-2/assets/backgrounds |
| Storyboards | https://github.com/paricha914-cloud/Mother-Monstar-2/upload/arena/01a10062-mother-monstar-2/assets/storyboards |
| Source files | https://github.com/paricha914-cloud/Mother-Monstar-2/upload/arena/01a10062-mother-monstar-2/reference/source-files |

---

# 🟡 METHOD B — GitHub Desktop

Command line bhoy lagle eta bhalo.

1. **GitHub Desktop** install koro → https://desktop.github.com
2. `File` → `Clone repository` → `Mother-Monstar-2`
3. Upore **`Current branch`** → **`arena/01a10062-mother-monstar-2`** select koro
4. Computer-e folder-ta khulo, file gulo thik folder-e copy koro
5. GitHub Desktop-e ekta message likhe **`Commit to arena/...`**
6. **`Push origin`** click koro

---

# 🔵 METHOD C — Command line

```bash
git clone https://github.com/paricha914-cloud/Mother-Monstar-2.git
cd Mother-Monstar-2
git checkout arena/01a10062-mother-monstar-2

cp /path/to/characters/*.png   assets/characters/
cp /path/to/backgrounds/*.png  assets/backgrounds/
cp /path/to/storyboards/*.png  assets/storyboards/
cp /path/to/character_manifest.json \
   /path/to/IDENTITY_PROMPT_BLOCKS.txt \
   /path/to/CONSISTENCY_LOG_TEMPLATE.csv  reference/source-files/

git add .
git commit -m "Add approved references, backgrounds and storyboards"
git push origin arena/01a10062-mother-monstar-2
```

---

# ⚡ METHOD D — Text file gulor jonno shortcut

`.json` / `.txt` / `.csv` **choto file** — eigulor jonno GitHub-e jawar dorkar nei.
**Shoja chat-e paste kore dao.** Ami nijei repo-te file banie debo.

Othoba ekta **GitHub Gist** banao (https://gist.github.com), shob paste koro,
"Create secret gist" dao, ar **link-ta amake dao** — ami fetch kore porte pari.

---

# 📝 File naming

Je naam-e upload korbe, repo oi naam-ei rakhbe. Consistent naam hole ami automatically
protita character/location file-e link korte parbo.

Protita folder-er bhitore ekta `README.md` ache — **sekhane exact naam-er table deowa ache**.

Already thik naam thakle rename korar dorkar nei — ami adjust kore nebo.

---

# ❓ Problem hole

| Somossa | Ki korbe |
|---|---|
| Branch dropdown-e `arena/...` dekhchi na | Dropdown-er search box-e `arena` likho |
| "Commit directly" option nei | Upper-right-e nijer account logged in ache kina dekho |
| File boro (>25 MB) | GitHub web upload-e 25 MB limit. Method B ba C use koro |
| Onek file ekshathe | Web upload-e 100 file / 25 MB per file limit |
