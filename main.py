import requests
import json

response = requests.get("https://api.github.com")

with open("response.json", "w") as f:
    f.write(json.dumps(response.json()))
