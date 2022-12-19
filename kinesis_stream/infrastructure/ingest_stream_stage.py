from constructs import Construct
from aws_cdk import (
    Stage
)
from kinesis_stream.infrastructure.ingest_stream_stack import IngestStreamStack


class IngestStreamStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = IngestStreamStack(self, 'IngestStreamStack')
