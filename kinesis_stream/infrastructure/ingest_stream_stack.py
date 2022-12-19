from aws_cdk import (
    Stack,
    aws_kinesis as kinesis
)
from constructs import Construct


class IngestStreamStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ### Create Ingest Kinesis Stream ###
        ############ Add Kinesis Configurations ############
        kinesis.Stream(self, "IngestStream",
                       stream_name="ingest-stream"
                       )
