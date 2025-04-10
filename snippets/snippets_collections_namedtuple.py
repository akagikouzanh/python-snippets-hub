"""
example collections namedtuple

Usage:
    snippets_collections_namedtuple.py

See also:
https://docs.python.org/ja/3.13/library/collections.html#collections.namedtuple
"""

from collections import namedtuple

if __name__ == "__main__":
    Students = namedtuple("Students", ["name", "age", "height"])
    taro = Students("taro", 12, 150)

    # taro 12 150
    print(taro.name, taro.age, taro.height)
    # {'name': 'taro', 'age': 12, 'height': 150}
    print(taro._asdict())

    taro = taro._replace(name="太郎")
    # Students(name='太郎', age=12, height=150)
    print(taro)

    # _make() はリストやタプルからnamedtupleを生成できる
    new_students_hanako = ["hanako", 32, 154]
    hanako = Students._make(new_students_hanako)
    # hanako
    print(hanako.name)

    Account = namedtuple("Account", ["type", "balance"], defaults=["premium", 0])
    # {"type": "premium", "balance": 0}
    print(Account._field_defaults)  # pylint: disable=no-member, protected-access

    basic = Account("basic")
    # Account(type='basic', balance=0)
    print(basic)
