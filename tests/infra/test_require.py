# tests/infra/test_require.py

import pytest

from llm_translate.infra.environment import require


def test_require_returns_value_when_exists(monkeypatch):
    monkeypatch.setenv("JSON_DIR", "data/json")

    value = require("JSON_DIR")

    assert value == "data/json"


def test_require_raises_when_json_dir_missing(monkeypatch):
    monkeypatch.delenv("JSON_DIR", raising=False)

    with pytest.raises(RuntimeError) as e:
        require("JSON_DIR")

    assert '環境変数"JSON_DIR"が未定義' in str(e.value)
