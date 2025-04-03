from backend.apps.eleven_labs.client import client

# Initialize the client
client.init_api_key("<apiKey>")

# Make the API call
response = client.studio.get_chapter(
    project_id="21m00Tcm4TlvDq8ikWAM",
    chapter_id="21m00Tcm4TlvDq8ikWAM"
)