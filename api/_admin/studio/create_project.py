from ...client import get_client

def create_studio_project(name, default_title_voice_id, default_paragraph_voice_id, default_model_id):
    client = get_client()
    
    response = client.post(
        "/v1/studio/projects",
        files={
            "name": (None, name),
            "default_title_voice_id": (None, default_title_voice_id),
            "default_paragraph_voice_id": (None, default_paragraph_voice_id),
            "default_model_id": (None, default_model_id)
        }
    )
    
    return response.json()