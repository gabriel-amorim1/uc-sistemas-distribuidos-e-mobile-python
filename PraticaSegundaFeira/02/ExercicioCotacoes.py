import requests
import sqlite3
import datetime

url = 'https://api.hgbrasil.com/finance/'
format = 'json-cors'
key = '64f90d7b'
currency = 'BRL'

r = requests.get(url, params={'format': format,
                 'key': key, 'currency': currency})

connection = sqlite3.connect("dbcotacoes.db")
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS moedas (Data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, Dolar FLOAT, Euro FLOAT)")

if (r.status_code == 200):
    currency_USD = r.json()['results']['currencies']['USD']["buy"]
    currency_EUR = r.json()['results']['currencies']['EUR']["buy"]

    cursor.execute("insert into moedas values (?, ?, ?)",
                   (datetime.datetime.now(), currency_USD, currency_EUR))
    connection.commit()

else:
    print('Nao houve sucesso na requisicao.')
