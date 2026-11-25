"""One-Line Office Jokes.

Writes one single-line joke about office life to /output/entry.txt.

The joke: a worker types the passive-aggressive office staple "per my last
email" and autocorrect rewrites it as the blunt truth underneath — "as I
already told you, twice". Setup and turn in one line, punchline last. It
turns on a real office detail (the email phrase everyone recognises), needs
no setup beyond the line itself, and avoids the tired meeting, reply-all
and printer angles.
"""

import os

ENTRY = (
    "I typed 'per my last email' and autocorrect changed it to "
    "'as I already told you, twice'."
)


def main() -> None:
    # The gate allows 1 to 199 characters; stay well inside it, and keep the
    # file to the single line with no trailing newline so the count is exact.
    assert 1 <= len(ENTRY) <= 199, "entry outside the 1-199 character gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
