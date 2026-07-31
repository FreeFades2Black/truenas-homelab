from pathlib import Path

REQUIRED_PATHS = [
    "README.md",
    "docker-compose.yml",
    "values.yaml",
]

def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]

    missing = []
    for rel in REQUIRED_PATHS:
        if not (repo_root / rel).exists():
            missing.append(rel)

    if missing:
        print("Missing expected files:")
        for item in missing:
            print(f" - {item}")
    else:
        print("Repository structure looks good.")

if __name__ == "__main__":
    main()
