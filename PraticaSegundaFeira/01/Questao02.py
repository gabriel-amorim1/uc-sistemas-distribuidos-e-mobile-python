import requests

url = 'https://viacep.com.br/ws/'
cep = 30140071
formato = '/json/'

for i in range(5):
    r = requests.get(url + str(cep) + formato)

    if (r.status_code == 200):
        print()
        print('JSON : ', r.json())
        print()
    else:
        print('Nao houve sucesso na requisicao.')

    cep += 1
