from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as python
)
from constructs import Construct


class SendUpdatePlayerEventStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        send_update_player_event = python.PythonFunction(self, "SendUpdatePlayerEvent",
                                                         entry="orchestration/lambda_function/runtime",  # required
                                                         runtime=_lambda.Runtime.PYTHON_3_8,  # required
                                                         index="send_update_player_event.py",
                                                         # optional, defaults to 'index.py'
                                                         handler="handler",
                                                         memory_size=256,
                                                         function_name="SendUpdatePlayerEvent"
                                                         )

        principal = iam.ServicePrincipal("events.amazonaws.com")
        send_update_player_event.grant_invoke(principal)
