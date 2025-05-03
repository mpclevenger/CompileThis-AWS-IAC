import json

# import requests
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
  try:
    response = dynamodb.update_item(
          TableName = 'cloud-resume-challenge',
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

  
  """Sample pure Lambda function

  Parameters
  ----------
  event: dict, required
      API Gateway Lambda Proxy Input Format

      Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

  context: object, required
      Lambda Context runtime methods and attributes

      Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

  Returns
  ------
  API Gateway Lambda Proxy Output Format: dict

      Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
  """

  # try:
  #     ip = requests.get("http://checkip.amazonaws.com/")
  # except requests.RequestException as e:
  #     # Send some context about this error to Lambda Logs
  #     print(e)

  #     raise e

