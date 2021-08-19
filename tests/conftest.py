import pytest


@pytest.fixture(name="stack_resources")
def stack_resources():
    return {
        "StackResourceSummaries": [
            {
                "LogicalResourceId": "CfServiceCatalogTaggedOption",
                "PhysicalResourceId": "tag-vbw5n6txuycwq",
                "ResourceType": "AWS::ServiceCatalog::TagOption",
                "LastUpdatedTimestamp": "123456",
                "ResourceStatus": "CREATE_COMPLETE",
                "DriftInformation": {"StackResourceDriftStatus": "NOT_CHECKED"},
            },
            {
                "LogicalResourceId": "Portfolio",
                "PhysicalResourceId": "port-tm4lmmzdbvvjo",
                "ResourceType": "AWS::ServiceCatalog::Portfolio",
                "LastUpdatedTimestamp": "123456",
                "ResourceStatus": "CREATE_COMPLETE",
                "DriftInformation": {"StackResourceDriftStatus": "NOT_CHECKED"},
            },
            {
                "LogicalResourceId": "LogDeliveryBucket",
                "PhysicalResourceId": "test-app-logging",
                "ResourceType": "AWS::S3::Bucket",
                "LastUpdatedTimestamp": "123456",
                "ResourceStatus": "CREATE_COMPLETE",
                "DriftInformation": {"StackResourceDriftStatus": "NOT_CHECKED"},
            },
        ]
    }


@pytest.fixture(name="cc_all_accounts")
def cc_all_accounts():
    return {
        "data": [
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
    }


@pytest.fixture(name="resource_failed_checks")
def resource_failed_checks():
    return {
        "data": [
            {
                "type": "checks",
                "id": "ccc:ay5zGLTky:S3-017:S3:ap-southeast-2:test-app-logging",
                "attributes": {
                    "region": "ap-southeast-2",
                    "status": "FAILURE",
                    "risk-level": "MEDIUM",
                    "pretty-risk-level": "Medium",
                    "message": "Bucket test-app-logging does not enforce SSL to secure data in transit",
                    "resource": "test-app-logging",
                    "descriptorType": "s3-bucket",
                    "resourceName": "S3 Bucket",
                    "service": "S3",
                },
            }
        ]
    }
