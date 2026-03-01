def resolve_choice(files: list[str], index: int) -> str:
    if not files:
        raise ValueError("ファイルが空です。")

    if index < 1 or index > len(files):
        raise ValueError("インデックスが不正です。")

    return files[index - 1]
