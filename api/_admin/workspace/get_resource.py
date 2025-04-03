from ...client import get_client

def get_workspace_resource(resource_id: str):
    client = get_client()
    
    response = client.get(f"/v1/workspace/resources/{resource_id}")
    
    return response.json()

# Usage example:
# resource_id = "your_resource_id_here"
# result = get_workspace_resource(resource_id)
# print(result)