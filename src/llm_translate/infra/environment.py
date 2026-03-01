# src/llm_translate/infra/environment.py

import os

from llm_translate.infra.root import PROJECT_ROOT


def load_env() -> None:
    dot_env_local = PROJECT_ROOT / ".env.local"
    dot_env = PROJECT_ROOT / ".env"

    env_file = None
    if dot_env_local.exists():
        env_file = dot_env_local
    elif dot_env.exists():
        env_file = dot_env

    if env_file is None:
        raise FileNotFoundError("envファイルが未存在")

    try:
        from dotenv import load_dotenv

        load_dotenv(env_file, override=False)
    except Exception:
        raise ImportError("python-dotenvが未インストール。")


def require(name: str) -> str:
    v = os.getenv(name)
    if v is None:
        raise RuntimeError(f'環境変数"{name}"が未定義')
    return v
