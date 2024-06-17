"""リポジトリのREST APIによる実装クラスを定義するモジュールです。"""

import os

import requests

# TODO: loggerパッケージをappbaseのインタフェースに変更
from aws_lambda_powertools.logging import Logger
from common.domain.model import Todo, User
from common.domain.repository import TodoRepository, UserRepository


class UserRepositoryImplForRestAPI(UserRepository):
    """UserのリポジトリのREST APIによる実装クラスです。"""

    def __init__(self, logger: Logger) -> None:
        self.logger = logger
        # TODO: プロパティ管理（AppConfig対応）機能を使うように修正する
        self.users_api_base_url = os.getenv(
            "USERS_API_BASE_URL", "http://host.docker.internal:3000"
        )

    def find_one(self, user_id: str) -> User:
        """todo_idが一致するTodoを取得します。"""
        user_api_url = f"{self.users_api_base_url}/users-api/v1/users/{user_id}"
        self.logger.debug("user_api_url: %s", user_api_url)
        # API呼び出し
        try:
            response = requests.get(user_api_url)
            response.raise_for_status()
            data = response.text
        except Exception as e:
            # TODO: 例外処理の検討
            self.logger.exception("リクエストエラー: %s", e)
            raise e

        self.logger.debug("response_json: %s", data)
        return User.from_json(data)

    def create_one(self, user: User) -> User:
        """ユーザを登録します。"""
        user_api_url = f"{self.users_api_base_url}/users-api/v1/users"
        self.logger.debug("user_api_url: %s", user_api_url)
        # API呼び出し
        try:
            response = requests.post(
                user_api_url,
                # TODO: データクラスからディクショナリ変換する
                json={"user_name": user.name},
            )
            response.raise_for_status()
            data = response.text
        except Exception as e:
            # TODO: 例外処理の検討
            self.logger.exception("リクエストエラー: %s", e)
            raise e

        self.logger.debug("response_json: %s", data)
        return User.from_json(data)


class TodoRepositoryImplForRestAPI(TodoRepository):
    """TodoのリポジトリのREST APIによる実装クラスです。"""

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
            # TODO: 例外処理の検討
            self.logger.exception("リクエストエラー: %s", e)
            raise e

        self.logger.debug("response_json: %s", data)
        return Todo.from_json(data)

    def create_one(self, todo: Todo) -> Todo:
        """Todoを登録します。"""
        todo_api_url = f"{self.todo_api_base_url}/todo-api/v1/todo"
        self.logger.debug("todo_api_url: %s", todo_api_url)
        # API呼び出し
        try:
            response = requests.post(
                todo_api_url,
                # TODO: データクラスからディクショナリ変換する
                json={"todo_title": todo.title},
            )
            response.raise_for_status()
            data = response.text
        except Exception as e:
            # TODO: 例外処理の検討
            self.logger.exception("リクエストエラー: %s", e)
            raise e

        self.logger.debug("response_json: %s", data)
        return Todo.from_json(data)
