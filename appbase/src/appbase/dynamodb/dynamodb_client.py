"""DynamoDBアクセス機能を提供するモジュールです。"""

import os

import boto3

# TODO: loggerパッケージをappbaseのインタフェースに変更
from aws_lambda_powertools.logging import Logger


def create_dynamodb_client(logger: Logger):
    """DynamoDBクライアントを生成します。"""
    dynamodb_local_endpoint = os.getenv("DYNAMODB_LOCAL_ENDPOINT", "")
    logger.debug(f"dynamodb_local_endpoint: {dynamodb_local_endpoint}")
    if dynamodb_local_endpoint is None or dynamodb_local_endpoint == "":
        return boto3.client("dynamodb")
    else:
        return boto3.client("dynamodb", endpoint_url=dynamodb_local_endpoint)
