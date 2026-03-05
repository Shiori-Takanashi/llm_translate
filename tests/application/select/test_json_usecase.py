import pytest

from llm_translate.application.select.json_usecase import resolve_choice


def test_resolve_choice_valid(tmp_path):
    tmp_path.mkdir(exist_ok=True)
    files = [tmp_path / name for name in ["a.json", "b.json"]]
    assert resolve_choice(files, 1) == tmp_path / "a.json"


def test_resolve_choice_invalid(tmp_path):
    tmp_path.mkdir(exist_ok=True)
    with pytest.raises(ValueError):
        resolve_choice([tmp_path / name for name in ["a.json", "b.json"]], 3)
