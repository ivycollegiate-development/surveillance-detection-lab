"""Grading gate for the Surveillance Detection Lab.

Usage:
    python3 scripts/check_report.py            # gate: exit 0 = complete
    python3 scripts/check_report.py --selftest # blank template MUST fail

Beyond structure, this gate enforces the two things that matter most in this
lab: every timeline claim must be confidence-tagged and cite a source file,
and the analyst must explicitly address what the evidence does NOT show.

It cannot verify that a student's reasoning is *correct*. It can verify that
the reasoning is present, sourced, and honest about uncertainty.
"""
import os
import re
import sys

TIMELINE_MIN = 6
CONTROLS_MIN = 5
RECS_MIN = 4
NOT_SHOW_MIN = 3
UNCERTAINTY_MIN = 2

CONFIDENCE = ("CONFIRMED", "INFERRED", "SPECULATIVE")
CONTROL_CODES = {"MOTION", "THERMAL", "ACOUSTIC", "ACCESS", "VIDEO", "ALARM"}

DATA_FILES = {
    "badge-log.csv.txt", "camera-register.md", "interview-notes.md",
}

SECTIONS = [
    "## 1. Summary",
    "## 2. Timeline",
    "## 3. What the Evidence Proves",
    "## 4. What the Evidence Does NOT Show",
    "## 5. Detection Control Evaluation",
    "## 6. Revised Sensor Plan",
    "## 7. First Change",
    "## 8. What I Am Not Sure About",
]

PLACEHOLDER = re.compile(r"YOUR NAME|YOUR DATE|^\s*\|?\s*\|?\s*$", re.M)


def load(path="incident-report.md"):
    with open(path) as f:
        return f.read()


def section(text, header):
    """Return the body of a section, up to the next '## ' heading."""
    start = text.find(header)
    if start == -1:
        return None
    rest = text[start + len(header):]
    nxt = rest.find("\n## ")
    return rest if nxt == -1 else rest[:nxt]


def count_rows(block):
    """Markdown table rows that actually have content (not | | | placeholders)."""
    rows = 0
    for line in block.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 2:
            continue
        if all(c == "" or set(c) <= set("-: ") for c in cells):
            continue
        if any(c for c in cells):
            rows += 1
    return rows


def check(text):
    problems = []

    for h in SECTIONS:
        if h not in text:
            problems.append(f"  missing section: {h}")

    if "YOUR NAME" in text:
        problems.append("  **Auditor** is still YOUR NAME")

    # --- Timeline: every row needs a confidence tag and a real source file.
    tl = section(text, "## 2. Timeline")
    if tl is not None:
        rows = [l for l in tl.splitlines()
                if l.strip().startswith("|") and not re.match(r"^\s*\|[\s\-:|]+\|\s*$", l)]
        body = [l for l in rows if "Confidence" not in l and "Time" not in l]
        if len(body) < TIMELINE_MIN:
            problems.append(
                f"  timeline has {len(body)} entries; need at least {TIMELINE_MIN}"
            )
        for i, line in enumerate(body, 1):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            # Scan every cell: students reorder columns, and the confidence tag
            # must be found wherever they put it.
            if not any(c in cells[0].upper() for c in CONFIDENCE) and \
               not any(c.upper() in CONFIDENCE for c in cells):
                problems.append(
                    f"  timeline row {i}: no confidence tag "
                    f"({'/'.join(CONFIDENCE)})"
                )
            if not any(f in line for f in DATA_FILES):
                problems.append(
                    f"  timeline row {i}: cites no file from incident-data/"
                )

    # --- Section 4: what the evidence does NOT show.
    ns = section(text, "## 4. What the Evidence Does NOT Show")
    if ns is not None:
        bullets = [l for l in ns.splitlines() if re.match(r"^\s*[-*\d]", l)]
        if len(bullets) < NOT_SHOW_MIN:
            problems.append(
                f"  'does NOT show' has {len(bullets)} item(s); need at least {NOT_SHOW_MIN}"
            )

    # --- Section 5: control codes must be real codes.
    ctl = section(text, "## 5. Detection Control Evaluation")
    if ctl is not None:
        if count_rows(ctl) < CONTROLS_MIN:
            problems.append(
                f"  control evaluation has {count_rows(ctl)} row(s); "
                f"need at least {CONTROLS_MIN}"
            )
        found = {c for c in CONTROL_CODES if c in ctl}
        if len(found) < 3:
            problems.append(
                f"  only {len(found)} valid control code(s) used "
                f"({', '.join(sorted(found)) or 'none'}); "
                f"draw from {sorted(CONTROL_CODES)}"
            )

    # --- Section 6: sensor plan recommendations.
    sp = section(text, "## 6. Revised Sensor Plan")
    if sp is not None:
        if count_rows(sp) < RECS_MIN:
            problems.append(
                f"  sensor plan has {count_rows(sp)} row(s); "
                f"need at least {RECS_MIN}"
            )

    # --- Section 8: uncertainty.
    un = section(text, "## 8. What I Am Not Sure About")
    if un is not None:
        bullets = [l for l in un.splitlines() if re.match(r"^\s*[-*\d]", l)]
        if len(bullets) < UNCERTAINTY_MIN:
            problems.append(
                f"  uncertainty section has {len(bullets)} item(s); "
                f"need at least {UNCERTAINTY_MIN}"
            )

    return problems


def main():
    selftest = "--selftest" in sys.argv
    text = load()
    problems = check(text)

    if selftest:
        if not problems:
            print("SELFTEST FAIL: blank template passed the gate (rules are broken)")
            sys.exit(1)
        print(f"  blank template correctly fails with {len(problems)} problem(s):")
        for p in problems[:8]:
            print(p)
        if len(problems) > 8:
            print(f"  ... and {len(problems) - 8} more")
        print("selftest OK")
        sys.exit(0)

    if problems:
        for p in problems:
            print(p)
        print(f"\nGATE: RED X — {len(problems)} problem(s) to fix (see list above)")
        sys.exit(1)
    print("\nGATE: GREEN CHECK — incident analysis is complete and well-sourced")


if __name__ == "__main__":
    main()
