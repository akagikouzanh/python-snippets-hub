"""
example collections deque

Usage:
    snippets_collections_deque.py

See also:
https://docs.python.org/ja/3.13/library/collections.html#collections.deque
"""

from collections import deque


if __name__ == "__main__":
    dq = deque("git")
    for el in dq:
        # GIT
        print(el.upper())

    # 右側(末尾)への追加
    dq.append("h")
    # deque(['g', 'i', 't', 'h'])
    print(dq)

    # 左側(先頭)への追加
    dq.appendleft("hello")
    # deque(['hello', 'g', 'i', 't', 'h'])
    print(dq)

    # iterableから得られる要素を右側(末尾)へ追加拡張
    dq.extend("ub")
    # deque(['hello', 'g', 'i', 't', 'h', 'u', 'b'])
    print(dq)

    # iterableから得られる要素を左側(先頭)へ追加拡張
    dq.extendleft("world")
    # deque(['d', 'l', 'r', 'o', 'w', 'hello', 'g', 'i', 't', 'h', 'u', 'b'])
    print(dq)

    # 右へ一個ずつずらす(=dq.appendleft(d.pop))
    dq.rotate(1)
    # deque(['b', 'd', 'l', 'r', 'o', 'w', 'hello', 'g', 'i', 't', 'h', 'u'])
    print(dq)

    # 左へ一個ずつずらす(=dq.append(d.popleft()))
    dq.rotate(-2)
    # deque(['l', 'r', 'o', 'w', 'hello', 'g', 'i', 't', 'h', 'u', 'b', 'd'])
    print(dq)

    dq.pop()
    dq.popleft()
    # deque(['r', 'o', 'w', 'hello', 'g', 'i', 't', 'h', 'u', 'b'])
    print(dq)

    dq.clear()
    # deque([])
    print(dq)

    dq_fixed = deque("python", maxlen=5)
    # deque(['y', 't', 'h', 'o', 'n'], maxlen=5)
    print(dq_fixed)
