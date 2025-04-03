from ...client import get_client

def remove_pronunciation_dictionary_rules(pronunciation_dictionary_id: str, rule_strings: list):
    client = get_client()

    response = client.post(
        f"/v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/remove-rules",
        json={"rule_strings": rule_strings}
    )

    return response.json()

# Usage example:
# pronunciation_dictionary_id = "21m00Tcm4TlvDq8ikWAM"
# rule_strings = ["rule_strings"]
# result = remove_pronunciation_dictionary_rules(pronunciation_dictionary_id, rule_strings)
# print(result)