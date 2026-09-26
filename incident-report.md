# Surveillance Detection Analysis — Building A Break-In

**Analyst:** Test Student
**Date:** 2026-10-09
**Incident:** Laptop theft from staff room, overnight 2026-09-28 → 2026-09-29

---

## 1. Summary

Two or three sentences. What do the evidence actually support?

---

## 2. Timeline

Every entry must cite a specific file in `incident-data/`. Every entry must be
marked `CONFIRMED`, `INFERRED`, or `SPECULATIVE`.

| Time | Event | Confidence | Source file |
|---|---|---|---|
| 2026-06-11 | CAM-6 offline | CONFIRMED | camera-register.md |
| 2026-09-24 | B-1002 badge reported lost | CONFIRMED | badge-log.csv.txt |
| 2026-09-28 20:15:33 | B-0777 badged into MAIN_OFFICE | CONFIRMED | badge-log.csv.txt |
| 2026-09-28 20:15:41 | B-1041 badged in 8s later | CONFIRMED | badge-log.csv.txt |
| 2026-09-28 23:30-23:44 | B-1041 in and out | INFERRED | badge-log.csv.txt |
| Overnight | Entry with no badge use | INFERRED | camera-register.md |
| Morning | B-1002 arrival swipe | CONFIRMED | badge-log.csv.txt |

**Minimum 6 entries.** Times may be given as ranges or "after 22:00" where the
evidence does not support an exact time.

---

## 3. What the Evidence Proves

State each fact you consider established, with its confidence level and source.

---

## 4. What the Evidence Does NOT Show

- Who used B-0777; the log records badge ID, not a person.
- Which entry route was used; CAM-6 is offline.
- When the laptop was taken; no sensor covers the staff room.

---

## 5. Detection Control Evaluation

For each control the building has, say whether it would have detected this
incident — and prove it with the camera register or a stated absence.

| Control | Code | Would it have detected? | Justification |
|---|---|---|---|
| Main office badge | ACCESS | Partially | Logged B-0777, no identity |
| Library badge | ACCESS | Partially | Same limitation |
| CAM-1 | VIDEO | Possibly | Front desk only |
| CAM-4 | VIDEO | No | IR illuminator failed |
| CAM-6 | VIDEO | No | Offline since June |
| Motion | MOTION | No | Not installed |
| Alarm | ALARM | No | No alarm system |

**At least 5 controls evaluated**, drawn from: `MOTION`, `THERMAL`, `ACOUSTIC`,
`ACCESS`, `VIDEO`, `ALARM`.

Note which of these the building **does not currently have** — the absence is
the finding.

---

## 6. Revised Sensor Plan

What you would change. For each recommendation: what to install or fix, which
`control code` it is, what it would have caught, and cost/effort.

| # | Recommendation | Control code | What it would have caught | Effort |
|---|---|---|---|---|
| 1 | Enforce deactivation on separation | ACCESS | B-0777 | Low |
| 2 | Replace CAM-6 | VIDEO | Entry route | Low |
| 3 | Repair CAM-4 IR | VIDEO | Parking lot | Low |
| 4 | Staff room door contact | ACCESS | Exact time | Low |

**Minimum 4 recommendations.**

---

## 7. First Change

Deactivating orphaned badges first, because it addresses the confirmed cause
and costs nothing but configuration.

---

## 8. What I Am Not Sure About

- The entry route; neighbouring property footage would settle it.
- The 20:15 B-1041 swipe, unexplained by Osei's account.
