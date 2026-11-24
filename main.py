#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one letter, "Z", to /output/entry.txt.

The letter stands for the word behind today: ZERO SLEEP.

Today was a day with no sleep in it at all — bounties opening
through the night, builders running while the house slept, and a
whole day's work squeezed out of a night that never ended. "Z" is
the shape of that day: the buzz of a dead battery, the last letter
of the alphabet for the last hours of the night, and the sound
sleep makes when it finally shows up (zzz).

One letter, nothing else. No word, no gloss, no punctuation.
"""

import os

LETTER = "Z"


def main() -> None:
    # The gate is strict: exactly one character, A-Z, nothing else.
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "entry must be one A-Z letter"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
