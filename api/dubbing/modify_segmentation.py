from ..client import get_client


def modify_segment(api_key: str, dubbing_id: str, segment_id: str, language: str):
    client = get_client()

    response = client.patch(
        f"/v1/dubbing/resource/{dubbing_id}/segment/{segment_id}/{language}", json={}
    )

    return response.json()


# Usage example:
# api_key = "your_api_key_here"
# dubbing_id = "your_dubbing_id"
# segment_id = "your_segment_id"
# language = "en"
# result = modify_segment(api_key, dubbing_id, segment_id, language)
# print(result)
