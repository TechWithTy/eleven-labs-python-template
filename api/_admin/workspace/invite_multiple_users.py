from ...client import get_client

def invite_multiple_users(emails):
    client = get_client()
    
    response = client.post(
        "/v1/workspace/invites/add-bulk",
        json={"emails": emails}
    )
    
    return response.json()

# Usage example:
# emails = ["user1@example.com", "user2@example.com"]
# result = invite_multiple_users(emails)
# print(result)