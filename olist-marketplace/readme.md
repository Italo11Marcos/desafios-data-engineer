## Transformação e Análise de Dados de E-commerce Brasileiro utilizando os serviços da Microsoft Azure
Azure Data Factory, Azure Data Lake Storage, Azure Databricks e Arquitetura Medalhão


### Sumário

1. [Objetivo](#objetivo)
2. [Ferramentas Utilizadas](#ferramentas-utilizadas)
3. [Descrição do processo](#descrição-do-processo)
4. [Demonstração](#demonstração)
5. [Pontos de interesse](#pontos-de-interesse)



### Objetivo
O projeto visa criar uma pipeline de dados eficiente para extrair, transformar e carregar (ETL) dados do conjunto de dados público de e-commerce brasileiro do Kaggle, utilizando as ferramentas e serviços da Microsoft Azure (Azure Data Factory, Azure Data Lake Storage, Azure Databricks) e arquitetura medalhão. 

![Pipeline](/olist-marketplace/docs/projeto_azure_databricks.png)

![Print](/olist-marketplace/docs/pipeline_1.png)

## Ferramentas utilizadas

- **Azure Data Factory (ADF):** Serviço utilizado para orquestrar e automatizar o processo de ETL

- **Azure Data Lake Storage (ADLS):** Solução de armazenamento escalável e segura para armazenar dados em diferentes estágios do pipeline

- **Azure Databricks:** Plataforma de análise de dados e machine learning, usada para transformar e analisar os dados

- **Arquitetura Medalhão:** Estrutura para organizar os dados em camadas Bronze, Silver e Gold, melhorando a organização, acessibilidade e qualidade dos dados

## Dataset utlizado

Os dados utilizados nesse projeto foram extraídos do [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

Contém o seguinte schema:

![Schema](/olist-marketplace/docs/olist-schema.png)

Os arquivos ```.csv``` podem ser encontrados [aqui](/olist-marketplace/data/).

## Descrição do processo

1. **Extração dos dados (Transient)**

    - Para fins didáticos, os dados foram adicionados no [github](/olist-marketplace/data/csv/) no repositório
    - Azure Data Factory: ADF foi configurado para baixar os dados brutos do git e armazená-los no Azure Data Lake Storage na camada ```Transient```. Nessa camada, os dados foram salvos em formato ```.parquet```, sem qualquer transformação e são deletados após a finalização total do processo da camada ```Bronze```

2. **Transformação dos Dados (Bronze)**

    - Azure Databricks: Utilizando notebooks do Databricks, foi adicionada uma nova coluna com a data de execução do processo.
    - Nessa camada, os dados mantém o histórico e após a finalização do processo, os dados da camada transient são deletados

3. **Transformação dos Dados (Silver)**

    - Azure Databricks: Utilizando notebooks do Databricks, os dados foram limpos, tratados. As operações incluíram:

        - Remoção de duplicadas
        - Conversão dos tipos de dados
        - Adição de coluna com data de execução do processo

    - Armazenamento: Os dados foram modelados em ```One Big Table (OBT)``` e salvos na camada Silver em formato ```Delta``` 

4. **Análise e Agregação dos Dados (Gold):**

    - Em desenvolvimento

5. **Consumo dos Dados:**

    - Em desenvolvimento

### Demonstração

- Demonstração do pipeline

![Pipeline](/olist-marketplace/docs/pipeline.gif)


#### Pontos de interesse

- Os Datasets no Azure Data Factory foram criados com parâmetros, para serem reaproveitados nos pipelines sem precisar criar um para cada base

![Datasets](/olist-marketplace/docs/datasets.gif)

- Os notebooks utilizados podem ser encontrados [aqui](/olist-marketplace/data/notebooks/).


