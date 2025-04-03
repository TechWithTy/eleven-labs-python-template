from ..client import get_client


def create_voice_clone(api_key, name, files):
    client = get_client()

    response = client.voices.add(name=name, files=files)

    return response
