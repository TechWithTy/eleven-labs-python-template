from ...client import get_client
from typing import Dict

def convert_project(project_id: str) -> Dict:
    client = get_client()
    
    response = client.post(
        f"/v1/studio/projects/{project_id}/convert"
    )
    
    return response.json()