scenes = [
 ("SC01","A Promise at the Grave","Act I","00:00","02:00",1,10,"GRAVE RIDGE","Night/Dusk"),
 ("SC02","The Princess Who Stayed","Act I","02:00","04:00",11,20,"PINE TRAIL / GRAVE RIDGE","Day"),
 ("SC03","A King Chooses Restraint","Act I","04:00","06:00",21,30,"CASTLE - HALL","Day"),
 ("SC04","Three Small Acts of Kindness","Act I","06:00","08:00",31,40,"GRAVE RIDGE","Day x3"),
 ("SC05","A Price on Compassion","Act II","08:00","09:36",41,48,"QUARRY CAMP / PINE TRAIL","Day"),
 ("SC06","The Ambush","Act II","09:36","12:00",49,60,"PINE TRAIL -> QUARRY CAMP","Late afternoon"),
 ("SC07","The Ransom and the March","Act II","12:00","14:00",61,70,"CASTLE / PINE TRAIL","Dusk"),
 ("SC08","Her Cry, His Mother's Farewell","Act II","14:00","18:00",71,90,"QUARRY CAMP / RAVINE / GRAVE RIDGE","Night"),
 ("SC09","Strength Without Cruelty","Act III","18:00","22:00",91,110,"QUARRY CAMP","Night"),
 ("SC10","Love Before the Miracle","Act III","22:00","24:00",111,120,"QUARRY CAMP","Night"),
 ("SC11","A Father Learns to See","Act IV","24:00","26:24",121,132,"RIVER BANK","Dawn"),
 ("SC12","A Love Carried Forward","Act IV","26:24","28:00",133,140,"CASTLE COURTYARD / GRAVE RIDGE","Day"),
]
def s(t):
    m,sec=t.split(":"); return int(m)*60+int(sec)
def f(x):
    return f"{x//60:02d}:{x%60:02d}"
SHOT=12
print("=== TIMING VERIFICATION ===")
ok=True; prev=0; total_shots=0
for sc,title,act,a,b,s1,s2,loc,tod in scenes:
    dur=s(b)-s(a); n=s2-s1+1; calc=n*SHOT
    match = "OK " if dur==calc else "MISMATCH"
    cont  = "OK " if s(a)==prev else "GAP!"
    if dur!=calc or s(a)!=prev: ok=False
    print(f"{sc} {title[:30]:32s} {a}-{b}  dur={dur:4d}s  shots={n:2d}x12={calc:4d}s  [{match}] [contig {cont}]")
    prev=s(b); total_shots+=n
print(f"\nTotal shots: {total_shots}   Total runtime: {total_shots*SHOT}s = {f(total_shots*SHOT)}")
print(f"ALL CHECKS PASS: {ok and total_shots==140 and total_shots*SHOT==1680}")

# ---- generate shot list ----
L=[]
L.append("# Shot List — THE MOTHER'S MONSTER: PART 2\n")
L.append("> Auto-generated scaffold from Production Draft v03.")
L.append("> **140 editorial shots x 12s = 1,680s = 28:00.** Timing verified — see `make-shotlist.py`.\n")
L.append("## Summary\n")
L.append("| Scene | Title | Act | In | Out | Shots | Dur | Primary location | Time of day |")
L.append("|---|---|---|---|---|---|---|---|---|")
for sc,title,act,a,b,s1,s2,loc,tod in scenes:
    n=s2-s1+1
    L.append(f"| {sc} | {title} | {act} | {a} | {b} | SH{s1:03d}–SH{s2:03d} ({n}) | {f(n*SHOT)} | {loc} | {tod} |")
L.append(f"| | **TOTAL** | | 00:00 | 28:00 | **140** | **28:00** | | |\n")
L.append("---\n")
L.append("## Status legend\n")
L.append("`⬜ not started` · `🟨 frame rendered` · `🟦 frame approved` · `🟩 clip rendered` · `✅ clip approved`\n")
L.append("> **Scene frame first, then video.** Compose ONE completed scene frame per shot from the")
L.append("> approved character references + the named background-master state, then feed that single")
L.append("> frame to image-to-video. Never request a fresh unrelated background per clip.\n")
L.append("---\n")
for sc,title,act,a,b,s1,s2,loc,tod in scenes:
    n=s2-s1+1
    L.append(f"## {sc} — {title}\n")
    L.append(f"**{act}** · `{a}–{b}` · {n} shots · **{loc}** · {tod}\n")
    L.append("| Shot | In | Out | Size | Move | Subject / Action | Dialogue / SFX | BG master state | Frame | Clip |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    t=s(a)
    for i in range(s1,s2+1):
        L.append(f"| **SH{i:03d}** | {f(t)} | {f(t+SHOT)} |  |  |  |  |  | ⬜ | ⬜ |")
        t+=SHOT
    L.append("")
    L.append(f"**VFX / notes:** \n")
    L.append("---\n")
open("production/shot-list.md","w").write("\n".join(L))
print("\nWrote production/shot-list.md")
