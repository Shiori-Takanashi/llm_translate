def resolve_choice(files: list[str], index: int) -> str:
    # infra/filesys.pyで、
    # filesが空リストではないことは検証済み。
    # だから、ここで検証する必要はない。

    if index < 1 or index > len(files):
        raise ValueError("選択した値が不正です。")

    return files[index - 1]
