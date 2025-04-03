import os
from typing import BinaryIO
from ..client import get_client

# ElevenLabs API URL and API key
ELEVENLABS_API_URL = 'https://api.elevenlabs.io/v1'
API_KEY = os.getenv('ELEVENLABS_API_KEY')  # Get API key from environment variable

def generate_speech(voice_id: str, text: str) -> BinaryIO:
    """
    Generate speech using a cloned voice from ElevenLabs.

    Args:
        voice_id: The ID of the voice to use
        text: The text to convert to speech

    Returns:
        A binary stream of the audio data

    Raises:
        Exception: If the speech generation fails
    """
    try:
        client = get_client()
        audio_stream = client.generate(
            text=text,
            voice=voice_id,
            model_id="eleven_multilingual_v2"
        )
        return audio_stream
    except Exception as error:
        print(f"Error generating speech: {error}")
        raise Exception("Speech generation failed.")
