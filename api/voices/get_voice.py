from ..client import get_client


def get_voice(api_key: str, voice_id: str):
    client = get_client()
    voice = client.voices.get(voice_id)
    return voice
