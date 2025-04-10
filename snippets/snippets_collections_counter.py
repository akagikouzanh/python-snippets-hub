"""
example collections Counter

Usage:
    snippets_collections_counter.py

See also:
https://docs.python.org/ja/3.13/library/collections.html
"""

from collections import Counter
import random


def collections_counter():
    """データの件数をカウントする"""
    # Counter({'i': 7, 'c': 3, 'a': 3, 'l': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 's': 2, 'o': 2, 'S': 1, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1})
    s = "Supercalifragilisticexpialidocious"
    print(f"{s}の文字数カウント:")
    print(Counter(s))


def numeric_counter():
    """数値データのカウント"""
    nums = [2, 1, 3, 1, 2, 5, 2, 4, 3, 4]
    c = Counter()
    for num in nums:
        c[num] += 1
    # Counter({2: 3, 1: 2, 3: 2, 4: 2, 5: 1})
    print("数値カウント:", c)


def shuffle_data_counter():
    """リストをランダムにしても正しくカウントされる"""
    li = ["spam"] * 100 + ["ham"] * 90 + ["egg"] * 110
    print("シャッフルデータのサイズ:", len(li))
    random.shuffle(li)
    print("シャッフルデータ数のカウント:", Counter(li))


def counter_operations():
    """Counterのsubtract, update, +, -, &, | 演算の使用例"""
    c1 = Counter(a=3, b=2, c=1, d=0)
    # Counter({'a': 3, 'b': 2, 'c': 1, 'd': 0})
    print(c1)
    # ['a', 'a', 'a', 'b', 'b', 'c']
    print(list(c1.elements()))
    c2 = Counter(a=2, b=1, c=1, d=1)
    # Counter({'a': 2, 'b': 1, 'c': 1, 'd': 1})
    print(c2)
    # c1からc2の要素を減算する
    c1.subtract(c2)
    # Counter({'a': 1, 'b': 1, 'c': 0, 'd': -1})
    print("subtract: ", c1)

    # c1からc2の要素を加算する
    c1.update(c2)
    # Counter({'a': 3, 'b': 2, 'c': 1, 'd': 0})
    print("update: ", c1)

    # 演算
    print("===演算===")
    print(c1 + c2)
    print(c1 - c2)
    print(c1 & c2)
    print(c1 | c2)


if __name__ == "__main__":
    collections_counter()
    numeric_counter()
    shuffle_data_counter()
    counter_operations()
