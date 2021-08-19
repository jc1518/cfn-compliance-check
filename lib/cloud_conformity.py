"""
Cloud Conformity
"""

import json
import os
from functools import lru_cache
from logging import DEBUG, ERROR, exception

import requests

from lib.log_utils import log

CLOUD_CONFORMITY_BASE_URL = "https://ap-southeast-2-api.cloudconformity.com/v1"


class CloudConformityApiKeyMissing(Exception):
    pass


if not os.environ.get("CLOUD_CONFORMITY_API_KEY"):
    raise CloudConformityApiKeyMissing(
        "CLOUD_CONFORMITY_API_KEY environment variable is missing!"
    )

CLOUD_CONFORMITY_API_KEY = os.environ["CLOUD_CONFORMITY_API_KEY"]


class CloudConformity:
    def __init__(self) -> None:
        self.base_url = CLOUD_CONFORMITY_BASE_URL
        self.api_key = CLOUD_CONFORMITY_API_KEY
        self.headers = {
            "Content-Type": "application/vnd.api+json",
            "Authorization": "ApiKey " + self.api_key,
        }

    def _get_request(self, path: str) -> str:
        try:
            response = requests.get(
                f"{self.base_url}/{path}", headers=self.headers, timeout=10
            )
            return response.text
        except Exception as err:
            log(err, level=ERROR)

    def get_all_accounts(self) -> list:
        response = json.loads(self._get_request("accounts"))
        accounts = response["data"]
        return accounts

    def get_aws_accounts(self, accounts=None) -> dict:
        aws_accounts = {}
        if accounts is None:
            accounts = self.get_all_accounts()
        for _, account in enumerate(accounts):
            if "awsaccount-id" in account["attributes"].keys():
                account["attributes"]["cc-id"] = account["id"]
                aws_accounts[account["attributes"]["awsaccount-id"]] = account[
                    "attributes"
                ]
        return aws_accounts

    def get_aws_account_cc_id(self, aws_account_id: str) -> str:
        aws_accounts = self.get_aws_accounts()
        cc_id = aws_accounts[aws_account_id]["cc-id"]
        log(f"cc_id for {aws_account_id} is {cc_id}", level=DEBUG)
        return cc_id

    def get_resource_failed_checks(self, cc_id: str, resource_id: str) -> dict:
        path = f"checks?accountIds={cc_id}&filter[resource]={resource_id}&filter[statuses]=FAILURE"
        log(f"path is {path}", level=DEBUG)
        response = json.loads(self._get_request(path))
        return response

    def get_service_checks(self, cc_id: str, service_name: str) -> dict:
        path = f"checks?accountIds={cc_id}&page[size]=1000&page[number]=0&filter[services]={service_name}"
        log(f"path is {path}", level=DEBUG)
        response = json.loads(self._get_request(path))
        return response
