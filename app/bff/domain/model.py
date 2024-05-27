"""ドメインオブジェクトを定義するモジュールです。"""

import dataclasses


@dataclasses.dataclass
class Todo:
    """Todoのエンティティクラスです。"""

    id: str
    title: str


@dataclasses.dataclass
class User:
    """Userのエンティティクラスです。"""

    id: str
    name: str
