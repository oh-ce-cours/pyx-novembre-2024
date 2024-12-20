import requests

response = requests.post(
    "http://127.0.0.1:5000/action", json={"message": "Hello, world!"}
)
response.raise_for_status()
print(response.json())
