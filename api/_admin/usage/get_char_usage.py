from ...client import get_client

def get_character_usage(start_unix: int, end_unix: int):
    client = get_client()
    
    response = client.get(
        "/v1/usage/character-stats",
        params={
            "start_unix": start_unix,
            "end_unix": end_unix
        }
    )
    
    return response.json()