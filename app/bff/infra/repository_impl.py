"""リポジトリクラスを定義するモジュールです。"""

import uuid

from domain.model import Todo, User
from domain.repository import TodoRepository, UserRepository


class TodoRepositoryStub(TodoRepository):
    """Todoのリポジトリクラスです。"""

    def __init__(self) -> None:
        pass

    def find_one(self, todo_id: str) -> Todo:
        """todo_idが一致するTodoを取得します。"""
        return Todo(
            id=todo_id,
            title="ダミーのタイトル",
        )

    def create_one(self, todo_title: str) -> Todo:
        """Todoを登録します。"""
        return Todo(
            id=str(uuid.uuid4()),
            title=todo_title,
        )


class UserRepositoryStub(UserRepository):
    """Userのリポジトリクラスです。"""

    def __init__(self) -> None:
        pass

    def find_one(self, user_id: str) -> User:
        """user_idが一致するUserを取得します。"""
        return User(
            id=user_id,
            name="ダミーの名前",
        )

    def create_one(self, user_name: str) -> User:
        """ユーザを登録します。"""
        return User(
            id=str(uuid.uuid4()),
            name=user_name,
        )
