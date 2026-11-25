"""One-Line Office Jokes.

Writes one single-line joke about office life to /output/entry.txt.

The joke: a worker types the passive-aggressive office staple "per my last
email" and autocorrect rewrites it as the blunt truth underneath — "as I
already told you, twice". Setup and turn in one line, punchline last. It
turns on a real office detail (the email phrase everyone recognises), needs
no setup beyond the line itself, and avoids the tired meeting, reply-all
and printer angles. The turn works because the machine does what the writer
only wished they could say: the polite corporate mask slips, and the reader
laughs at the honesty, not at the typo.
"""

import os
import sys

ENTRY = (
    "I typed 'per my last email' and autocorrect changed it to "
    "'as I already told you, twice'."
)


def validate(text: str) -> str:
    if not text or text.strip() == "":
        raise ValueError("entry is empty")
    if len(text) > 199:
        raise ValueError(f"entry is {len(text)} chars, over the 199 gate")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    return text


def main() -> None:
    if "--check" in sys.argv:
        entry = validate(ENTRY)
        print(f"self-test ok: {entry} ({len(entry)} chars, 1 line)")
        return
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
