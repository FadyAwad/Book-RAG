from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "project" / "data"

if __name__ == "__main__":
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(str(DATA_DIR))
