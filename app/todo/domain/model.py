"""ドメインオブジェクトを定義するモジュールです。"""

from dataclasses import dataclass, field

from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass
class Todo:
    """Todoのエンティティクラスです。"""

    # https://lidatong.github.io/dataclasses-json/#encode-or-decode-using-a-different-name
    id: str = field(metadata=config(field_name="todo_id"))
    title: str = field(metadata=config(field_name="todo_title"))


@dataclass_json
@dataclass
class User:
    """Userのエンティティクラスです。"""

    id: str = field(metadata=config(field_name="user_id"))
    name: str = field(metadata=config(field_name="user_name"))
