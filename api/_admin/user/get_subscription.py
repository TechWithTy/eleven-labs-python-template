from ...client import get_client

def get_user_subscription():
    client = get_client()
    
    response = client.get("/v1/user/subscription")
    
    return response.json()