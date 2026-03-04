# src/llm_translate/infra/root.py


from pathlib import Path


def find_project_root(start: Path) -> Path:
    current = start.resolve()
    if current.is_file():
        current = current.parent
    while True:
        if (current / "pyproject.toml").is_file():
            return current
        if current.parent == current:
            raise FileNotFoundError("pyproject.tomlが未発見。")
        current = current.parent
