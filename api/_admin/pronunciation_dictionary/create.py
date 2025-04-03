from ...client import get_client

def create_pronunciation_dictionary_from_file(name: str, file_path: str):
    client = get_client()

    with open(file_path, 'rb') as file:
        response = client.post(
            "/v1/pronunciation-dictionaries/add-from-file",
            files={
                "name": (None, name),
                "file": (file.name, file, "application/octet-stream")
            }
        )

    return response.json()