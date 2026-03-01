prompt_ja = (
    "以下の単語を日本語に翻訳してください。\n"
    "普通の人が読みやすい翻訳をお願いします。\n"
    "日本語の翻訳のみを1行に1つずつ、入力と同じ順序で返してください。\n"
)


def build_prompt(content: str) -> str:
    return f"{prompt_ja}\n{content}"
