from ...client import get_client

def delete_voice_sample(voice_id: str, sample_id: str):
    client = get_client()
    response = client.delete(f"/v1/voices/{voice_id}/samples/{sample_id}")
    return response.json()

# Usage example:
# voice_id = "21m00Tcm4TlvDq8ikWAM"
# sample_id = "VW7YKqPnjY4h39yTbx2L"
# result = delete_voice_sample(voice_id, sample_id)
# print(result)