import requests

url = 'https://viacep.com.br/ws/'
uf = 'MG/'
cidade = 'Belo Horizonte/'
rua = 'Rua dos Aimores'
formato = '/json/'

r = requests.get(url + uf + cidade + rua + formato)
print(url + uf + cidade + rua + formato)
if (r.status_code == 200):
    print()
    print('JSON : ', r.json())
    print()
else:
    print('Nao houve sucesso na requisicao.')
