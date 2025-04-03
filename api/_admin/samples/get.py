from ...client import get_client

def get_sample_audio(voice_id: str, sample_id: str):
    client = get_client()
    
    response = client.get(f"/v1/voices/{voice_id}/samples/{sample_id}/audio")
    
    return response.content