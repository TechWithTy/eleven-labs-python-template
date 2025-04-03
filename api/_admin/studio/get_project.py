from ...client import get_client

def get_studio_project(project_id: str):
    client = get_client()
    
    response = client.get(f"/v1/studio/projects/{project_id}")
    
    return response.json()
