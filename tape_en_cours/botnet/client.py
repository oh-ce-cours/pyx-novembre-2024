import requests

requests.post("http://localhost:5000/action", json={"message": "Hello, world!"})
