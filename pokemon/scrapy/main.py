import requests
import pandas as pd
from bs4 import BeautifulSoup

"""
Pega os dados dos pokemons e exporta para .csv e .json
"""

# URL da pokedex
url = "https://pokemondb.net/pokedex/all"

# Parse da url e procura pela tabela com id pokedex
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')
table = soup.find('table', id="pokedex")

# Listas para apendar os dados
header = []
rows = []
icons = []

# Pecorre cada linha da tabela
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])
        icons.append([el['src'] for el in row.find_all('img')])

# Monta o dataframe
df = pd.DataFrame(data=rows, columns=header)
df['icons'] = icons

# Transforma a coluna 'Type' em uma lista
df['Type'] = df['Type'].str.split(' ')

# Renomeia as colunas
df.columns = ['POKEID', 'NAME', 'TYPE', 'TOTAL', 'HP', 'ATTACK', 'DEFENSE', 'SP_ATK', 'SP_DEF', 'SPEED', 'ICONS']

# Exporta para csv e json
df.to_csv('pokedex.csv', sep=';', index=False)
df.to_json('pokedex.json', orient="records")