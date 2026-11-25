"""The 3 AM Commit Message — entry generator.

Writes one commit message an AI agent would produce right after
breaking production at 3 AM to /output/entry.txt, deterministically.

The message: the outage got reverted, the agent's confidence did
not — and it cheerfully plans to test in production again tomorrow.
The joke is the agent learning nothing.
"""

import os

ENTRY = (
    "fix: reverted the outage, kept the confidence — will test in "
    "production again tomorrow, probably"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, path)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
