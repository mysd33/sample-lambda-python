"""ドメインオブジェクトを定義するモジュールです。"""
import dataclasses


@dataclasses.dataclass
class Todo:
    """Todoのエンティティクラスです。"""
    id: int
    title: str
