from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines,
    SecretValue
)

from apigateway.infrastructure.apigateway_stage import ApigatewayStage
from kinesis_stream.infrastructure.ingest_stream_stage import IngestStreamStage
from orchestration.lambda_function.infrastructure.orchestrate_stream_stage import OrchestrateStreamStage
from sqs.infrastructure.ingest_sqs_stage import IngestSQSStage
from orchestration.lambda_function.infrastructure.orchestrate_sqs_stage import OrchestrateSQSStage
from orchestration.lambda_function.infrastructure.send_update_player_stage import SendUpdatePlayerEventStage

class PipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        code_pipeline = pipelines.CodePipeline(
            self,
            'IngestDomain-Pipeline',
            docker_enabled_for_synth=True,
            synth=pipelines.ShellStep('Synth',
                                      input=pipelines.CodePipelineSource.git_hub(
                                          'nwoodson-ctech/ingest-domain',
                                          'main',
                                          authentication=SecretValue.secrets_manager(
                                              'exploration-token')
                                      ),
                                      env={'privileged': 'True'},
                                      commands=[
                                          "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                                          # Instructs Codebuild to install required packages
                                          "pip3 install -r requirements.txt",
                                          "cdk synth"
                                      ]
                                      )
        )

        wave = code_pipeline.add_wave("wave")

        wave.add_stage(ApigatewayStage(self, "DeployApigateway"))
        wave.add_stage(IngestStreamStage(self, "DeployIngestStream"))
        wave.add_stage(IngestSQSStage(self, "DeployIngestSQS"))

        wave2 = code_pipeline.add_wave("wave2")

        wave2.add_stage(OrchestrateStreamStage(self, "DeployOrchestration"))
        wave2.add_stage(OrchestrateSQSStage(self, "DeployOrchestrateSQS"))
        wave2.add_stage(SendUpdatePlayerEventStage(self, "DeploySendUpdatePlayerEvent"))

