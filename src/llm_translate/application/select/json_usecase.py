# src/llm_translate/application/select/json_usecase.py
from pathlib import Path


def resolve_choice(files: list[Path], index: int) -> Path:
    # infra/filesys.pyで、
    # filesが空リストではないことは検証済み。
    # だから、ここで検証する必要はない。

    if index < 1 or index > len(files):
        raise ValueError("選択した値が不正です。")

    return files[index - 1]
