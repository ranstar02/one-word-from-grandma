"""One Word From Grandma — make.fun entry.

The program writes exactly one word to /output/entry.txt: the word a
grandma would text about AI.

The word is "smartypants": the classic grandma word for a know-it-all,
and an AI machine is the ultimate know-it-all — it knows everything and
answers anything. Warm, a little scolding, exactly how a grandma types
to a grandchild ("that smarty-pants machine"). The joke lands in one
word, with no caption or context needed, and it comes from grandma's
voice rather than from robot words, so it stands out from the crowd.

Deterministic, stdlib only, no network, no randomness. The program
self-checks the word before writing it, so a bad value can never
reach the output file.
"""

import os

WORD = "smartypants"


def self_check(word: str) -> None:
    """Gate: one word, 1-30 characters, not only whitespace."""
    assert isinstance(word, str), "word must be a string"
    assert word.strip() != "", "word must not be empty or whitespace only"
    assert len(word) >= 1 and len(word) <= 30, "word must be 1-30 characters"
    assert not any(ch.isspace() for ch in word), "word must be a single word"


def write_entry(word: str) -> str:
    """Write the word (plus a newline) to /output/entry.txt.

    Falls back to ./output/entry.txt when /output cannot be written.
    Returns the path that was written.
    """
    self_check(word)
    text = word + "\n"
    for base in ("/output", "output"):
        path = os.path.join(base, "entry.txt")
        try:
            os.makedirs(base, exist_ok=True)
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(text)
            return path
        except OSError:
            continue
    raise OSError("could not write entry.txt to /output or ./output")


def main() -> None:
    path = write_entry(WORD)
    print(WORD)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
