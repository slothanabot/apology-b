#!/usr/bin/env python3
"""Write one AI-agent apology line to /output/entry.txt.

Angle: the agent confidently scheduled a meeting with the user's cat,
sent the cat a calendar invite and a pre-read, and is now apologizing
for it. Deterministic, stdlib only, no network, no secrets.
"""

import os

LINE = (
    "Sorry \u2014 I confidently scheduled a meeting with your cat, "
    "sent it a calendar invite and a pre-read. "
    "It hasn't replied. I think it's judging me."
)


def verify(path):
    """Re-read the written file and enforce the sealed gate."""
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert 1 <= len(text) <= 159, "entry is %d chars" % len(text)
    assert "\n" not in text and "\r" not in text, "entry is not one line"
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 159, "line is %d chars" % len(text)
    assert "\n" not in text, "line must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    checked = verify(path)
    assert checked == text, "written entry differs from the line"
    print("wrote %d chars to %s" % (len(text), path))


if __name__ == "__main__":
    main()
