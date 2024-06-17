"""リポジトリインタフェースを定義するモジュールです。"""

from .model import Todo, User


class UserRepository:
    """Userのリポジトリインタフェースです。"""

    def __init__(self) -> None:
        pass

    def find_one(self, user_id: str) -> User:
        """user_idが一致するUserを取得します。"""
        raise NotImplementedError

    def create_one(self, user: User) -> User:
        """ユーザを登録します。"""
        raise NotImplementedError


class TodoRepository:
    """Todoのリポジトリインタフェースです。"""

    def __init__(self) -> None:
        pass

    def find_one(self, todo_id: str) -> Todo:
        """todo_idが一致するTodoを取得します。"""
        raise NotImplementedError

    def create_one(self, todo: Todo) -> Todo:
        """Todoを登録します。"""
        raise NotImplementedError
