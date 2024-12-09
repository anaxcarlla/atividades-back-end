import requests


url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("URL da imagem:", data["message"])  
else:
    print(f"Erro: {response.status_code}")
