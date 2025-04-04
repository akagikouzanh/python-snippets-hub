"""
特殊メソッド（__str__ など）を使ったクラスの例

Usage:
    python snippets/snippets_class_special_methods.py

See also:
https://docs.python.org/ja/3.13/reference/datamodel.html#special-method-names
"""

from __future__ import annotations
from typing import Any


class User:
    """
    Represents a user with name, age, and address.
    Provides methods to manipulate user attributes.
    """

    # Class variable
    user_type = None

    def __init__(self, name: str, age: int, address: str) -> None:
        """
        ユーザインスタンスを初期化します

        Args:
        name (str): User's name.
        age (int): User's age.
        address (str): User's address.

        Note:
        selfは別に名称はなんでもいいthisとか
        でも慣例としてselfを使用する、また、selfはインスタンスそのものを指す
        """
        # Instance variable
        self.name: str = name
        self.age: int = age
        self.address: str = address
        self.active = True

    def __call__(self, *args, **kwds) -> str:
        """
        インスタンスオブジェクトを関数のように呼び出せる
        用途が難しい
        https://stackoverflow.com/questions/3369640/when-is-using-call-a-good-idea

        戻り値:
        ユーザの状態を文字列で返す
        """
        return f"{self.name} is {self.age} years old and lives in {self.address}."

    def __bool__(self) -> bool:
        return bool(self.name and self.age and self.address)

    def __getitem__(self, value) -> Any:
        return getattr(self, value)

    def __del__(self) -> None:
        print(f"Good bye {self.name}({self.age})! See you again 👋")
        self.active = False  # あくまでサンプルとして使用(本番NG)

    def __repr__(self) -> str:
        return f"<User id:{id(self)} name:{self.name}>"

    def __str__(self) -> str:
        return f"{self.name} ({self.age}) - {self.address}"

    def __len__(self) -> int:
        """ユーザ名の長さを返す"""
        return len(self.name)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, User):
            return False
        return self.age == value.age

    def __lt__(self, value: User) -> bool:
        return self.age < value.age

    def __le__(self, value: User) -> bool:
        return self.age <= value.age

    def __gt__(self, value: User) -> bool:
        return self.age > value.age

    def __ge__(self, value: User) -> bool:
        return self.age >= value.age

    def __add__(self, value: int) -> User:
        return User(self.name, self.age + value, self.address)

    def __iadd__(self, value: int) -> User:
        self.age += value
        return self

    # 以降 __sub__や__mul__,__truediv__とかはaddと同じ原理のため、省略


if __name__ == "__main__":
    # user instance
    u = User("taro tanaka", 25, "Japan")
    u2 = User("ichi taro", 51, "Japan")

    # <User id:xxxxx, name:taro tanaka> (コード内、デバッグ用)
    print(repr(u))

    # taro tanaka (25) - Japan 文字列型へ変換(ユーザに見せる用)
    print(u)

    # 11
    print(len(u))

    # False
    print(u == u2)

    # True
    print(u < u2)
    print(u <= u2)

    # False
    print(u > u2)
    print(u >= u2)

    # 新しいオブジェクトとして返す
    u3 = u + 10
    # taro tanaka (25) - Japan taro tanaka (35) - Japan
    print(u, u3)

    # インプレースで書き換える def add()みたいな形と同じ
    u += 1
    # taro tanaka (26) - Japan
    print(u)

    # taro tanaka is 26 years old and lives in Japan.
    print(u())

    # ichi taro
    print(u2["name"])

    # True
    print(bool(u))

    # Good bye xxxxx! See you again 👋
