"""src/llm_translate/domain/types.py"""

from dataclasses import dataclass


@dataclass(frozen=True)
class OpenaiConst:
    api_key: str
    model: str
    timeout: str
    prompt: str
