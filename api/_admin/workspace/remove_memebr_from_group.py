from ...client import get_client

async def remove_member_from_group(group_id: str, email: str):
    client = get_client()
    endpoint = f"/v1/workspace/groups/{group_id}/members/remove"
    payload = {"email": email}
    
    response = await client.post(endpoint, json=payload)
    return response.json()