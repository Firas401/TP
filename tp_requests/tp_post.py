import requests

data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post"

response = requests.post(url, json=data)
print("Status code:", response.status_code)

response_data = response.json()
print("JSON response:", response_data)
