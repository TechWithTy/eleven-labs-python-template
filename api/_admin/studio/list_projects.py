from ...client import get_client

def list_studio_projects():
    client = get_client()
    
    response = client.get("/v1/studio/projects")
    
    return response.json()