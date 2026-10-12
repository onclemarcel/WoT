"""Write Claude Docs markdown exports into the repo.

The Docs `export` tool returns each card as base64 inside the session log.
Copying that base64 by hand is slow and error-prone, so this script reads it
back from the newest session log and writes the files:

    python3 tools/save_exports.py "WoT Character — Tam.md=characters/tam.md" ...

Each argument maps an export's file name (the `name` field of the export
result) to a path in the repo. The latest export of each name wins, and the
byte count is checked against the export's `bytes` field.
"""

import base64
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS = os.path.expanduser("~/.claude/projects/*/*.jsonl")
EXPORT = re.compile(r'"name":"([^"]+)","mime".*?"bytes":(\d+),"bytes_b64":"([A-Za-z0-9+/=]+)"')


def exports_in(log):
    latest = {}

    def walk(o):
        if isinstance(o, str):
            if '"bytes_b64"' in o:
                for m in EXPORT.finditer(o):
                    latest[m.group(1)] = (int(m.group(2)), m.group(3))
        elif isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    with open(log, encoding="utf-8") as f:
        for line in f:
            if "bytes_b64" in line:
                try:
                    walk(json.loads(line))
                except ValueError:
                    pass
    return latest


def main():
    pairs = [a.split("=", 1) for a in sys.argv[1:]]
    if not pairs or any(len(p) != 2 for p in pairs):
        sys.exit(__doc__)
    logs = sorted(glob.glob(LOGS), key=os.path.getmtime)
    if not logs:
        sys.exit("No session log found under ~/.claude/projects")
    latest = exports_in(logs[-1])
    failed = False
    for name, path in pairs:
        if name not in latest:
            print("MISSING", name)
            failed = True
            continue
        size, data = latest[name]
        raw = base64.b64decode(data)
        if len(raw) != size:
            print("SIZE MISMATCH", name, size, len(raw))
            failed = True
            continue
        full = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "wb") as f:
            f.write(raw)
        print("wrote", path, size, "bytes")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
