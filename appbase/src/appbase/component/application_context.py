"""ソフトウェアフレームワークをapplication_contextモジュール"""

from aws_lambda_powertools import Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import Logger, correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext


def get_api_gateway_rest_resolver() -> APIGatewayRestResolver:
    """APIGatewayRestResolverを取得します"""
    return APIGatewayRestResolver()


def get_logger() -> Logger:
    """Loggerを取得します"""
    # TODO: メッセージIDに基づくLoggerインタフェースに置き換える
    return Logger(log_uncaught_exceptions=True)


def get_tracer() -> Tracer:
    """Tracerを取得します"""
    return Tracer()
