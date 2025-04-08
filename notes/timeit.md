### timeit

`timeit`は実行時間を計測する標準ライブラリ

- 特徴

  - あまり大きくない(snippet)コード群のパフォーマンスチェックを行うことができる

- 主な使用用途

  - パフォーマンスチェック

- 注意
  - 名前空間を認識させないとエラーになる

### 資料

[ドキュメント](https://docs.python.org/ja/3.13/library/timeit.html)

[snippets](https://github.com/akagikouzanh/python-snippets-hub/blob/master/snippets/snippets_timeit.py)

- command line case

```bash
python -m timeit <option>
```

```
option:
-n N, --number=N: 実行回数
-r N, --repeat=N: timer を繰り返す回数
-s S, --setup=S: 初回に 1 回だけ実行する文(デフォルトは pass)
-p, --process: 実時間ではなくプロセス時間を計測
-u, --unit=U: timer の出力単位を指定(nsec, usec, msec, sec)
-v, --verbose: 計測結果詳細を数値で繰り返し表示する
-h, --help: ヘルプの表示
```

```bash sample-case
#　option -sでtextをセットアップ, その後、`test`がtextにあるかチェックしている
python -m timeit -s 'text = "this is a test."; char = "test"' 'char in text'

20000000 loops, best of 5: 15.3 nsec per loop
```
