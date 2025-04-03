from ...client import get_client

def create_podcast(model_id: str, host_voice_id: str, guest_voice_id: str, text: str):
    client = get_client()

    response = client.post(
        "/v1/studio/podcasts",
        json={
            "model_id": model_id,
            "mode": {
                "type": "conversation",
                "conversation": {
                    "host_voice_id": host_voice_id,
                    "guest_voice_id": guest_voice_id
                }
            },
            "source": {
                "text": text
            }
        }
    )

    return response.json()