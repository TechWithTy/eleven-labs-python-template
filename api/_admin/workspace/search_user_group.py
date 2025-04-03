from ...client import get_client

client = get_client()

response = client.workspace.search_user_group(
    name="name"
)

# Process the response as needed
