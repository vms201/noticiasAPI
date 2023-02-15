#biblioteca: pip, requests
import requests

try:
    requisicao = requests.get("https://newsapi.org/v2/top-headlines?country=br&apiKey=0acf488927204207a9d6a0436d9bd704")
    requisicao.raise_for_status()
    # JSON
    dados = requisicao.json()
    for i in range(len(dados['articles'])):
            autor = dados['articles'][i]['author'] if dados['articles'][i]['author'] else "Sem informação"
            titulo = dados['articles'][i]['title'] if dados['articles'][i]['title'] else "Sem informação"
            descricao = dados['articles'][i]['description'] if dados['articles'][i]['description'] else "Sem informação"
            print("Autor: " + autor + "\nTítulo: " + titulo + "\nDescrição: " + descricao + "\n")

except requests.HTTPError as http_erro:
    print(f'Erro HTTP: {http_erro}')
except Exception as erro:
    print(f'Ocorreu um erro inesperado: {erro}')