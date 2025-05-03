import os
import json
import boto3
import pytest
from moto import mock_dynamodb

from app import lambda_handler

TABLE_NAME = "cloud-resume-challenge"

@pytest.fixture(autouse=True)
def setup_env(monkeypatch):
    monkeypatch.setenv("TABLE_NAME", TABLE_NAME)

@mock_dynamodb
def test_put_counter():
    # Create mock table
    dynamodb = boto3.client("dynamodb", region_name="us-east-1")
    dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            { "AttributeName": "ID", "KeyType": "HASH" }
        ],
        AttributeDefinitions=[
            { "AttributeName": "ID", "AttributeType": "S" }
        ],
        BillingMode="PAY_PER_REQUEST"
    )

    # Seed item
    dynamodb.put_item(
        TableName=TABLE_NAME,
        Item={ "ID": { "S": "visitors" }, "visitors": { "N": "1" } }
    )

    # Fake PUT request
    event = { "httpMethod": "PUT" }
    context = {}

    response = lambda_handler(event, context)

    assert response["statusCode"] == 200
    assert "Access-Control-Allow-Origin" in response["headers"]
    assert json.loads(response["body"])["message"] == "Counter updated."
