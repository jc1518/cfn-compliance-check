#!/usr/bin/env python3

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="cfn-compliance-check",
    version="1.0",
    description="CloudFormation Stack Compliance Check",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jc1518/cfn-compliance-check.git",
    author="Jackie Chen",
    py_modules=[
        "cfn_compliance_check",
        "lib.log_utils",
        "lib.aws_cloudformation",
        "lib.cloud_conformity",
    ],
    python_requires=">=3.0",
    install_requires=["requests", "boto3"],
    entry_points={
        "console_scripts": [
            "cfn-compliance-check=cfn_compliance_check:main",
        ],
    },
)
