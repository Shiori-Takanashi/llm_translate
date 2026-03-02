# src/llm_translate/presentation/cli/select_json.py

import click

from llm_translate.infra.root import PROJECT_ROOT
from llm_translate.infra.filesys import listup_json
from llm_translate.application.config import AppConfig
from llm_translate.application.select.json_usecase import resolve_choice


@click.command(name="select-json")
@click.pass_obj
def select_json(config: AppConfig) -> None:
    dir_name = config.json_dir

    files = listup_json(PROJECT_ROOT, dir_name)

    click.echo("\n翻訳対象のファイルを選択せよ:")
    for i, p in enumerate(files, 1):
        click.echo(f"{i}: {p}")

    choice = click.prompt("番号", type=int)

    selected = resolve_choice(files, choice)

    click.secho(f"選択されたファイル: {selected}")
