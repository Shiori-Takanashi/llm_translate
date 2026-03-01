import pytest

from llm_translate.application.select.json_usecase import resolve_choice


def test_resolve_choice_valid():
    files = ["a.json", "b.json"]
    assert resolve_choice(files, 1) == "a.json"


def test_resolve_choice_invalid():
    with pytest.raises(ValueError):
        resolve_choice(["a.json"], 2)
