from ...client import get_client

def delete_studio_project(project_id: str):
    client = get_client()
    response = client.delete(f"/v1/studio/projects/{project_id}")
    return response.json()