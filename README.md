# Surveillance Detection Lab — AP Cybersecurity Unit 2, Period 9

**Unit 2: Securing Spaces · LO 2.A, 2.D, 3.D**
**Time:** one 45-minute period

Building A has been broken into. The incident happened, and now it is your job
to work out what actually occurred from the evidence that survived.

This lab runs in the **VS Code server**. You will analyze data, not write code.
The grading gate checks that you reasoned correctly from the evidence.

---

## What you will do

1. Work through the incident evidence in `incident-data/`.
2. Reconstruct a timeline of what happened.
3. Determine which detection controls would have caught it, and which would not.
4. Recommend a revised sensor plan for the building.
5. Open a **Pull Request** from your fork containing your findings, and open an
   **Issue** describing the one change you would make first.

**This lab is your first Pull Request.** Read the PR section below carefully —
budget your time and get something submitted even if incomplete.

## How to work in this repo

Do not use Codespaces. Use the **VS Code server** at `vscode.ivycollegiate.org`.

1. **Fork** this repository to your own GitHub account.
2. In the VS Code server terminal, clone your fork:

   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/surveillance-detection-lab.git
   cd surveillance-detection-lab
   ```

3. Read the evidence files, then edit `incident-report.md`.
4. Commit, push, and open a Pull Request:

   ```bash
   git add incident-report.md
   git commit -m "Complete surveillance detection analysis"
   git push
   ```

   Then open the PR in the GitHub web interface (or with the
   Pull Requests extension in VS Code).

## If you get stuck on git

If a push is rejected or you hit a conflict, this is the recovery:

```bash
git pull --rebase origin main
# resolve any conflict in audit-report.md, then:
git add incident-report.md
git rebase --continue
git push
```

If git is still fighting you, submit your work as an **Issue** instead and tell
your teacher. A correct analysis submitted as an Issue earns more than a
broken pull request. Do not burn the period debugging git.

---

## The incident

A laptop was taken from the Building A staff room overnight. The badge log
contains a swipe that is almost certainly not the owner's. The building has six
cameras, one of which has not worked since June, and a 7-day badge log
retention policy.

Your job is to work out what the evidence can and cannot tell you.

## Control categories

When you evaluate a detection control, classify it:

| Code | Control | Question it answers |
|---|---|---|
| `MOTION` | Motion sensor | Did anything move here? |
| `THERMAL` | Thermal / heat sensor | Is something present that should not be? |
| `ACOUSTIC` | Acoustic / glass-break sensor | Was a door or window forced? |
| `ACCESS` | Badge / door controller | Who was authorized, and when? |
| `VIDEO` | Camera | Can we see what happened? |
| `ALARM` | Audible alarm | Would anyone have noticed? |

## Evidence grading

Some evidence in `incident-data/` is reliable and some is not. For every claim
you make, state how confident you are:

- `CONFIRMED` — the data directly shows it.
- `INFERRED` — supported by evidence, but not directly stated.
- `SPECULATIVE` — plausible, not enough evidence to assert.

This is the part that is graded hardest. A confident wrong answer scores worse
than a well-hedged right one.

## The gate

The 🤖 `surveillance-gate` Action runs on your Pull Request:

- **Green check** = the report is complete and the timeline is internally consistent.
- **Red X** = something is missing, or your timeline contradicts your evidence.
  The Action log tells you exactly which.
- `python3 scripts/check_report.py --selftest` proves the blank template fails.

## Rules

- Every timeline entry must cite a specific file in `incident-data/`.
- Do not claim the badge log shows who was on site. It shows badge IDs.
- "The camera would have caught it" is a claim about coverage. Name the camera
  and prove it covers the location, or do not make the claim.
