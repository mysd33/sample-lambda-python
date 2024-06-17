"""リポジトリのREST APIによる実装クラスを定義するモジュールです。"""

import os

import boto3

# TODO: loggerパッケージをappbaseのインタフェースに変更
from aws_lambda_powertools.logging import Logger
from common.domain.model import Todo, User
from common.domain.repository import TodoRepository, UserRepository

from appbase.dynamodb.utils import dynamo_to_python, python_to_dynamo


class UserRepositoryImplForDynamoDB(UserRepository):
    """UserのリポジトリのDynamoDBによる実装クラスです。"""

    def __init__(self, logger: Logger, dynamodb_client) -> None:
        self.logger = logger
        self.table_name = os.getenv("USERS_TABLE_NAME", "users")
        self.dynamodb_client = dynamodb_client

    def find_one(self, user_id: str) -> User:
        """todo_idが一致するTodoを取得します。"""
        response = self.dynamodb_client.get_item(
            TableName=self.table_name, Key={"user_id": {"S": user_id}}
        )
        return User.from_dict(dynamo_to_python(response["Item"]))

    def create_one(self, user: User) -> User:
        """ユーザを登録します。"""
        self.dynamodb_client.put_item(
            TableName=self.table_name, Item=python_to_dynamo(user.to_dict())
        )
        return user


class TodoRepositoryImplForDynamoDB(TodoRepository):
    """TodoのリポジトリのREST APIによる実装クラスです。"""

    def __init__(self, logger: Logger, dynamodb_client) -> None:
        self.logger = logger
        self.table_name = os.getenv("TODO_TABLE_NAME", "todo")
        self.dynamodb_client = dynamodb_client

    def find_one(self, todo_id: str) -> Todo:
        """todo_idが一致するTodoを取得します。"""
        response = self.dynamodb_client.get_item(
            TableName=self.table_name, Key={"todo_id": {"S": todo_id}}
        )
        return Todo.from_dict(dynamo_to_python(response["Item"]))

    def create_one(self, todo: Todo) -> Todo:
        """Todoを登録します。"""
        self.dynamodb_client.put_item(
            TableName=self.table_name, Item=python_to_dynamo(todo.to_dict())
        )
        return todo

    # TODO: トランザクション管理機能による登録メソッドの実装例追加
