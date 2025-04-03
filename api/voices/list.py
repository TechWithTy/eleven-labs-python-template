from ..client import get_client


def list_voices(api_key: str):
    client = get_client()
    voices = client.voices.get_all(include_total_count=True)
    return voices
