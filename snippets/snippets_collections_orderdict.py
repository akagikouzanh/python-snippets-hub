"""
example collections order dict

Usage:
    python snippets_collections_orderdict.py

See also:
https://docs.python.org/ja/3.13/library/collections.html#collections.OrderedDict
"""

from collections import OrderedDict


if __name__ == "__main__":
    normal_dict = dict.fromkeys("abcde", 0)
    order_dict = OrderedDict.fromkeys("abcde", 0)
    print(f"normal_dict: {normal_dict}")
    print(f"order_dict: {order_dict}")

    # dを一番後ろに設定 d.move_to_end("d", last=False)の場合は先頭に来る
    order_dict.move_to_end("d")

    # OrderedDict({'a': 0, 'b': 0, 'c': 0, 'e': 0, 'd': 0})
    print(order_dict)

    # LIFO
    order_dict.popitem()
    # d.popitem(): OrderedDict({'a': 0, 'b': 0, 'c': 0, 'e': 0})
    print(f"d.popitem(): {order_dict}")

    # FIFO
    order_dict.popitem(last=False)
    # d.popitem(last=False): OrderedDict({'b': 0, 'c': 0, 'e': 0})
    print(f"d.popitem(last=False): {order_dict}")
