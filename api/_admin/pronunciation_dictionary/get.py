from ...client import get_client

def get_pronunciation_dictionary(pronunciation_dictionary_id: str):
    client = get_client()

    response = client.get(
        f"/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}"
    )

    return response.json()

# Usage example:
# pronunciation_dictionary_id = "21m00Tcm4TlvDq8ikWAM"
# result = get_pronunciation_dictionary(pronunciation_dictionary_id)
# print(result)