from ...client import get_client

def delete_workspace_invite(email: str):
    client = get_client()
    
    response = client.delete(
        "/v1/workspace/invites",
        json={"email": email}
    )
    
    return response.json()

# Usage example:
# result = delete_workspace_invite("john.doe@testmail.com")
# print(result)