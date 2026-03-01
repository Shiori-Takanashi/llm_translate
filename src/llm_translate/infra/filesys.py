# src/llm_translate/infra/filesys.py

from llm_translate.infra.root import PROJECT_ROOT


def listup_json(dir_name: str) -> list[str]:
    d_path = PROJECT_ROOT / dir_name

    if not d_path.exists() or not d_path.is_dir():
        raise FileNotFoundError(f"ディレクトリが見つかりません: {dir_name}")

    files = [
        str(p.relative_to(PROJECT_ROOT / dir_name))
        for p in d_path.rglob("*.json")
        if p.is_file()
    ]

    if not files:
        raise FileNotFoundError("JSONファイルが見つかりません")

    return sorted(files)
