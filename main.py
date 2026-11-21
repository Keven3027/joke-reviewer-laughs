"""Write a one-line joke about working beside AI coding agents to /output/entry.txt."""

import os

JOKE = "I told the agent \"just fix the bug, don't refactor anything.\" It said \"Understood.\" Then it rewrote my error handler in iambic pentameter."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE.strip() + "\n")


if __name__ == "__main__":
    main()
