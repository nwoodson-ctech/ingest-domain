from constructs import Construct
from aws_cdk import (
    Stage
)
from sqs.infrastructure.ingest_sqs_stack import IngestSQSStack


class IngestSQSStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = IngestSQSStack(self, 'IngestSQSStack')
