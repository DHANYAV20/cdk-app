import aws_cdk.aws_s3 as _s3
from aws_cdk.core import Stack
from constructs import Construct

class CdkAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkAppQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="myfirstcdkproject252",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access = _s3.BlockPublicAccess.BLOCK_ALL
        )
