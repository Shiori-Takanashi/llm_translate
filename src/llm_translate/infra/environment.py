# src/llm_translate/infra/environment.py
import os
from pathlib import Path


def load_env(candidates: list[Path]) -> Path:
    env_file = next((p for p in candidates if p.is_file()), None)
    if env_file is None:
        raise FileNotFoundError("envファイルが発見不能")

    try:
        from dotenv import load_dotenv
    except Exception as e:
        raise ImportError("python-dotenvが未インストール。") from e

    load_dotenv(env_file, override=False)
    return env_file


def require(name: str) -> str:
    v = os.getenv(name)
    if v is None:
        raise RuntimeError(f'環境変数"{name}"が未定義')
    return v
