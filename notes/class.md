### Python 特殊メソッド

#### カテゴリ

- 表示系: `__repr__`, `__str__`, etc
- 比較系: `__eq__`, `__lt__`, etc
- 算術系: `__add__`, `__sub__`, etc
- イテラブル・コンテナ系: `__len__`, `__iter__`, etc
- その他: `__call__`, `__del__` etc

### 注意

- `__del__`はタイミングの保証はない(GC がいつ呼ぶかは未定。循環参照がある場合は呼ばれないこともあるため注意)

### 資料

[特殊メソッド](https://docs.python.org/ja/3.13/reference/datamodel.html#special-method-names)

[snippets-special_methods](https://github.com/akagikouzanh/python-snippets-hub/blob/master/snippets/snippets_class_special_methods.py)
