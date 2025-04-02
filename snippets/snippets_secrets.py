"""
example secrets

usage: python snippets/snippets_secrets.py
"""

import string

import secrets
from urllib import parse

# 特定のシーケンスからランダムに要素を選択
alpha_num: str = string.ascii_letters + string.digits
print(alpha_num)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

password: str = "".join(secrets.choice(alpha_num) for i in range(8))
print(f"password: {password}, len:{len(password)}")
# random 8 length password


# トークンの生成
# 一時的なパスワードリセット用のトークン、推測しづらいURLの生成で使用
# nbytesを含むbyte文字列を返す、指定がない場合デフォルトサイズを使用する(default=32)
print(secrets.token_bytes())

# 16進数のランダムなテキストを返す、指定がない場合デフォルトサイズを使用する(default=64)
print(secrets.token_hex())

# ランダムなbyteを持つURLテキストを返す、指定がない場合デフォルトサイズを使用する(default=43)
print(secrets.token_urlsafe())

# トークン検証(「タイミング攻撃」のリスクを低減した定数時間比較で行われる)
# 「タイミング攻撃」= 処理にかかる時間差を分析し情報を盗み取る攻撃(比較の時間を同一時間で終わるようにする必要がある)
reset_token: str = secrets.token_urlsafe()
url: str = "https://snippets_secrets.com/?reset=" + reset_token
print(url)

url_parse = parse.urlparse(url)
url_query = parse.parse_qs(url_parse.query)
print(url_query)
print(secrets.compare_digest(reset_token, url_query["reset"][0]))
