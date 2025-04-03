from ...client import get_client

def list_studio_project_snapshots(project_id: str):
    client = get_client()
    
    response = client.get(
        f"/v1/studio/projects/{project_id}/snapshots"
    )
    
    return response.json()