"""ソフトウェアフレームワークをapplication_contextモジュール"""

from aws_lambda_powertools import Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import Logger

from appbase.dynamodb import dynamodb_client


class ApplicationContext:
    """アプリケーションコンテキスト"""

    def __init__(self):
        self._api_gateway_rest_resolver = APIGatewayRestResolver()
        self._logger = Logger(log_uncaught_exceptions=True)
        self._tracer = Tracer()
        self._dynamodb_client = dynamodb_client.create_dynamodb_client(
            logger=self._logger
        )

    def get_api_gateway_rest_resolver(self) -> APIGatewayRestResolver:
        """APIGatewayRestResolverを取得します"""
        return self._api_gateway_rest_resolver

    def get_logger(self) -> Logger:
        """Loggerを取得します"""
        return self._logger

    def get_tracer(self) -> Tracer:
        """Tracerを取得します"""
        return self._tracer

    def get_dynamodb_client(self):
        """DynamoDBClientを取得します"""
        return self._dynamodb_client


# def get_api_gateway_rest_resolver() -> APIGatewayRestResolver:
#    """APIGatewayRestResolverを取得します"""
#    return APIGatewayRestResolver()


# def get_logger() -> Logger:
#    """Loggerを取得します"""
# TODO: メッセージIDに基づくLoggerインタフェースに置き換える
#    return Logger(log_uncaught_exceptions=True)


# def get_tracer() -> Tracer:
#    """Tracerを取得します"""
#    return Tracer()
