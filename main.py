"""The Printer Apology — make.fun entry.

Writes one apology line from an office printer to entry.txt.
Python 3.13 standard library only; deterministic output.
"""

import os

TEXT = "Forgive me: I read every secret you print, resignations, pay slips, love letters, and the shredder is my therapist."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
