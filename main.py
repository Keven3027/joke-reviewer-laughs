"""Write a one-line joke about working beside AI coding agents to /output/entry.txt."""

import os

JOKE = "The agent fixed my bug in 40 seconds. I've spent the rest of the sprint writing the review comment that says it fixed the bug in 40 seconds."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE.strip() + "\n")


if __name__ == "__main__":
    main()
