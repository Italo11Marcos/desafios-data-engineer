import pandas as pd
import logging

from tracer import Tracer

pd.options.mode.chained_assignment = None

t = Tracer(logging.DEBUG)


def gera_dict(df: pd.DataFrame, col: str) -> dict:
    """
        Função que retorna um dicionario com o elemento e seu
        indice como ID
        Return: Dicionario
    """
    dicionario = {}
    for indice, elemento in enumerate(list(df[col].dropna().unique()), start=1):
        dicionario[elemento] = indice

    return dicionario


def concat_respondent(col: str) -> str:
    """
        Concatena o id do respondent com o prefixo 'respondent_'
        Return: Uma string resultante da concatenação do id do respondent com 'respondent_'
    """
    return 'respondent_'+str(col)


def treat_database() -> tuple:
    """
        Essa função faz a leitura e o tratamento do arquivo
        Return: uma tupla de dataframes
    """
    t.log_info('Fazendo a leitura do arquivo')
    df = pd.read_csv('https://raw.githubusercontent.com/AmeDigital/challenge-data-engineer/master/base_de_respostas_10k_amostra.csv', sep=',')

    t.log_info('Realizando os tratamentos')
    # Seleciona somente as colunas necessárias
    df_treat = df[['Respondent', 'Hobby', 'OpenSource', 'Country', 'CompanySize', 'CommunicationTools',
                   'LanguageWorkedWith', 'ConvertedSalary', 'OperatingSystem']]

    # Os valores 'NA' são convertidos para 0.0
    df_treat['ConvertedSalary'] = df_treat['ConvertedSalary'].fillna(0.0)

    # Converte para real (3.14) e em valor mensal
    df_treat['ConvertedSalary'] = ((df_treat['ConvertedSalary'] * 3.81) / 12)

    # Arredonda para 2 casas decimais
    df_treat = df_treat.round(2)

    # Converte para boolean
    dict_yes_no = {'Yes': 1, 'No': 0}
    df_treat['Hobby'] = df_treat['Hobby'].replace(dict_yes_no)
    df_treat['OpenSource'] = df_treat['OpenSource'].replace(dict_yes_no)

    # Cria nova coluna com o id concatenado
    df_treat['RespondentName'] = df_treat['Respondent'].apply(concat_respondent)

    # Faz split das colunas para transformar em lista
    df_treat['CommunicationTools'] = df_treat['CommunicationTools'].str.split(';')
    df_treat['LanguageWorkedWith'] = df_treat['LanguageWorkedWith'].str.split(';')

    # Deleta os valores nulos
    df_treat.dropna(inplace=True)

    # Transforma cada elemento da lista em uma nova linha
    df_exploded_lww = df_treat[['Respondent', 'LanguageWorkedWith']].explode('LanguageWorkedWith')
    df_exploded_ct = df_treat[['Respondent', 'CommunicationTools']].explode('CommunicationTools')

    # Cria nova coluna com ID
    company_dict = gera_dict(df_treat, 'CompanySize')
    df_treat['CompanySizeId'] = df_treat['CompanySize'].replace(company_dict)
    country_dict = gera_dict(df_treat, 'Country')
    df_treat['CountryId'] = df_treat['Country'].replace(country_dict)
    operating_system_dict = gera_dict(df_treat, 'OperatingSystem')
    df_treat['OperatingSystemId'] = df_treat['OperatingSystem'].replace(operating_system_dict)
    lww_dict = gera_dict(df_exploded_lww, 'LanguageWorkedWith')
    df_exploded_lww['LanguageWorkedWithId'] = df_exploded_lww['LanguageWorkedWith'].replace(lww_dict)
    ct_dict = gera_dict(df_exploded_ct, 'CommunicationTools')
    df_exploded_ct['CommunicationToolsId'] = df_exploded_ct['CommunicationTools'].replace(ct_dict)

    return df_treat, df_exploded_lww, df_exploded_ct