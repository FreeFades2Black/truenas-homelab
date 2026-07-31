# filepath: d:\projects\Donavan010\truenas-homelab\scripts\check_repo.py
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

    # Extra repo-health hints
    yaml_files = list(repo_root.glob("*.yml")) + list(repo_root.glob("*.yaml"))
    print(f"YAML files found: {len(yaml_files)}")

    scripts_dir = repo_root / "scripts"
    if scripts_dir.exists():
        print(f"Scripts directory exists: {scripts_dir}")
    else:
        print("Scripts directory is missing.")

if __name__ == "__main__":
    main()
