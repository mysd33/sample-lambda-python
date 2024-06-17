"""サービスクラスを定義するモジュールです。"""

import uuid

from common.domain.model import Todo
from common.domain.repository import TodoRepository


class TodoService:
    """Todoのサービスクラスです。"""

    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    def find_todo(self, todo_id: int) -> Todo:
        """todo_idが一致するTodoを取得します。"""
        return self.todo_repository.find_one(todo_id)

    def register_todo(self, todo_title: str) -> Todo:
        """Todoを登録します。"""
        return self.todo_repository.create_one(
            Todo(id=str(uuid.uuid4()), title=todo_title)
        )
