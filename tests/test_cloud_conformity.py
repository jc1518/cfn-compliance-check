import json
import os
import unittest
from unittest.mock import patch


from lib.cloud_conformity import CloudConformity

cloudconformity = CloudConformity()


class TestCloudConformity:
    @patch("lib.cloud_conformity.CloudConformity._get_request")
    def test_get_all_accounts(self, mock_get_request, cc_all_accounts):
        mock_get_request.return_value = json.dumps(cc_all_accounts)
        accounts = cloudconformity.get_all_accounts()
        assert accounts == [
            {
                "type": "accounts",
                "id": "1111111111",
                "attributes": {
                    "cloud-type": "azure",
                },
            },
            {
                "type": "accounts",
                "id": "2222222222",
                "attributes": {
                    "awsaccount-id": "123456789012",
                    "cloud-type": "aws",
                },
            },
        ]

    def test_get_aws_accounts(self, cc_all_accounts):
        aws_accounts = cloudconformity.get_aws_accounts(
            accounts=cc_all_accounts["data"]
        )
        print(aws_accounts)
        assert aws_accounts == {
            "123456789012": {
                "awsaccount-id": "123456789012",
                "cc-id": "2222222222",
                "cloud-type": "aws",
            }
        }

    @patch("lib.cloud_conformity.CloudConformity.get_aws_accounts")
    def test_aws_account_cc_id(self, mock_get_aws_accounts):
        mock_get_aws_accounts.return_value = {
            "123456789012": {
                "awsaccount-id": "123456789012",
                "cc-id": "2222222222",
                "cloud-type": "aws",
            }
        }
        cc_id = cloudconformity.get_aws_account_cc_id("123456789012")
        assert cc_id == "2222222222"
