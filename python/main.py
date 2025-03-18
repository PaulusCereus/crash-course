"""Программа для обращения к API Github"""

import requests

response = requests.get("https://api.github.com")
print(response.json())
