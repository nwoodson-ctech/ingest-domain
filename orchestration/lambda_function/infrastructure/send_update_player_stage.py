from aws_cdk import (
    Stage
)
from constructs import Construct

from orchestration.lambda_function.infrastructure.send_update_player_stack import SendUpdatePlayerEventStack


class SendUpdatePlayerEventStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        SendUpdatePlayerEventStack(self, 'SendUpdatePlayerEventStack')
