from ...client import get_client

def get_user():
    client = get_client()
    response = client.get("/v1/user")
    return response.json()
