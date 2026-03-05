# src/llm_translate/infra/filesys.py

from pathlib import Path


def listup_json(base_path: Path, search_dirname: str) -> list[Path]:
    d_path = base_path / search_dirname

    if not d_path.exists() or not d_path.is_dir():
        raise FileNotFoundError(f"ディレクトリが見つかりません: {search_dirname}")

    files = [p for p in d_path.rglob("*.json") if p.is_file()]

    # filesは空リストではない。
    if not files:
        raise FileNotFoundError("JSONファイルが見つかりません")

    return sorted(files)


def convert_path_to_display(p: Path, base_path: Path) -> str:
    return str(p.relative_to(base_path))
