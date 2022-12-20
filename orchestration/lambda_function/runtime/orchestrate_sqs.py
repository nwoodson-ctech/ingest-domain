import json
import boto3
from aws_lambda_powertools.utilities.data_classes import event_source, SQSEvent
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

client = boto3.client('events')

logger = Logger(service="OrchestrateStreamAddPlayerEvent")


@event_source(data_class=SQSEvent)
@logger.inject_lambda_context
def handler(event: SQSEvent, context: LambdaContext) -> str:
    # Multiple records can be delivered in a single event
    for record in event.records:
        data = record.body

        logger.info(data)

        add_player_event = {
            'Source': 'ingest-api',
            'DetailType': 'player',
            'Detail': data,
            'EventBusName': 'CoreEventBus'
        }

        logger.info(add_player_event)

        event_bus_event = client.put_events(
            Entries=[add_player_event]
        )

        logger.info(event_bus_event)

    result = {
        "statusCode": 200,
        "headers": {
            "content-type": "application/json"
        }
    }

    return result
