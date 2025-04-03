from elevenlabs import client

# Initialize the client with your API key
client.api_key = "<apiKey>"

# Make the API request
response = client.studio.project.chapter.list_snapshots(
    project_id="21m00Tcm4TlvDq8ikWAM",
    chapter_id="21m00Tcm4TlvDq8ikWAM"
)

# Process the response
snapshots = response.json()