import requests

response = requests.post(
    "http://localhost:5000/action", json={"message": "Hello, world!"}
)
# response.raise_for_status()
print(response.json())
