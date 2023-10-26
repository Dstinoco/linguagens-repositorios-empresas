import requests
import pandas as pd


class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = '__Token__Aqui__'
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                        "X-GitHub-Api-Version": "2022-11-28"
                        }

    def lista_repositorio(self):
        repos_list = []
        for page_num in range(1, 20):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)     
        return repos_list

    def nomes_repos(self, respos_list):
        repo_names = []
        for page in respos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])

                except:
                    pass
        return repo_names    

    def nomes_linguagens(self, repos_list):
        repo_linguagens = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_linguagens.append(repo['language'])
                except:
                    pass
        return repo_linguagens        

    def cria_df_linguagens(self):
        repositorios = self.lista_repositorio()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens

        return dados
    


dados = DadosRepositorios('amzn')
df = dados.cria_df_linguagens()
df.to_csv("dados/amzn.csv")

dados = DadosRepositorios('netflix')
df = dados.cria_df_linguagens()
df.to_csv("dados/netflix.csv")

dados = DadosRepositorios('spotify')
df = dados.cria_df_linguagens()
df.to_csv("dados/spotify.csv")


                    


