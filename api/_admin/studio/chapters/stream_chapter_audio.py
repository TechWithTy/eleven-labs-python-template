from ....client import get_client

def stream_chapter_audio(project_id: str, chapter_id: str, chapter_snapshot_id: str):
    client = get_client()
    
    response = client.post(
        f"/v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots/{chapter_snapshot_id}/stream",
        json={}
    )
    
    return response.content