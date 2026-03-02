# src/llm_translate/presentation/main.py

import click

from llm_translate.application.config import AppConfig
from llm_translate.infra.root import PROJECT_ROOT
from llm_translate.infra.environment import load_env, require
from llm_translate.presentation.cli.select_json import select_json


@click.group()
@click.pass_context
def main(ctx: click.Context) -> None:
    """llm_translate CLI"""
    load_env([PROJECT_ROOT / ".env.local", PROJECT_ROOT / ".env"])
    json_dir = require("JSON_DIR")
    ctx.obj = AppConfig(json_dir=json_dir)


# サブコマンド登録
main.add_command(select_json)


if __name__ == "__main__":
    main()
