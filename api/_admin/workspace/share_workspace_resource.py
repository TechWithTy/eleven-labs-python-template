from ...client import get_client

def share_workspace_resource(resource_id: str, role: str, resource_type: str):
    client = get_client()
    
    response = client.post(
        f"/v1/workspace/resources/{resource_id}/share",
        json={
            "role": role,
            "resource_type": resource_type
        }
    )
    
    return response.json()