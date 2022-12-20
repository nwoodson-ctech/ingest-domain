from constructs import Construct
from aws_cdk import (
    Stage
)
from orchestration.lambda_function.infrastructure.orchestrate_sqs_stack import OrchestrateSQSStack


class OrchestrateSQSStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = OrchestrateSQSStack(self, 'OrchestrateSQSStack')
