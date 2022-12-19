from constructs import Construct
from aws_cdk import (
    Stage
)
from orchestration.lambda_function.infrastructure.orchestrate_stream_stack import OrchestrateStreamStack


class OrchestrateStreamStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = OrchestrateStreamStack(self, 'OrchestrateStreamStack')
