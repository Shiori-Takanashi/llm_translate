# src/llm_translate/application/config.py

from pathlib import Path
from dataclasses import dataclass


@dataclass
class AppConfig:
    base_path: Path
    json_dir: str
