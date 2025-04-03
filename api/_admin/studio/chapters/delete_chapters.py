from ....client import get_client

def delete_chapter(project_id: str, chapter_id: str):
    client = get_client()
    response = client.delete(f"/v1/studio/projects/{project_id}/chapters/{chapter_id}")
    return response.json()