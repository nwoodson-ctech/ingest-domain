import json

from aws_lambda_powertools import Logger

logger = Logger(service="SendUpdatePlayerResponseHandler")


@logger.inject_lambda_context
def handler(event, context) -> str:
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from SendUpdatePlayerResponseHandler Lambda!')
    }
