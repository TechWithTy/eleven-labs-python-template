from ..client import get_client


def delete_segment(api_key: str, dubbing_id: str, segment_id: str):
    client = get_client()

    response = client.delete(f"/v1/dubbing/resource/{dubbing_id}/segment/{segment_id}")
    return response.json()
