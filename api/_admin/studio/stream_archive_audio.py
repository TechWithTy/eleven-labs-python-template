from ...client import get_client

def stream_archive_audio(project_id: str, project_snapshot_id: str):
    client = get_client()
    
    response = client.post(
        f"/v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/archive"
    )
    
    return response.content