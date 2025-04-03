from ...client import get_client

def create_pronunciation_dictionaries(project_id: str, pronunciation_dictionary_locators: list):
    client = get_client()

    response = client.post(
        f"/v1/studio/projects/{project_id}/pronunciation-dictionaries",
        json={
            "pronunciation_dictionary_locators": pronunciation_dictionary_locators
        }
    )

    return response.json()

# Usage example:
# project_id = "21m00Tcm4TlvDq8ikWAM"
# pronunciation_dictionary_locators = [
#     {
#         "pronunciation_dictionary_id": "pronunciation_dictionary_id"
#     }
# ]
# result = create_pronunciation_dictionaries(project_id, pronunciation_dictionary_locators)
# print(result)