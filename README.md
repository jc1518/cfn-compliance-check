# CloudFormation Compliance Check

A tool that checks if the CloudFormation stack has any failed checks in Cloud Conformity.

## Install

```
pip install --user git+https://github.com/jc1518/cfn-compliance-check.git
```

## Setup

- Assume the AWS role that has the `cloudformation:ListStackResources` permission.
- Setup CloudConformity API key as an environment variable: `export CLOUD_CONFORMITY_API_KEY=HqJMC......`.

## Usage

```
usage: cfn-compliance-check [-h] stack_arn

CloudFormation Compliance Check

positional arguments:
  stack_arn   CloudFormation Stack ID (arn)

optional arguments:
  -h, --help  show this help message and exit
```

Example:

```
cfn-compliance-check arn:aws:cloudformation:ap-southeast-2:123456789012:stack/test-appLog/9cc21eb0-d27b-11eb-9559-06a07c2b4aa8

2021-08-16 21:39:20,524 WARNING: Failed checks:
 ❌ Low: (S3 Bucket) Bucket test-logging doesn't have access logging enabled
 ❌ Medium: (S3 Bucket) Bucket test-logging does not enforce SSL to secure data in transit
 ❌ Medium: (S3 Bucket) Bucket test-logging-delivery-failures does not enforce SSL to secure data in transit
```

## Test

```
python -m pytest -v
```
