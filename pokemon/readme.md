##  PokéSelect

### Sumário

1. [Objetivos](#objetivos)
2. [Resumo](#resumo)
3. [Execução](#execução)
4. [Demonstração](#demonstração)


### Objetivos

O projeto PokéSelect é uma aplicação web que utiliza o ``MongoDB`` como banco de dados e ``Flask`` como backend para permitir aos usuários selecionar e explorar Pokémon com base em seus tipos. A aplicação foi desenvolvida para oferecer uma experiência intuitiva e amigável aos fãs da franquia Pokémon que desejam descobrir e aprender mais sobre os diferentes tipos de Pokémon disponíveis.

### Resumo

A base de dados foi feita a partir do web scrapy da página [pokemondb](https://pokemondb.net/pokedex/all), obtendo os seguintes dados:

| Coluna  | Descrição                              |
|---------|----------------------------------------|
| POKEID  | Número na national pokedex             |
| NAME    | Nome do pokemon                        |
| TYPE    | Tipo do pokemon                        |
| TOTAL   | Soma de todos os atributos do pokemon  |
| HP      | Quantidade de Health Points do pokemon |
| ATTACK  | Valor de ataque do pokemon             |
| DEFENSE | Valor de defesa do pokemon             |
| SP_ATK  | Valor de ataque especial do pokemon    |
| SP_DEF  | Valor de defesa especial do pokemon    |
| SPEED   | Valor da velocidade do pokemon         |
| ICONS   | Url com a imagem do pokemon            |

Após a raspagem dos dados, foi feito um tratamento e exportado em formato [json](/pokemon/pokemon.json).

Tecnologias utilizadas:
* Backend: Flask (Python)
* Banco de Dados: MongoDB

### Execução
* Crie seu ambiente de desenvolvimento e instale as dependências: ``pip install -r requirements.txt``
* Configure os dados de conexão com mongodb no arquivo ``.env``
* Para gerar os dados .json, execute o arquivo: [main.py](/pokemon/scrapy/main.py) e depois o [modify_json.py](/pokemon/scrapy/modify_json.py)
* Você pode encontrar o arquivo já pronto para importar [aqui](/pokemon/pokemon.json).

### Demonstração

![](/pokemon/docs/pokemons-screen.gif)

