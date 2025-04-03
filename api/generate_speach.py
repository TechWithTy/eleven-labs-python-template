import os
import requests
from typing import BinaryIO

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
        response = requests.post(
            f"{ELEVENLABS_API_URL}/text-to-speech/{voice_id}",
            json={
                "text": text,
                "model_id": "eleven_multilingual_v2"  # Optional model, can be customized
            },
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            stream=True
        )
        
        if response.status_code == 200:
            return response.raw
        else:
            print(f"Error: {response.status_code}, {response.text}")
            raise Exception(f"Speech generation failed with status code {response.status_code}")
            
    except Exception as error:
        print(f"Error generating speech: {error}")
        raise Exception("Speech generation failed.")
