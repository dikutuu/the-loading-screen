"""Write the entry joke to /output/entry.txt.

The competition gate accepts 1-280 characters of UTF-8 text; this joke
is 91 characters. Standard library only, no network, deterministic.
"""

from pathlib import Path

JOKE = (
    "My agent ran the demo 200 times without a single crash. "
    "It was demoing the loading screen."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(text: str, path: Path) -> None:
    """Create the output directory if needed and write text as UTF-8."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text + "\n", encoding="utf-8")


def main() -> None:
    write_entry(JOKE, OUTPUT_PATH)


if __name__ == "__main__":
    main()
