from ....client import get_client
from typing import Dict

def create_chapter(project_id: str, name: str) -> Dict:
    client = get_client()
    
    response = client.post(
        f"/v1/studio/projects/{project_id}/chapters",
        json={"name": name}
    )
    
    return response.json()