from ....client import get_client
from typing import Dict

def get_chapter(project_id: str, chapter_id: str) -> Dict:
    client = get_client()
    
    response = client.get(
        f"/v1/studio/projects/{project_id}/chapters/{chapter_id}"
    )
    
    return response.json()
