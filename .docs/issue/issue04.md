# Issue04: listup_json返り値のPath化

## 背景

PR03で`infra.filesys.listup_json()`からPROJECT_ROOT依存を排除したが、
返り値の型は`list[str]`となっている。

この結果、呼び出し側（presentation / application）が

- 文字列をPathとしてみなして扱う
- 後続処理で再度`Path`に変換する

といったコードを書かざるを得ず、責務境界と抽象度が曖昧になっている。

PR03内の「発見した問題点」としても、
`listup_json() -> list[Path]` への変更が提案されている。

## 問題点

1. `listup_json()`の返り値が`list[str]`であり、型が**Pathそのもの**を表現していない。
2. CLI層がPath相当の情報を文字列で扱うため、抽象度が下がる。
3. application層・ユースケース層で「文字列 -> Path」の再変換が必要になり、重複ロジック・バグの温床となる。

## 目的

- `listup_json()`の返り値を`list[Path]`に変更し、
  「ファイルパスを列挙する」という責務をinfra層に集約する。
- presentation / application層ではPathオブジェクトをそのまま扱い、
  表示などの都合で文字列化が必要な場合のみ変換を行うようにする。
- レイヤーごとの抽象度と責務境界を明確にする。

## 方針

- `infra.filesys.listup_json()`の返り値型を`list[str]`から`list[Path]`に変更する。
- `application.select.json_usecase.resolve_choice()`の引数・返り値の型を
  `list[str]` / `str` から `list[Path]` / `Path` に変更する。
- `presentation.cli.select_json.select_json()`では、
  Pathのリストを受け取り、
  - ユーザー表示時のみ文字列化
  - 選択結果としてはPathをそのまま保持
  するように修正する。
- 既存テスト（特に `tests/application/select/test_json_usecase.py`）も
  Path型に合わせて期待値を更新する。

## 完了条件

- `infra.filesys.listup_json()`の返り値が`list[Path]`となっている。
- `application.select.json_usecase.resolve_choice()`が`list[Path]`を受け取り、`Path`を返す。
- `presentation.cli.select_json.select_json()`が、
  - Pathのリストを受け取り
  - 表示時のみ文字列化している
  ことが確認できる。
- `tests/application/select/test_json_usecase.py`がPath型に追従しており、
  pytestがグリーンで通る。

## スコープ外

- `listup_json()`の列挙ロジック自体（どのディレクトリまで探索するか等）の変更。
- CLIインターフェースそのものの仕様変更（選択UIの変更など）。
