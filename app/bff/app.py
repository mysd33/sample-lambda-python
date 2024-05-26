import json

import requests
from aws_lambda_powertools import Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import Logger, correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from domain.service import BffService
from infra.repository_impl import TodoRepositoryImpl

app = APIGatewayRestResolver()
logger = Logger(log_uncaught_exceptions=True)
tracer = Tracer()

repository = TodoRepositoryImpl()
service = BffService(repository=repository)

@app.get("/bff-api/v1/todo")
@tracer.capture_method
def get_todo():
    user_id: str = app.current_event.get_query_string_value(name="user_id")    
    todo_id: str = app.current_event.get_query_string_value(name="todo_id")
    logger.info(f"user_id={user_id}, todo_id={todo_id}")
    # サービスの実行
    result = service.find_todo(todo_id=todo_id)    
    # 処理結果を返却    
    return json.dumps(result.__dict__, ensure_ascii=False)

@app.post("/bff-api/v1/users")
@tracer.capture_method
def create_user():
    return {"message": "create user"}

@app.post("/bff-api/v1/todo")
@tracer.capture_method
def create_todo():
    return {"message": "create todo"}

@app.post("/bff-api/v1/todo-async")
@tracer.capture_method
def create_todo_async():
    return {"message": "create todo async"}

@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context: LambdaContext):
    return app.resolve(event, context)    

