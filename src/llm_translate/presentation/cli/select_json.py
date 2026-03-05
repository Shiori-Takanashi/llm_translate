# src/llm_translate/presentation/cli/select_json.py

import click

from llm_translate.infra.filesys import listup_json, convert_path_to_display
from llm_translate.application.config import AppConfig
from llm_translate.application.select.json_usecase import resolve_choice


@click.command(name="select-json")
@click.pass_obj
def select_json(config: AppConfig) -> None:
    base_path = config.base_path
    data_dir = config.data_dir
    json_dir = config.json_dir

    search_dirname: str = f"{data_dir}/{json_dir}"
    # listup_jsonの返り値をココから変更
    # filesはフルパスであるべき？
    files = listup_json(base_path, search_dirname)

    click.echo("\n翻訳対象のファイルを選択せよ:")
    for i, p in enumerate(files, 1):
        click.echo(f"{i}: {convert_path_to_display(p, base_path, search_dirname)}")

    choice = click.prompt("番号", type=int)

    selected = resolve_choice(files, choice)

    click.secho(
        f"選択されたファイル: {convert_path_to_display(selected, base_path, search_dirname)}"
    )
