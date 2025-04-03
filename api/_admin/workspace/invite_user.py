from ...client import get_client

def invite_user(email: str):
    client = get_client()
    
    response = client.post(
        "/v1/workspace/invites/add",
        json={"email": email}
    )
    
    return response.json()

# Usage example:
# result = invite_user("john.doe@testmail.com")
# print(result)