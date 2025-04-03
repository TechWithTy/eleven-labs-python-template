from ...client import get_client

def update_project(project_id: str, name: str, default_title_voice_id: str, default_paragraph_voice_id: str):
    client = get_client()
    
    response = client.post(
        f"/v1/studio/projects/{project_id}",
        json={
            "name": name,
            "default_title_voice_id": default_title_voice_id,
            "default_paragraph_voice_id": default_paragraph_voice_id
        }
    )
    
    return response.json()