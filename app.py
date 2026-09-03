#!/usr/bin/env python3

from aws_cdk import App, Environment

from bryanturns_cdk.frontend_stack import FrontendStack

app = App()

# Intentionally errors if doesn't exist
account = app.node.get_context("account")
region = app.node.get_context("region")
# TODO: These parameters should be tied to the account and region.
# Although I'll only ever be the one deploying this and I don't plan on a dev/prod
# setup for now
cert_arn = app.node.get_context("certificate_arn")
hosted_zone_id = app.node.get_context("hosted_zone_id")
hosted_zone_name = app.node.get_context("hosted_zone_name")
projects = app.node.get_context("projects")

env = Environment(account=account, region=region)

# Assume that a wildcard certificate was issued and all provided domains
# are either the root domain or only one subdomain deep
# this would be easy to validate later.
for project in projects:
    domain_name = project["domain_name"]
    project_name = project["project_name"]
    FrontendStack(
        app, project_name, cert_arn, hosted_zone_id, hosted_zone_name, domain_name, env
    )


app.synth()
