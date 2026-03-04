# Issue03: PROJECT_ROOTへの依存

## 背景

###  `listup_json()`について（`infra/filesys.py`）

80e2d82 の時点において、
`listup_json()`は、PROJECT_ROOTをimportして使用している。
そこで、以下の設計原則を遵守させる。

### 設計原則

- 関数は外部状態に依存すべきでない。
- application層からinfra層へDIを行うべき。

## 問題点

1. `PROJECT_ROOT`がグローバル定数である。
2. `listup_json()`が暗黙で`PROJECT_ROOT`前提に動く。
3. `listup_json()`がテストしづらい。

## タスク

- infra層からimportしたroot解決ロジックを、presentation層で実行。
- `listup_json()`に`base_path`をDIする仕様に変更。

## 完了条件

- infra層がグローバルrootに依存しない。
- 適切にDIを導入する。
- `python -m llm_translate.presentation.main select-json`が従来通り作動。

## スコープ外

- pytestの実装は後のIssueで行う
