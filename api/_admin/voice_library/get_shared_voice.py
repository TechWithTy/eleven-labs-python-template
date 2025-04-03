from ...client import get_client

def get_shared_voices(featured=True, reader_app_enabled=True):
    client = get_client()
    
    params = {
        "featured": featured,
        "reader_app_enabled": reader_app_enabled
    }
    
    response = client.get("/v1/shared-voices", params=params)
    
    return response.json()