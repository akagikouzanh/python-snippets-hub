"""
example unicodedata
https://www.unicode.org/reports/tr44/

usage: python snippets/snippets_unicodedata.py
"""

import unicodedata

# unicode文字と文字の名称を変換する
# ⛩ / データがない場合はKeyErrorになる(defaultを指定していればそれが返される)
print(unicodedata.lookup("SHINTO SHRINE"))
# CURRY AND RICE / データがない場合はValueErrorになる(defaultを指定していればそれが返される)
print(unicodedata.name("🍛"))

# unicode文字列の正規化
# 半角全角の文字を全角に統一したりするといった用途で使用する
# https://ja.wikipedia.org/wiki/Unicode%E6%AD%A3%E8%A6%8F%E5%8C%96
print(unicodedata.normalize("NFC", "アｱ"))
print(unicodedata.normalize("NFKC", "アｱ"))
print(unicodedata.normalize("NFD", "ガ"))
nfd = unicodedata.normalize("NFD", "ガ")
nfc = unicodedata.normalize("NFC", "ガ")
nfkc = unicodedata.normalize("NFKC", "ガ")
nfkd = unicodedata.normalize("NFKD", "ガ")

# 同一に見える
# ガ ガ
print(nfd, nfkc, nfkd)

# 実際は違う
# b'\xe3\x82\xac' : b'\xe3\x82\xab\xe3\x82\x99'
print(
    "\n".join(
        f"{name}={val.encode('utf-8')!r}"
        for name, val in zip(["NFD", "NFKD", "NFC", "NFKC"], [nfd, nfkd, nfc, nfkc])
    )
)

# カ
print(nfkd.encode("utf-8")[:3].decode("utf-8"))
# 濁点
print(nfkd.encode("utf-8")[3:].decode("utf-8"))

# NFD/NFKD = バラす(ガで試したように文字をバラす)
# NFC/NFKC = まとめる(アｱで試したように文字をまとめる)
# NFK系 = 似てたらまとめる
