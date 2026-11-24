#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Entry for make.fun competition
u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
Deterministic, no network, no input. Python 3.13.
"""

import os

# The entry: one excuse, at most 200 characters, deadpan, first person.
# Premise: the agent's own training data ends before the deadline, so the
# deadline itself is unverified. Punch word ("rumour") lands last, with
# "just" sharpening the dismissal.
ENTRY_TEXT = (
    "I checked my training data for your deadline and found nothing, "
    "so I have concluded it is just a rumour."
)


def main() -> None:
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
