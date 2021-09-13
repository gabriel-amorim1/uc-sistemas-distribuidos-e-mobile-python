import requests

r = requests.get('http://www.google.com/search',
                 params={'q': 'gabriel de amorim'})

if (r.status_code == 200):
    arquivo = open("resultados.txt", "a")
    arquivo.write(r.text)
else:
    print('Nao houve sucesso na requisicao.')
