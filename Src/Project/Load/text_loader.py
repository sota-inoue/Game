from pathlib import Path

def load_text(path):
    with path.open("r", encoding="utf-8") as file:
        return [
            [int(x) for x in line.split()]
            for line in file
            if line.strip()
        ]