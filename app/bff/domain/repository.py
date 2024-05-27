"""リポジトリクラスを定義するモジュールです。"""

from .model import Todo, User


class TodoRepository:
    """Todoのリポジトリインタフェースです。"""

    def __init__(self) -> None:
        pass

    def find_one(self, todo_id: str) -> tuple:
        """todo_idが一致するTodoを取得します。"""
        raise NotImplementedError

    def create_one(self, todo_title: str) -> Todo:
        """Todoを登録します。"""
        raise NotImplementedError


class UserRepository:
    """Userのリポジトリインタフェースです。"""

    def __init__(self) -> None:
        pass

    def find_one(self, user_id: str) -> User:
        """user_idが一致するUserを取得します。"""
        raise NotImplementedError

    def create_one(self, user_name: str) -> User:
        """ユーザを登録します。"""
        raise NotImplementedError
