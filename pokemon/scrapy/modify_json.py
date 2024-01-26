import json

"""
Script que modifica a estrutura do json
"""

f = open('../pokedex.json')
pokemons = json.load(f)

for data in pokemons:

    # Cria uma nova estrutura
    data['STATUS'] = {
        "TOTAL": int(data["TOTAL"]),
        "HP": int(data["HP"]),
        "ATTACK": int(data["ATTACK"]),
        "DEFENSE": int(data["DEFENSE"]),
        "SP_ATK": int(data["SP_ATK"]),
        "SP_DEF": int(data["SP_DEF"]),
        "SPEED": int(data["SPEED"])
    }

    # Deleta os atributos que não serão utilizados
    data.pop("TOTAL")
    data.pop("HP")
    data.pop("ATTACK")
    data.pop("DEFENSE")
    data.pop("SP_ATK")
    data.pop("SP_DEF")
    data.pop("SPEED")

# Grava o arquivo novo
with open("../pokemon.json", "w") as file:
    json.dump(pokemons, file, indent=4)
