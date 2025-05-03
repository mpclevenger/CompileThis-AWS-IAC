import os
import json
import boto3

from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb',region_name="us-east-1")
TABLE_NAME = os.environ["TABLE_NAME"] 

def lambda_handler(event, context):
  if event["httpMethod"] == "OPTIONS":
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS, PUT",
            "Access-Control-Allow-Headers": "*"
        }
    }

  
  try:
    response = dynamodb.update_item(
      TableName = TABLE_NAME,
      Key={
            "ID": {"S": "visitors"}
      },
      UpdateExpression="ADD visitors :inc",
      ExpressionAttributeValues={
            ":inc":{"N": "1"}
      }
    )

  except ClientError as e:
    print(f"Error updating item: {e}")
    return {
       "statusCode" : 500,
       "headers": {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "*",
          "Access-Control-Allow-Headers": "*"
       },
       "body": json.dumps({"error": "Could not update counter."})
    }
  
  return {
    "statusCode": 200,
    "headers": {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "*",
      "Access-Control-Allow-Headers": "*"
    },
    "body": json.dumps({"message": "Counter updated."})
  }
