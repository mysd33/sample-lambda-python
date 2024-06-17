"""リポジトリのスタブを定義するモジュールです。"""

import uuid

# TODO: loggerパッケージをappbaseのインタフェースに変更
from aws_lambda_powertools.logging import Logger
from common.domain.model import Todo, User
from common.domain.repository import TodoRepository, UserRepository


class UserRepositoryStub(UserRepository):
    """Userのリポジトリのスタブクラスです。"""

    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def find_one(self, user_id: str) -> User:
        """user_idが一致するUserを取得します。"""
        return User(
            id=user_id,
            name="ダミーの名前",
        )

    def create_one(self, user: User) -> User:
        """ユーザを登録します。"""
        return user


class TodoRepositoryStub(TodoRepository):
    """Todoのリポジトリのスタブクラスです。"""

    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def find_one(self, todo_id: str) -> Todo:
        """todo_idが一致するTodoを取得します。"""
        return Todo(
            id=todo_id,
            title="ダミーのタイトル",
        )

    def create_one(self, todo: Todo) -> Todo:
        """Todoを登録します。"""
        return todo
