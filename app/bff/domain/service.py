"""サービスクラスを定義するモジュールです。"""

from common.domain.model import Todo, User
from common.domain.repository import TodoRepository, UserRepository


class BffService:
    """BFFのサービスクラスです。"""

    def __init__(
        self, todo_repository: TodoRepository, user_repository: UserRepository
    ):
        self.todo_repository = todo_repository
        self.user_repository = user_repository

    def find_todo(self, todo_id: int, user_id: int) -> tuple:
        """todo_idとuser_idが一致するTodoを取得します。"""
        user = self.user_repository.find_one(user_id)
        todo = self.todo_repository.find_one(todo_id)
        return (user, todo)

    def register_user(self, user_name: str) -> User:
        """ユーザを登録します。"""
        return self.user_repository.create_one(user_name)

    def register_todo(self, todo_title: str) -> Todo:
        """Todoを登録します。"""
        return self.todo_repository.create_one(todo_title)
