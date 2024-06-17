"""リポジトリのREST APIによる実装クラスを定義するモジュールです。"""

import os

import boto3

# TODO: loggerパッケージをappbaseのインタフェースに変更
from aws_lambda_powertools.logging import Logger
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
from common.domain.model import Todo, User
from common.domain.repository import TodoRepository, UserRepository


class UserRepositoryImplForDynamoDB(UserRepository):
    """UserのリポジトリのDynamoDBによる実装クラスです。"""

    def __init__(self, logger: Logger) -> None:
        self.logger = logger
        self.table_name = os.getenv("USERS_TABLE_NAME", "users")

        dynamodb_local_endpoint = os.getenv("DYNAMODB_LOCAL_ENDPOINT", "")
        self.logger.debug(f"dynamodb_local_endpoint: {dynamodb_local_endpoint}")
        if dynamodb_local_endpoint is None or dynamodb_local_endpoint == "":
            self.dynamodb = boto3.client("dynamodb")
        else:
            self.dynamodb = boto3.client(
                "dynamodb", endpoint_url=dynamodb_local_endpoint
            )

    def find_one(self, user_id: str) -> User:
        """todo_idが一致するTodoを取得します。"""
        response = self.dynamodb.get_item(
            TableName=self.table_name, Key={"user_id": {"S": user_id}}
        )
        return User.from_dict(dynamo_to_python(response["Item"]))

    def create_one(self, user: User) -> User:
        """ユーザを登録します。"""
        self.dynamodb.put_item(
            TableName=self.table_name, Item=python_to_dynamo(user.to_dict())
        )
        return user


class TodoRepositoryImplForDynamoDB(TodoRepository):
    """TodoのリポジトリのREST APIによる実装クラスです。"""

    def __init__(self, logger: Logger) -> None:
        self.logger = logger
        self.table_name = os.getenv("TODO_TABLE_NAME", "todo")
        dynamodb_local_endpoint = os.getenv("DYNAMODB_LOCAL_ENDPOINT", "")
        self.logger.info(f"dynamodb_local_endpoint: {dynamodb_local_endpoint}")
        if dynamodb_local_endpoint is None or dynamodb_local_endpoint == "":
            self.logger.info("dynamodb creating")
            self.dynamodb = boto3.client("dynamodb")
            self.logger.info("dynamodb created")
        else:
            self.logger.info("dynamodb creating (local)")
            self.dynamodb = boto3.client(
                "dynamodb", endpoint_url=dynamodb_local_endpoint
            )
            self.logger.info("dynamodb created (local)")

    def find_one(self, todo_id: str) -> Todo:
        """todo_idが一致するTodoを取得します。"""
        response = self.dynamodb.get_item(
            TableName=self.table_name, Key={"todo_id": {"S": todo_id}}
        )
        return Todo.from_dict(dynamo_to_python(response["Item"]))

    def create_one(self, todo: Todo) -> Todo:
        """Todoを登録します。"""
        self.dynamodb.put_item(
            TableName=self.table_name, Item=python_to_dynamo(todo.to_dict())
        )
        return todo

    # TODO: トランザクション管理機能による登録メソッドの実装例追加


def dynamo_to_python(dynamo_object: dict) -> dict:
    deserializer = TypeDeserializer()
    return {k: deserializer.deserialize(v) for k, v in dynamo_object.items()}


def python_to_dynamo(python_object: dict) -> dict:
    serializer = TypeSerializer()
    return {k: serializer.serialize(v) for k, v in python_object.items()}
