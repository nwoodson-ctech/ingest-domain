from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as python,
    aws_events as events,
    aws_sqs as sqs,
    aws_lambda as lambda_
)
from constructs import Construct


class OrchestrateSQSStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ### Stream Add Player Lambda ###
        orchestration = python.PythonFunction(self, "OrchestrateSQS",
                                              entry="orchestration/lambda_function/runtime",  # required
                                              runtime=_lambda.Runtime.PYTHON_3_8,  # required
                                              index="orchestrate_sqs.py",  # optional, defaults to 'index.py'
                                              handler="handler",
                                              memory_size=256,
                                              function_name="OrchestrateSQS"
                                              )

        ### Retrieve Core Event Bus from event bus name ###
        core_event_bus = events.EventBus.from_event_bus_name(
            self, "CoreEventBus", "CoreEventBus")

        ### Grant Orchestration permissions for Core Event Bus put events ###
        core_event_bus.grant_put_events_to(orchestration)

        ingest_stream = sqs.Queue.from_queue_arn(
            self,
            "ImportIngestSQS",
            "arn:aws:sqs:us-east-1:499104388492:ingest-sqs-stack-1029")

        ingest_stream.grant_read(orchestration)

        event_source_mapping = lambda_.EventSourceMapping(
            self,
            "IngestSQSEventSourceMapping",
            target=orchestration,
            event_source_arn="arn:aws:sqs:us-east-1:499104388492:ingest-sqs-stack-1029",
            starting_position=lambda_.StartingPosition.TRIM_HORIZON)
