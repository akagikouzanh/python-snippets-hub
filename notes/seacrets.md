### seacrets

`seacrets`は、セキュリティ目的で使用する乱数生成やトークン生成などで使用する Python の標準ライブラリ。

- random モジュールよりもセキュア(=暗号学的で安全)
- 主な使用用途

  - パスワードリセットや API キーや一時的な URL や短縮 URL のためのキー生成
  - ワンタイム パスワードや一時的なパスワードの生成
  - ランダムなトークン生成

- 注意

  - 復元できる形式でパスワードの保存は NG

### 資料

[secrets --- 機密を扱うために安全な乱数を生成する](https://docs.python.org/ja/3/library/secrets.html#module-secrets)

[snippets](https://github.com/akagikouzanh/python-snippets-hub/blob/master/snippets/snippets_secrets.py)
