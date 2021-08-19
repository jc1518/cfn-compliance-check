"""
CloudFormation Compliance Check
"""
import argparse
import logging
import re

from lib.aws_cloudformation import CloudFormation
from lib.cloud_conformity import CloudConformity
from lib.log_utils import log

cloudconformity = CloudConformity()
cloudformation = CloudFormation()


class NoResourceFound(Exception):
    pass


class NotValidArn(Exception):
    pass


def is_valid_arn(stack_arn: str) -> bool:
    """Validate arn"""
    arn_pattern = "^arn:aws:cloudformation:(?P<Region>[^:\n]*):\d{12}:stack/?/.*$"
    if re.compile(arn_pattern).match(stack_arn):
        return True
    return False


def cfn_compliance_check(stack_arn: str) -> list:
    account = stack_arn.split(":")[4]
    cc_id = cloudconformity.get_aws_account_cc_id(account)
    checks_summary = []
    resources_ids = cloudformation.get_stack_resources(stack_arn)

    if not resources_ids:
        raise NoResourceFound(f"Faild to find the CloudFormation stack {stack_arn}")

    for _, resource_id in enumerate(resources_ids):
        resource_checks = cloudconformity.get_resource_failed_checks(
            cc_id,
            resource_id,
        )
        if resource_checks["data"]:
            for _, check in enumerate(resource_checks["data"]):
                checks_summary.append(
                    f'{check["attributes"]["pretty-risk-level"]}: ({check["attributes"]["resourceName"]}) {check["attributes"]["message"]}'
                )
    if checks_summary:
        checks_summary.sort()
        log(
            "Failed checks: \n \u274c " + "\n \u274c ".join(map(str, checks_summary)),
            level=logging.WARN,
        )
    else:
        zero_findings_message = (
            "\u2705 Congratulations! There are no any failed compliance checks so far. "
            "But please be aware of that the compliance check is not real time, "
            "so there is a possibility that your stack has not been scanned yet."
        )
        log(f"{zero_findings_message}")
    return checks_summary


def parse_args():
    parser = argparse.ArgumentParser(description="CloudFormation Compliance Check")
    parser.add_argument("stack_arn", help="CloudFormation Stack ID (arn)", type=str)
    return parser.parse_args()


def main():
    args = parse_args()
    arn = args.stack_arn
    if not is_valid_arn(arn):
        raise NotValidArn(f"{arn} is not a valid CloudFormation arn.")
    cfn_compliance_check(args.stack_arn)


if __name__ == "__main__":
    main()
