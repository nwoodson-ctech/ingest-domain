import base64
import json
import boto3

client = boto3.client('events')


def handler(event, context):
    print(event[0])

    for payload in event:
        stream_data = json.loads(base64.b64decode(payload["data"]).decode("utf-8"))
        event_bus_event = client.put_events(
            Entries={
                'Source': 'ingest-api',
                'DetailType': 'player',
                'Detail': stream_data,
                'EventBusName': 'CoreEventBus'
            }
        )
        result = {
            "statusCode": 200,
            "headers": {
                "content-type": "application/json"
            },
            "body": event_bus_event
        }

        print(json.dumps(result))

        return result
