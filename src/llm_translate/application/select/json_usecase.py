def resolve_choice(files: list[str], index: int) -> str:
    if not files:
        raise ValueError("ファイルが見つかりません。")

    if index < 1 or index > len(files):
        raise ValueError("選択した値が不正です。")

    return files[index - 1]
