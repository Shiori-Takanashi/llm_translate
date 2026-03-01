# src/llm_translate/infra/root.py


from pathlib import Path
from functools import lru_cache


def _find_project_root(start: Path) -> Path:
    current = start.resolve()
    while True:
        if (current / "pyproject.toml").is_file():
            return current
        if current.parent == current:
            raise FileNotFoundError("pyproject.toml not found.")
        current = current.parent


@lru_cache
def get_project_root() -> Path:
    return _find_project_root(Path(__file__).parent)


PROJECT_ROOT = get_project_root()
