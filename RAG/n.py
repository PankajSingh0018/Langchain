import requests

base_url = "http://localhost:11434"

# List of potential endpoints to check
endpoints = [
    "/api/embeddingsa",
    "/v1/embeddings",
    "/embeddings",
    "/api/embeddings",
    "/llm/embeddings",
    "/llms/embeddings",
    "/api/llm/embeddings",
    "/api/llms/embeddings",
    "/api/v1/models",
    "/v1/models",
    "/models",
    "/api/models"
]

for endpoint in endpoints:
    url = base_url + endpoint
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Endpoint '{url}' is available.")
            print(response.json())  # Assuming the response is JSON
        elif response.status_code == 404:
            print(f"Endpoint '{url}' returned 404 Not Found.")
        else:
            print(f"Endpoint '{url}' returned status code {response.status_code}.")
    except requests.ConnectionError as e:
        print(f"Failed to connect to endpoint '{url}':", e)
