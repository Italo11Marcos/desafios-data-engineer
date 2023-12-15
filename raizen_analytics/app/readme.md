# Raizen Analytics

[Repositório Original](https://github.com/raizen-analytics/data-engineering-test/tree/master)


### Como executar?

    1 - Clone o projeto
    2 - Crie seu ambiente virtual: python -m venv env
    3 - Instale os requirements: python -m pip install -r requirements.txt
    4 - Crie sua conexão com o banco de dados de sua preferência (Utilizei o postgresql)
    5 - Configure a conexão com o banco de dados no arquivo: utils.py
    6 - Execute o arquivo: main.py

### Observações

    - A extensão do arquivo original foi modificada de '.xls' para '.xlsx' para facilitar a leitura
    - O arquivo 'anp_sales.sql' contem o script para criar a tabela com repartição no Postgresql
    - O objetivo era utilizar o airflow para orquestrar as funções, mas por problemas técnicos, não foi possível
