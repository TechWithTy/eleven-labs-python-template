from ...client import get_client

def list_pronunciation_dictionaries():
    client = get_client()
    response = client.get("/v1/pronunciation-dictionaries/")
    return response.json()