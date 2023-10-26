import requests
import base64

class ManipulaRepositorios:

    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = '__Token__Aqui__'
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                        "X-GitHub-Api-Version": "2022-11-28"
                        }
        
    def cria_repo(self, nome_repo):
        data = {
            "name": nome_repo,
            "description": 'Upload no repositório feito via API e linguagem python',
            'private': False
        }
        response = requests.post(f"{self.api_base_url}/user/repos", json=data, headers=self.headers)
        print(f'Status_code criação do repositorio: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        with open(caminho_arquivo, 'rb') as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)


        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            "message": "Dados dos repositorio de algumas empresas",
            "content": encoded_content.decode("utf-8")   
        }
        response = requests.put(url, json=data, headers=self.headers)
        print(f"status_code upload do arquivo: {response.status_code}")
        print(response.json())

novo_repo = ManipulaRepositorios("Dstinoco")
nome_repo = "linguagens-repositorios-empresas"
novo_repo.cria_repo(nome_repo)


novo_repo.add_arquivo(nome_repo,"linguagem_amzn.csv", "dados/amzn.csv")
novo_repo.add_arquivo(nome_repo,"linguagem_netflix.csv", "dados/netflix.csv")
novo_repo.add_arquivo(nome_repo,"linguagem_spotify.csv", "dados/spotify.csv")
print("Sucesso!!")






