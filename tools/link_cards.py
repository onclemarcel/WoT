"""Turn card titles inside the exported cards into relative Markdown links.

Claude Docs exports links between cards as plain titles. Run this after
replacing any card with a fresh export:

    python3 tools/link_cards.py

It is safe to run more than once, and after moving a card: existing links to
known cards are rebuilt from the list below.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Card title (as it appears in the exports) -> file, relative to the repo root.
TITLES = {
    "Wheel of Time — Story Map": "story-map.md",
    "WoT Character — Perrin": "characters/perrin.md",
    "WoT Thread — The Shadow": "threads/shadow.md",
    "WoT Character — Faile": "characters/faile.md",
    "WoT Arc — The Road with Elyas": "arcs/b01-road-with-elyas.md",
    "EotW Ch. 1 — An Empty Road": "chapters/b01-eye-of-the-world/ch01-an-empty-road.md",
    "EotW Ch. 2 — Strangers": "chapters/b01-eye-of-the-world/ch02-strangers.md",
    "WoT — World Index": "world/index.md",
    "WoT — Manetheren": "world/manetheren.md",
    "WoT — Stedding": "world/stedding.md",
    "EotW Ch. 3 — The Peddler": "chapters/b01-eye-of-the-world/ch03-the-peddler.md",
    "EotW Ch. 4 — The Gleeman": "chapters/b01-eye-of-the-world/ch04-the-gleeman.md",
    "EotW Ch. 5 — Winternight": "chapters/b01-eye-of-the-world/ch05-winternight.md",
    "EotW Ch. 6 — The Westwood": "chapters/b01-eye-of-the-world/ch06-the-westwood.md",
    "WoT Character — Padan Fain": "characters/padan-fain.md",
    "WoT Character — Rand": "characters/rand.md",
    "WoT Character — Mat": "characters/mat.md",
    "WoT Character — Nynaeve": "characters/nynaeve.md",
    "WoT Character — Egwene": "characters/egwene.md",
    "WoT Character — Moiraine": "characters/moiraine.md",
    "WoT Character — Lan": "characters/lan.md",
    "WoT Character — Thom": "characters/thom.md",
    "WoT Character — Tam": "characters/tam.md",
    "WoT — The Two Rivers": "world/two-rivers.md",
    "WoT — Ghealdan": "world/ghealdan.md",
    "WoT — Illian": "world/illian.md",
    "WoT — Tar Valon and the White Tower": "world/tar-valon.md",
    "WoT — Children of the Light": "world/children-of-the-light.md",
    "WoT — Tales and Legends": "world/tales-and-legends.md",
}

# Some exports lose the title of their "Up" link and print "Up: Doc".
# File -> the card its "Up" link points to.
UP_TARGETS = {
    "characters/perrin.md": "story-map.md",
    "world/index.md": "story-map.md",
    "world/manetheren.md": "world/index.md",
    "world/stedding.md": "world/index.md",
}

# Old card titles -> current title. Links in Claude Docs can keep a card's old
# title after a rename, and exports print that old title.
RENAMED = {
    "WoT Thread — Perrin": "WoT Character — Perrin",
}

PATH_TO_TITLE = {path: title for title, path in TITLES.items()}

# Longest titles first, so a long title is never split by a shorter one.
TITLE_PATTERN = re.compile(
    r"(?<!\[)("
    + "|".join(re.escape(t) for t in sorted(TITLES, key=len, reverse=True))
    + r")(?!\]\()"
)


# An existing link to a known card, so it can be rebuilt if the card moved.
KNOWN = set(TITLES) | set(RENAMED)
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\([^)]*\.md\)")


def unlink(line):
    return LINK_PATTERN.sub(
        lambda m: m.group(1) if m.group(1) in KNOWN else m.group(0), line
    )


def rel(from_file, to_file):
    return os.path.relpath(to_file, os.path.dirname(from_file)).replace(os.sep, "/")


def link_file(path):
    full = os.path.join(ROOT, path)
    with open(full, encoding="utf-8") as f:
        lines = f.read().split("\n")

    out = []
    for line in lines:
        if line.startswith("# "):  # the card's own title stays plain
            out.append(line)
            continue
        line = unlink(line)
        for old, new in RENAMED.items():
            line = line.replace(old, new)
        if line.strip() == "Up: Doc" and path in UP_TARGETS:
            target = UP_TARGETS[path]
            line = f"Up: [{PATH_TO_TITLE[target]}]({rel(path, target)})"
        line = TITLE_PATTERN.sub(
            lambda m: f"[{m.group(1)}]({rel(path, TITLES[m.group(1)])})", line
        )
        out.append(line)

    text = "\n".join(out)
    with open(full, encoding="utf-8") as f:
        changed = f.read() != text
    if changed:
        with open(full, "w", encoding="utf-8") as f:
            f.write(text)
    return changed


def main():
    missing = [p for p in TITLES.values() if not os.path.exists(os.path.join(ROOT, p))]
    if missing:
        sys.exit("Missing card files: " + ", ".join(missing))
    for path in sorted(set(TITLES.values())):
        if link_file(path):
            print("linked", path)


if __name__ == "__main__":
    main()
