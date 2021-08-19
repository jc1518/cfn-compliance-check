import json
from unittest.mock import patch

from cfn_compliance_check import is_valid_arn, cfn_compliance_check


class TestCfnCompliancCheck:
    def test_is_valid_arn(self):
        valid_arn = "arn:aws:cloudformation:ap-southeast-2:123456789012:stack/test-app/f9309100-fbc9-11eb-b0cb-0a2fe791cc2c"
        invalid_arn = "test-app"
        assert is_valid_arn(valid_arn) == True
        assert is_valid_arn(invalid_arn) == False

    @patch("lib.cloud_conformity.CloudConformity.get_aws_account_cc_id")
    @patch("lib.cloud_conformity.CloudConformity.get_resource_failed_checks")
    @patch("lib.aws_cloudformation.CloudFormation.get_stack_resources")
    def test_cfn_compliance_check(
        self,
        mock_cloudformation_get_stack_resources,
        mock_confomrity_get_resource_failed_checks,
        mock_confomrity_get_aws_account_cc_id,
        resource_failed_checks,
    ):
        mock_confomrity_get_aws_account_cc_id.return_value = "2222222222"
        mock_cloudformation_get_stack_resources.return_value = ["test-app-logging"]
        mock_confomrity_get_resource_failed_checks.return_value = resource_failed_checks

        checks_summary = cfn_compliance_check(
            "arn:aws:cloudformation:ap-southeast-2:123456789012:stack/test-app/f9309100-fbc9-11eb-b0cb-0a2fe791cc2c"
        )
        assert checks_summary == [
            "Medium: (S3 Bucket) Bucket test-app-logging does not enforce SSL to secure data in transit"
        ]
