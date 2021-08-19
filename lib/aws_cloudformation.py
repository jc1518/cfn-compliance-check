"""
AWS Cloudformation
"""
import logging

import boto3

from lib.log_utils import log


class CloudFormation:
    def __init__(self) -> None:
        pass

    def get_stack_resources(self, stack_arn: str) -> list:
        try:
            region = stack_arn.split(":")[3]
            cloudformation_client = boto3.client("cloudformation", region_name=region)
            resources_ids = []
            response = cloudformation_client.list_stack_resources(StackName=stack_arn)

            while "nextToken" in response:
                for _, resource in enumerate(response["StackResourceSummaries"]):
                    resources_ids.append(resource["PhysicalResourceId"])
                response = cloudformation_client.list_stack_resources(
                    StackName=stack_arn,
                    nextToken=response["nextToken"],
                )

            for _, resource in enumerate(response["StackResourceSummaries"]):
                resources_ids.append(resource["PhysicalResourceId"])

            log(f"resouces_ids are {resources_ids}", level=logging.DEBUG)
            return resources_ids
        except Exception as err:
            log(f"{err}", level=logging.ERROR)
            return []
