"""
example collections chainmap

Usage:
    python snippets_collections_chainmap.py

See also:
https://docs.python.org/ja/3.13/library/collections.html#collections.ChainMap
"""

from collections import ChainMap


if __name__ == "__main__":
    # 元の各辞書をコピーせず、優先順位付きで束ねてアクセスできる
    # （注）値の取得は優先順に行われるが、ChainMap自体は参照なので、書き込み時は元の辞書が直接変更される点に注意

    global_var = {"user": "taro"}
    local_var = {"user": "hanako"}
    default_var = {"user": "jiro"}

    cm = ChainMap(default_var, global_var, local_var)
    print(cm)  # ChainMap({'user': 'jiro'}, {'user': 'taro'}, {'user': 'hanako'})

    cm["user"] = "二郎"
    new_cm = cm.new_child({"user": "saburo"})
    print(cm)  # ChainMap({'user': '二郎'}, {'user': 'taro'}, {'user': 'hanako'})

    # ChainMap({'user': 'saburo'}, {'user': '二郎'}, {'user': 'taro'}, {'user': 'hanako'})
    print(new_cm)

    # ChainMap({'user': '二郎'}, {'user': 'taro'}, {'user': 'hanako'})
    print(new_cm.parents)

    new_cm.maps[3]["user"] = "花子"
    # ChainMap({'user': 'saburo'}, {'user': '二郎'}, {'user': 'taro'}, {'user': '花子'})
    print(new_cm)
