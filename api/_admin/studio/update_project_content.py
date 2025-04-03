from ...client import get_client

def update_project_content(project_id: str, content_file):
    client = get_client()
    
    response = client.post(
        f"/v1/studio/projects/{project_id}/content",
        files={"content": content_file},
        headers={"Content-Type": "multipart/form-data"}
    )
    
    return response.json()