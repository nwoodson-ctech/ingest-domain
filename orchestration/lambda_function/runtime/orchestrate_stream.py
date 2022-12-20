import json
import boto3
from aws_lambda_powertools.utilities.data_classes import event_source, KinesisStreamEvent
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

client = boto3.client('events')

logger = Logger(service="OrchestrateStreamAddPlayerEvent")


@event_source(data_class=KinesisStreamEvent)
@logger.inject_lambda_context
def handler(event: KinesisStreamEvent, context: LambdaContext) -> str:
    kinesis_record = next(event.records).kinesis

    # if data was delivered as json
    data = kinesis_record.data_as_json()

    add_player_event = {
        'Source': 'ingest-api',
        'DetailType': 'player',
        'Detail': json.dumps(data),
        'EventBusName': 'CoreEventBus'
    }

    logger.info(add_player_event)

    event_bus_event = client.put_events(
        Entries=[add_player_event]
    )

    result = {
        "statusCode": 200,
        "headers": {
            "content-type": "application/json"
        },
        "body": event_bus_event
    }

    logger.info(result)

    return result
