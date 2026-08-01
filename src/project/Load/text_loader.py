from pathlib import Path

def load_text(filename):
    path = (
        Path(__file__).resolve().parent.parent
        / "Assets"
        / "map"
        / filename
    )

    with path.open("r", encoding="utf-8") as file:
        return [
            [int(x) for x in line.split()]
            for line in file
            if line.strip()
        ]