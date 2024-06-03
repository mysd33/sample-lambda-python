from logging import Logger as StdLogger

from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver
from aws_lambda_powertools.logging import Logger, correlation_paths
from aws_lambda_powertools.tracing import Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext
from common.infra.repository_stub import TodoRepositoryStub
from domain.service import TodoService

from appbase.component import application_context

try:
    app: APIGatewayRestResolver = application_context.get_api_gateway_rest_resolver()
    logger: Logger = application_context.get_logger()
    tracer: Tracer = application_context.get_tracer()
    todo_repository = TodoRepositoryStub()
    service = TodoService(todo_repository=todo_repository)

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

    todo = service.find_todo(todo_id)
    return todo.to_json(ensure_ascii=False)


@app.post("/todo-api/v1/todo")
@tracer.capture_method
def register_todo():
    """Todo登録API"""
    request_data: dict = app.current_event.json_body
    logger.debug("register todo todo_title: %s", request_data["todo_title"])

    todo = service.register_todo(todo_title=request_data["todo_title"])
    return todo.to_json(ensure_ascii=False), 201


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context: LambdaContext) -> dict:
    """Lambdaハンドラ"""
    return app.resolve(event, context)
