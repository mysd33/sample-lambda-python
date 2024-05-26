"""リポジトリクラスを定義するモジュールです。"""
from domain.model import Todo
from domain.repository import TodoRepository


class TodoRepositoryImpl(TodoRepository):
    """Todoのリポジトリクラスです。"""
    def __init__(self) -> None:
        pass

    def find_one(self, todo_id: str):
        """ todo_idが一致するTodoを取得します。"""
        return Todo(
            id=todo_id,
            #title='dummy title',
            title='ダミーのタイトル',
        )
