import requests
import rich

data = {"command": "ls -alh"}
response = requests.post("http://127.0.0.1:8000/action", json=data, timeout=1)
response.raise_for_status()
rich.print(response.json())
