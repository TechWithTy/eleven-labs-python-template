from ....client import get_client
from typing import Dict

def list_chapters(project_id: str) -> Dict:
    client = get_client()
    
    response = client.get(
        f"/v1/studio/projects/{project_id}/chapters"
    )
    
    return response.json()