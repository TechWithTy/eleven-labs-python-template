from ....client import get_client

def get_chapter_snapshot(project_id: str, chapter_id: str, chapter_snapshot_id: str):
    client = get_client()
    
    response = client.get(
        f"/v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots/{chapter_snapshot_id}"
    )
    
    return response.json()