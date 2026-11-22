"""Write one short text to /output/entry.txt.

The text is a quiet photograph of an absence: an empty chair, tea still
steaming, a window open to rain that has not started yet. Nothing is
ordered, nothing is explained; the last clause quietly reframes the rest.
"""

import os

ENTRY_TEXT = (
    "The photograph shows an empty chair, a cup of tea still steaming, "
    "and a window open to rain that has not started yet."
)


def main() -> int:
    text = ENTRY_TEXT
    if not (1 <= len(text) <= 280):
        raise ValueError(f"entry must be 1-280 code points, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    data = text.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    if os.path.abspath(out_dir) != os.path.abspath("/output"):
        # Best effort mirror: a read-only /output must not fail the run.
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "wb") as f:
                f.write(data)
        except OSError:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
