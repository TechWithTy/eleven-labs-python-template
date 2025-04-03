from ...client import get_client

def unshare_workspace_resource(resource_id: str, resource_type: str):
    client = get_client()
    
    response = client.post(
        f"/v1/workspace/resources/{resource_id}/unshare",
        json={"resource_type": resource_type}
    )
    
    return response.json()