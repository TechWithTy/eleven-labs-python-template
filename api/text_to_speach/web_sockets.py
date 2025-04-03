from ..client import get_client
from elevenlabs import Voices


def text_to_speech_stream(api_key, voice_id, text, model_id="eleven_monolingual_v1"):
    client = get_client()

    audio_stream = client.generate(
        text=text, voice=Voices().get(voice_id), model=model_id, stream=True
    )

    audio_stream = client.generate(
        text=text, voice=Voices().get(voice_id), model=model_id, stream=True
    )

    client.stream(audio_stream)

    client.stream(audio_stream)
