import json
from dataclasses import dataclass, field
from logging import Logger as StdLogger

from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver
from aws_lambda_powertools.logging import Logger, correlation_paths
from aws_lambda_powertools.tracing import Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext
from dataclasses_json import config, dataclass_json
from domain.model import Todo, User
from domain.service import BffService
from infra.repository_impl import TodoRepositoryImpl, UserRepositoryStub

from appbase.component import application_context

try:
    app: APIGatewayRestResolver = application_context.get_api_gateway_rest_resolver()
    logger: Logger = application_context.get_logger()
    tracer: Tracer = application_context.get_tracer()

    # todo_repository = TodoRepositoryStub()
    todo_repository = TodoRepositoryImpl(logger=logger)
    user_repository = UserRepositoryStub()
    service = BffService(
        todo_repository=todo_repository, user_repository=user_repository
    )
except Exception as e:
    # TODO: 初期化時の正しい例外処理の検討
    if logger:
        logger.exception("初期化エラー: %s", e)
    else:
        StdLogger().exception("初期化エラー: %s", e)


@dataclass_json
@dataclass
class FindTodoResponse:
    """Todo取得APIのレスポンス"""

    todo: Todo = field(metadata=config(field_name="Todo"))
    user: User = field(metadata=config(field_name="User"))


@app.get("/bff-api/v1/todo")
@tracer.capture_method
def find_todo():
    """Todo取得API"""
    user_id: str = app.current_event.get_query_string_value(name="user_id")
    todo_id: str = app.current_event.get_query_string_value(name="todo_id")
    logger.debug(f"user_id={user_id}, todo_id={todo_id}")
    # サービスの実行
    result: tuple = service.find_todo(todo_id=todo_id, user_id=user_id)
    response = FindTodoResponse(user=result[0], todo=result[1])
    # 処理結果を返却
    return response.to_json(ensure_ascii=False)


@app.post("/bff-api/v1/users")
@tracer.capture_method
def register_user():
    """ユーザ登録API"""
    request_data: dict = app.current_event.json_body
    # サービスの実行
    user: User = service.register_user(user_name=request_data["user_name"])
    # 処理結果を返却
    return user.to_json(ensure_ascii=False), 201


@app.post("/bff-api/v1/todo")
@tracer.capture_method
def register_todo():
    """Todo登録API"""
    request_data: dict = app.current_event.json_body
    todo: Todo = service.register_todo(todo_title=request_data["todo_title"])
    return todo.to_json(ensure_ascii=False), 201


@app.post("/bff-api/v1/todo-async")
@tracer.capture_method
def register_todo_async():
    """Todo一括登録依頼API"""
    return {"message": "create todo async"}


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context: LambdaContext) -> dict:
    """Lambdaハンドラ"""
    return app.resolve(event, context)
