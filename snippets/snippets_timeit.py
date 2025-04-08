"""
example timeit

Usage:
  python snippets/snippets_timeit.py

See also:
https://docs.python.org/ja/3.13/library/timeit.html
"""

import timeit


if __name__ == "__main__":
    # 5回分のタイムを出力する
    # sample: [0.003027708036825061, 0.0028882090118713677, 0.0030957499984651804, 0.002981124969664961, 0.0029137920355424285]
    print(timeit.repeat('"here we go!"'))

    # setupを利用した例
    print(timeit.timeit("text.find(char)", setup='text = "hello world"; char = "d"'))

    # 複数行の場合(インデントをしっかりしないとダメ)
    S = """try:
    "This is a test".__bool__
except AttributeError:
    pass
"""
    # sample: 0.28930195805151016
    print(timeit.timeit(stmt=S))

    def my_func() -> list:
        """0から999までの整数を2乗したリストを生成して返す関数。

        Returns:
            list: 各整数の2乗値を格納したリスト
        """
        return [x**2 for x in range(1000)]

    # グローバル名前空間内で実行する(対象の関数をグローバルで探す)
    # グローバルなしでやるのであれば、そのままmy_funcを渡せばOK
    # 1000000回実行にかかった秒数
    # sample: 30.015518333006185
    print(timeit.timeit("my_func()", globals=globals()))
    total = timeit.timeit(my_func, number=10)
    print(f"1回あたりの平均実行時間: {total / 10:.8f}秒")
