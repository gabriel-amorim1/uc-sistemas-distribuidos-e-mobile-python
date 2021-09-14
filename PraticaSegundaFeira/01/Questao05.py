import requests

r = requests.get('http://www.google.com/search',
                 params={'q': 'gabriel de amorim'})

if (r.status_code == 200):
    arquivo = open("resultados.txt", "w")
    arquivo.write(r.text)
    arquivo.close
else:
    print('Nao houve sucesso na requisicao.')
