"""リポジトリクラスを定義するモジュールです。"""
class TodoRepository:
    """Todoのリポジトリインタフェースです。"""
    def __init__(self) -> None:
        pass

    def find_one(self, todo_id: str):
        """ todo_idが一致するTodoを取得します。"""        
        raise NotImplementedError



        
