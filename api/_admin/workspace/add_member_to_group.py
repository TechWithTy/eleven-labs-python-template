from typing import Dict, Any
import httpx
import logging
from ...client import client

API_BASE_URL = "https://api.elevenlabs.io"
API_VERSION = "v1"

def add_member_to_group(group_id: str, email: str) -> Dict[str, Any]:
    """
    Add a member to a user group.

    Args:
        group_id (str): The ID of the group to add the member to.
        email (str): The email of the member to add.

    Returns:
        Dict[str, Any]: The response from the API.
    """
    endpoint = f"{API_BASE_URL}/{API_VERSION}/workspace/groups/{group_id}/members"
    
    payload = {
        "email": email
    }

    try:
        response = client.post(endpoint, json=payload)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise