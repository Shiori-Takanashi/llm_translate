# src/llm_translate/application/config.py

from pathlib import Path
from dataclasses import dataclass


@dataclass
class AppConfig:
    base_path: Path
    data_dir: str
    json_dir: str
