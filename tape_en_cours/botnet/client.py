import requests
import rich

data = {"commande": "ls -alh"}
response = requests.post("http://127.0.0.1:8000/action", json=data, timeout=1)
rich.print(response.json())
response.raise_for_status()
rich.print(response.json())
