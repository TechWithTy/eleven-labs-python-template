from ....client import get_client

def update_chapter(project_id: str, chapter_id: str):
    client = get_client()
    
    response = client.post(
        f"/v1/studio/projects/{project_id}/chapters/{chapter_id}",
        json={}
    )
    
    return response.json()