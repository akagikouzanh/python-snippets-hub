### collections

`collections`は コンテナデータ型の標準ライブラリ

- 特徴

  - 汎用組み込みコンテナ(list, dict, set, tuple)に変わる、特殊コンテナデータ型を実装している

- 主な使用用途

  - データの件数をカウント
  - デフォルト値を持った辞書
  - データ挿入順序を維持する辞書
  - 名前付きフィールドを持つタプル

- 注意

  - Python 3.7 以降、通常の `dict` も挿入順を保持するようになった
  - そのため、**明示的に順序を操作（移動・削除）したい場合のみ `OrderedDict` を使う**のが適切

### 資料

[ドキュメント](https://docs.python.org/ja/3.13/library/collections.html)

[snippets-collections-Counter](https://github.com/akagikouzanh/python-snippets-hub/blob/master/snippets/snippets_collections_counter.py)

[snippets-collections-default-dict](https://github.com/akagikouzanh/python-snippets-hub/blob/master/snippets/snippets_collections_defaultdict.py)

[snippets-collections-order-dict](https://github.com/akagikouzanh/python-snippets-hub/blob/master/snippets/snippets_collections_orderdict.py)

[snippets-collections-namedtuple](https://github.com/akagikouzanh/python-snippets-hub/blob/master/snippets/snippets_collections_namedtuple.py)
