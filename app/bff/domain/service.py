"""サービスクラスを定義するモジュールです。"""
from .repository import TodoRepository


class BffService:
    """BFFのサービスクラスです。"""

    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def find_todo(self, todo_id: int):
        """ todo_idが一致するTodoを取得します。"""
        return self.repository.find_one(todo_id)
        #return Todo(id=todo_id, title="title")
