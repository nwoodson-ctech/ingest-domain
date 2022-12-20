from aws_cdk import (
    Stack,
    aws_sqs as sqs
)
from constructs import Construct


class IngestSQSStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ### Create Ingest SQS Queue ###
        ############ Add SQS Configurations ############
        sqs.Queue(self, id="IngestQueue", queue_name="ingest-sqs-stack-1029")
