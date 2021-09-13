import requests

url = 'https://viacep.com.br/abc/'
formato = 'json/'

r = requests.get(url + formato)

print('Código de retorno: ' + str(r.status_code))
print(r.text)
