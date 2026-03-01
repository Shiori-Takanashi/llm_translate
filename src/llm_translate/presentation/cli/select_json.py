# src/llm_translate/presentation/cli/select_json.py

import click

from llm_translate.infra.environment import load_env, require
from llm_translate.infra.filesys import listup_json


@click.command(name="select-json")
def select_json() -> None:
    load_env()
    dir_name = require("JSON_DIR")

    files = listup_json(dir_name)

    click.echo("\n翻訳対象のファイルを選択してください:")
    for i, p in enumerate(files, 1):
        click.echo(f"{i}: {p}")

    choice = click.prompt(
        "番号を入力してください",
        type=click.IntRange(1, len(files)),
        show_choices=False,
    )

    selected = files[choice - 1]

    click.secho(f"選択されたファイル: {selected}")
