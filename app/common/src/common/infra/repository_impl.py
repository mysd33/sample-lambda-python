"""リポジトリクラスを定義するモジュールです。"""

import os
import uuid

import requests

# TODO: loggerパッケージをappbaseのインフェースに変更
from aws_lambda_powertools.logging import Logger
from common.domain.model import Todo, User
from common.domain.repository import TodoRepository, UserRepository


class TodoRepositoryImpl(TodoRepository):
    """Todoのリポジトリの実装クラスです。"""

    def __init__(self, logger: Logger) -> None:
        self.logger = logger
        # TODO: プロパティ管理（AppConfig対応）機能を使うように修正する
        self.todo_api_base_url = os.getenv(
            "TODO_API_BASE_URL", "http://host.docker.internal:3000"
        )

    def find_one(self, todo_id: str) -> Todo:
        """todo_idが一致するTodoを取得します。"""
        todo_api_url = f"{self.todo_api_base_url}/todo-api/v1/todo/{todo_id}"
        self.logger.debug("todo_api_url: %s", todo_api_url)
        # API呼び出し
        try:
            response = requests.get(todo_api_url)
            response.raise_for_status()
            data = response.text
        except Exception as e:
            self.logger.exception("リクエストエラー: %s", e)
            raise e

        self.logger.debug("response_json: %s", data)
        return Todo.from_json(data)

    def create_one(self, todo_title: str) -> Todo:
        """Todoを登録します。"""
        todo_api_url = f"{self.todo_api_base_url}/todo-api/v1/todo"
        self.logger.debug("todo_api_url: %s", todo_api_url)
        # API呼び出し
        try:
            response = requests.post(
                todo_api_url,
                json={"todo_title": todo_title},
            )
            response.raise_for_status()
            data = response.text
        except Exception as e:
            # TODO: 例外処理の検討
            self.logger.exception("リクエストエラー: %s", e)
            raise e

        self.logger.debug("response_json: %s", data)
        return Todo.from_json(data)


class TodoRepositoryStub(TodoRepository):
    """Todoのリポジトリのスタブクラスです。"""

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
    """Userのリポジトリのスタブクラスです。"""

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
