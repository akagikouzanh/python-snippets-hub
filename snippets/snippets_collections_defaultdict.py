"""
example collections defaultdict

Usage:
    snippets_collections_defaultdict.py

See also:
https://docs.python.org/ja/3.13/library/collections.html#collections.defaultdict
"""

from collections import defaultdict


if __name__ == "__main__":
    # キーがない場合に返す値を設定することができるのがdefault factory
    # d = {"params": [1, 2, 3]}
    # KeyError: "key"
    # print(d["key"])

    # KeyErrorにならず、空のリストが表示されるようになる
    dd: defaultdict = defaultdict(list, params=[1, 2, 3])
    print(dd["key"])

    # defaultdict(<class 'list'>, {'params': [1, 2, 3], 'key': []})
    print(dd)

    d: defaultdict = defaultdict(int)
    s: str = "japan"
    for i in s:
        d[i] += 1

    # defaultdict(<class 'int'>, {'j': 1, 'a': 2, 'p': 1, 'n': 1})
    print(d)

    # データセットのグループ化
    data = [
        ("vegetable", "tomato"),
        ("fruit", "apple"),
        ("vegetable", "carrot"),
        ("fruit", "banana"),
        ("vegetable", "lettuce"),
    ]

    categories: defaultdict = defaultdict(list)
    for kind, name in data:
        categories[kind].append(name)

    # defaultdict(<class 'list'>, {'vegetable': ['tomato', 'carrot', 'lettuce'], 'fruit': ['apple', 'banana']})
    print(categories)

    # access log
    access_log = [
        ("2025-04-10", "user1"),
        ("2025-04-10", "user2"),
        ("2025-04-10", "user1"),
        ("2025-04-09", "user1"),
    ]

    # lambdaにすることでnestedのdefault dictを構築することができる
    user_access: defaultdict = defaultdict(lambda: defaultdict(int))

    for day, user in access_log:
        # nestedに値がなければ0値でデータが作成される
        user_access[day][user] += 1

    # defaultdict(<function <lambda> at 0x104bcb240>, {'2025-04-10': defaultdict(<class 'int'>, {'user1': 2, 'user2': 1}), '2025-04-09': defaultdict(<class 'int'>, {'user1': 1})})
    # print(user_access)
    # 出力:
    #  2025-04-10:
    #    user1: 2
    #    user2: 1
    #  2025-04-09:
    #    user1: 1
    for day, users in user_access.items():
        print(f"{day}:")
        for user, count in users.items():
            print(f"  {user}: {count}")
