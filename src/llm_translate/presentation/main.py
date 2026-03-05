# src/llm_translate/presentation/main.py

import click
from pathlib import Path

from llm_translate.application.config import AppConfig
from llm_translate.infra.root import find_project_root
from llm_translate.infra.environment import load_env, require
from llm_translate.presentation.cli.select_json import select_json


@click.group()
@click.pass_context
def main(ctx: click.Context) -> None:
    """llm_translate CLI"""
    root = find_project_root(Path(__file__))
    load_env([root / ".env.local", root / ".env"])
    data_dir = require("DATA_DIR")
    json_dir = require("JSON_DIR")
    ctx.obj = AppConfig(base_path=root, data_dir=data_dir, json_dir=json_dir)


# サブコマンド登録
main.add_command(select_json)


if __name__ == "__main__":
    main()
