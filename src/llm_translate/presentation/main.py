# src/llm_translate/presentation/main.py

import click

from llm_translate.presentation.cli.select_json import select_json


@click.group()
def main() -> None:
    """llm_translate CLI"""
    pass


# サブコマンド登録
main.add_command(select_json)


if __name__ == "__main__":
    main()
