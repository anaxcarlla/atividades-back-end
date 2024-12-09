import requests

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    print("ID:", data["id"])
    print("Nome:", data["name"])
    print("Email:", data["email"])
else:
    print(f"Erro: {response.status_code}")
