from ...client import get_client

def add_shared_voice(public_user_id: str, voice_id: str, new_name: str):
    client = get_client()
    
    response = client.post(
        f"/v1/voices/add/{public_user_id}/{voice_id}",
        json={"new_name": new_name}
    )
    
    return response.json()

# Usage example:
# public_user_id = "63e06b7e7cafdc46be4d2e0b3f045940231ae058d508589653d74d1265a574ca"
# voice_id = "21m00Tcm4TlvDq8ikWAM"
# new_name = "John Smith"
# result = add_shared_voice(public_user_id, voice_id, new_name)
# print(result)