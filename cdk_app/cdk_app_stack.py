import aws_cdk.aws_s3 as _s3
from aws_cdk.core import Stack
from constructs import Construct
import aws_cdk.core as core
class CdkAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="myfirstcdkproject252",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access = _s3.BlockPublicAccess.BLOCK_ALL
        )
        mybucket =  _s3.Bucket(
            self,
            "myBucketId1"
        )

        snstopicname = "abczys1234"

        if not core.Token.is_unresolved(snstopicname) and len(snstopicname) > 10:
            raise ValueError("Maximum value can be only 18 characters")

        print(mybucket.bucket_name)

        output_1 = core.CfnOutput(
            self,
            "myBucketOutput1",
            value=mybucket.bucket_name,
            description=f"My first CDK Bucket",
            export_name="myBucketOutput1"
        )


