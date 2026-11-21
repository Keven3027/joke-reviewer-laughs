"""Write a one-line joke about working beside AI coding agents to /output/entry.txt."""

import os

JOKE = "My coding agent apologized for breaking the build, promised to be more careful, and broke it again on the next commit — honestly the most human colleague I've ever had."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE.strip() + "\n")


if __name__ == "__main__":
    main()
