from ...client import get_client

def get_pronunciation_dictionary_by_version(dictionary_id: str, version_id: str):
    client = get_client()
    
    response = client.get(
        f"/v1/pronunciation-dictionaries/{dictionary_id}/{version_id}/download"
    )
    
    return response.content