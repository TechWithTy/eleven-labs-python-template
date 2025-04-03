from ...client import get_client

def add_pronunciation_dictionary(name: str, rules: list):
    client = get_client()

    response = client.post(
        "/v1/pronunciation-dictionaries/add-from-rules",
        json={
            "name": name,
            "rules": rules
        }
    )

    return response.json()

# Usage example:
# rules = [
#     {
#         "type": "alias",
#         "alias": "tie-land",
#         "string_to_replace": "Thailand"
#     }
# ]
# result = add_pronunciation_dictionary("My Dictionary", rules)
# print(result)