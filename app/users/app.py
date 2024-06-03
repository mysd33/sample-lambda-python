import uuid
from logging import Logger as StdLogger

from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver
from aws_lambda_powertools.logging import Logger, correlation_paths
from aws_lambda_powertools.tracing import Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext
from common.domain.model import User

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


@app.get("/users-api/v1/users/<user_id>")
@tracer.capture_method
def find_user_by_id(user_id: str):
    """ユーザ情報取得API"""
    logger.debug("find user by id: %s", user_id)

    # TODO: dummy response
    user = User(
        id=user_id,
        name="ダミーのユーザ名",
    )

    return user.to_json(ensure_ascii=False)


@app.post("/users-api/v1/users")
@tracer.capture_method
def register_user():
    """ユーザ情報登録API"""
    request_data: dict = app.current_event.json_body
    logger.debug("register user user_name: %s", request_data["user_name"])
    # TODO: dummy response
    user = User(
        id=str(uuid.uuid4()),
        name=request_data["user_name"],
    )
    return user.to_json(ensure_ascii=False), 201


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context: LambdaContext) -> dict:
    """Lambdaハンドラ"""
    return app.resolve(event, context)
