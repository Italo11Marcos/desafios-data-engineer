## Lego

O projeto de Extração, Transformação e Carregamento (ETL) com armazenamento em um bucket S3 da AWS foi desenvolvido utilizando a linguagem de programação Python, com uma abordagem orientada a objetos (POO). Este sistema eficiente e modularizado realiza o processo de ETL em uma base de dados, aplicando transformações necessárias e, em seguida, armazenando os resultados em um bucket S3 para fácil acesso e escalabilidade.

### Sumário

1. [Resumo](#resumo)
2. [Fluxo](#fluxo)
3. [Tecnologias Aplicadas](#tecnologias-utilizadas)
4. [Execução](#execução)

### Resumo

O arquivo LEGO Sets pode ser encontrado no [Maven Analytics](https://maven-datasets.s3.amazonaws.com/LEGO+Sets/LEGO+Sets.zip).
O objetivo é desenvolver um ETL utilizando ``POO`` no código ``python``, subindos os arquivos para ``AWS``.

### Fluxo

1. Extração de Dados:

    * O sistema é capaz de extrair dados de uma variedade de fontes, como bancos de dados SQL, NoSQL, APIs, ou arquivos locais.
    * Implementa classes dedicadas para diferentes fontes de dados, garantindo flexibilidade e fácil extensibilidade.

2. Transformação de Dados:

    * As transformações são aplicadas aos dados extraídos, utilizando classes de transformação dedicadas para modularizar e organizar o código.
    * A POO permite fácil manutenção e adição de novas transformações sem impactar o restante do código.

3. Carregamento no Bucket S3:

    * Os dados transformados são carregados de maneira eficiente em um bucket S3 da AWS.
    * A utilização da POO facilita a implementação de lógicas específicas para o armazenamento em nuvem, como controle de versão, criptografia, e gerenciamento de permissões.

4. Configuração Flexível:

    * O projeto possui um sistema de configuração flexível, permitindo que os usuários ajustem parâmetros como as fontes de dados, transformações específicas, e configurações do bucket S3.

5. Logs e Monitoramento:

    * Implementação de logs detalhados e monitoramento do processo ETL, facilitando a identificação de erros e otimização do desempenho.


### Tecnologias utilizadas

* Linguagem de Programação: Python
* POO (Programação Orientada a Objetos): Classes para Extração, Transformação e Carregamento, proporcionando modularidade e reutilização de código.
* Armazenamento em Nuvem: AWS S3 para o armazenamento dos dados transformados.


### Execução
* Crie seu ambiente virtual
* Instale as dependências ``python -m pip install requirements.txt``
* No arquivo ``.env``, coloque suas credenciais da AWS
* Execute o arquivo ``main.py``

