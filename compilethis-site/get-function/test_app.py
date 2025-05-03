from app import lambda_handler

def test_lambda_returns_200():
    event = {
        "httpMethod": "GET"
    }
    context = {}
    response = lambda_handler(event, context)

    assert response["statusCode"] == 200
    assert "headers" in response
    assert "body" in response
