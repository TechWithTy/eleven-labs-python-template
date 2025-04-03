from ...client import get_client

def update_member(email: str):
    client = get_client()
    
    response = client.post(
        "/v1/workspace/members",
        json={"email": email}
    )
    
    return response.json()