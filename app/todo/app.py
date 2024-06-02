import json
from logging import Logger as StdLogger

from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver
from aws_lambda_powertools.logging import Logger, correlation_paths
from aws_lambda_powertools.tracing import Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext
from domain.model import Todo

from appbase.component import application_context

try:
    app: APIGatewayRestResolver = application_context.get_api_gateway_rest_resolver()
    logger: Logger = application_context.get_logger()
    tracer: Tracer = application_context.get_tracer()
except Exception as e:
    # TODO: 初期化時の正しい例外処理の検討
    if logger:
        logger.exception("初期化エラー: %s", e)
    else:
        StdLogger().exception("初期化エラー: %s", e)


@app.get("/todo-api/v1/todo/<todo_id>")
@tracer.capture_method
def find_todo_by_id(todo_id: str):
    """Todo取得API"""
    logger.debug("find todo by id: %s", todo_id)

    # TODO: dummy response
    todo = Todo(
        id=todo_id,
        title="Buy Milk",
    )
    return todo.to_json()


@app.post("/todo-api/v1/todo")
@tracer.capture_method
def register_todo():
    """Todo登録API"""
    logger.debug("register todo")

    # TODO: dummy response
    todo = Todo(
        id="daac7b7b-1fef-11ef-b357-0242ac110003",
        title="Buy Milk",
    )
    return todo.to_json(), 201


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context: LambdaContext) -> dict:
    """Lambdaハンドラ"""
    return app.resolve(event, context)
