from ...client import get_client

def add_pronunciation_dictionary_rules(pronunciation_dictionary_id: str, rules: list):
    client = get_client()

    response = client.post(
        f"/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/add-rules",
        json={"rules": rules}
    )

    return response.json()

# Usage example:
# pronunciation_dictionary_id = "21m00Tcm4TlvDq8ikWAM"
# rules = [
#     {
#         "type": "alias",
#         "alias": "tie-land",
#         "string_to_replace": "Thailand"
#     }
# ]
# result = add_pronunciation_dictionary_rules(pronunciation_dictionary_id, rules)
# print(result)
