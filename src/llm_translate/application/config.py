# src/llm_translate/application/config.py

from dataclasses import dataclass


@dataclass
class AppConfig:
    json_dir: str
