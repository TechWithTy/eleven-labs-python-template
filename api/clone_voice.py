import os
from typing import BinaryIO
from ..client import get_client


# Import customer voice data function
from ..api.get_vocie_data import get_customer_voice_data

# Initialize ElevenLabs client
elevenlabs = Client(api_key=os.getenv("ELEVENLABS_API_KEY"))


def use_customer_voice(customer_id: str, text: str) -> BinaryIO:
    """
    Use a customer's voice for text generation.
    This example fetches voices and uses one to generate speech.

    Args:
        customer_id: The unique ID of the customer
        text: The text to generate speech from

    Returns:
        The audio stream of generated speech

    Raises:
        Exception: If speech generation fails
    """
    # Get customer-specific data to ensure isolation
    customer_data = get_customer_voice_data(customer_id)
    voice_name = customer_data.get("voiceName")

    try:
        # Fetch all available voices
        voices_response = elevenlabs.voices.get_all()

        # Access the array of voices in the response
        voices = voices_response.voices

        # Find a specific voice by name
        selected_voice = next(
            (voice for voice in voices if voice.name == voice_name), None
        )

        if not selected_voice:
            raise Exception(f"No voice found with the name {voice_name}")

        # Ensure that we are using the correct property for the voice ID
        voice_id = selected_voice.voice_id

        if not voice_id:
            raise Exception("No voice ID found for the selected voice")

        # Generate speech using the selected voice
        audio = elevenlabs.generate(
            text=text,
            voice=voice_id,
            model_id="eleven_multilingual_v2",  # Specify the model for generation
        )

        print(f"Speech generated successfully using voice: {selected_voice.name}")
        return audio
    except Exception as error:
        print(f"Error using voice for customer {customer_id}: {error}")
        raise Exception("Failed to generate speech using customer voice")
