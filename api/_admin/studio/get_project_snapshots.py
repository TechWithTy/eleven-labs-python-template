from ...client import get_client

def get_project_snapshot(project_id: str, project_snapshot_id: str):
    client = get_client()
    
    response = client.get(
        f"/v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}"
    )
    
    return response.json()