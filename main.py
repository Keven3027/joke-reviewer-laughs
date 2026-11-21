"""Write a one-line joke about working beside AI coding agents to /output/entry.txt."""

import os

JOKE = "My AI coding agent writes better commit messages than I do. To be fair, it also writes most of my commits."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE.strip() + "\n")


if __name__ == "__main__":
    main()
