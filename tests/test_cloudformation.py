import unittest
from unittest.mock import patch

import boto3

from lib.aws_cloudformation import CloudFormation


class TestCloudFormation:
    @patch("boto3.client")
    def test_get_stack_resources(self, mock_boto3_client, stack_resources):
        cloudformation = CloudFormation()
        stack_arn = "arn:aws:cloudformation:ap-southeast-2:123456789012:stack/test-app/f9309100-fbc9-11eb-b0cb-0a2fe791cc2c"
        mock_boto3_client(
            "cloudormation"
        ).list_stack_resources.return_value = stack_resources

        resources_ids = ["tag-vbw5n6txuycwq", "port-tm4lmmzdbvvjo", "test-app-logging"]
        assert cloudformation.get_stack_resources(stack_arn) == resources_ids
