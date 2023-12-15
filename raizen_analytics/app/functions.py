import pandas as pd
from unidecode import unidecode

from db import connection
from tracer import Tracer
from sqlalchemy import text

t = Tracer()


def classify_combustivel(col):
    """
        Function that classify combustível type based on the given value

        Args:
            col (str): Value to be classified

        Retuns:
            str: combustível classified. Can be 'diesel' if the value is present in the list of types of diesel,
             else, will be 'fuels'.

        Exemplo:
        >>> classify_combustivel("OLEO DIESEL S-10 (m3)")
        'diesel'
        >>> classify_combustivel("GASOLINA (m3)")
        'fuels'
        """
    diesel = ["OLEO DIESEL (OUTROS) (m3)",
             "OLEO DIESEL MARITIMO (m3)",
             "OLEO DIESEL S-10 (m3)",
             "OLEO DIESEL S-1800 (m3)",
             "OLEO DIESEL S-500 (m3)"]

    if col in diesel:
        return 'diesel'
    else:
        return 'fuels'

def read_xlsx(path):

    appended_data = []

    # Ler as spreadsheets e concatena em um único DataFrame
    for i in range(1, 3):
        data = pd.read_excel(path, f'DPCache_m3_{i}')
        appended_data.append(data)

    df = pd.concat(appended_data)

    return df


def remove_acent(df):

    df.columns = [unidecode(c.upper()) for c in df.columns]

    df['COMBUSTIVEL'] = df['COMBUSTIVEL'].astype(str)
    df['COMBUSTIVEL'] = df['COMBUSTIVEL'].map(unidecode)

    df['REGIAO'] = df['REGIAO'].astype(str)
    df['REGIAO'] = df['REGIAO'].map(unidecode)

    df['ESTADO'] = df['ESTADO'].astype(str)
    df['ESTADO'] = df['ESTADO'].map(unidecode)

    return df


def rename_df(df):

    df = df[['COMBUSTIVEL', 'ANO', 'ESTADO', 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']]

    # Renomear as colunas
    df.rename(columns={'JAN': '01', 'FEV': '02', 'MAR': '03',
                       'ABR': '04', 'MAI': '05', 'JUN': '06',
                       'JUL': '07', 'AGO': '08', 'SET': '09',
                       'OUT': '10', 'NOV': '11', 'DEZ': '12',
                       'COMBUSTIVEL': 'PRODUCT', 'ESTADO': 'UF'}, inplace=True)

    return df


def transform_df(df):

    # Utilize a função melt para fundir as colunas de meses
    df_final = df.melt(
        id_vars=['PRODUCT', 'ANO', 'UF'],
        value_vars=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        var_name='MES',
        value_name='VOLUME'
    )

    # Extrair o ano e o mês da coluna "MES" e criar a coluna "YEAR_MONTH"
    df_final['YEAR_MONTH'] = df_final['ANO'].astype(str) + '-' + df_final['MES']
    df_final = df_final[['PRODUCT', 'YEAR_MONTH', 'UF', 'VOLUME']]

    # Cria a coluna UNIT
    df_final['UNIT'] = df_final['PRODUCT'].apply(classify_combustivel)

    # Cria a coluna CREATED_AT
    df_final['CREATED_AT'] = pd.Timestamp.today().strftime('%Y-%m-%d %H:%M:%S')
    df_final['CREATED_AT'] = df_final['CREATED_AT'].astype('datetime64[ns]')

    # Preenche os valores NaN com 0
    df_final.fillna(0, inplace=True)

    return df_final


def insert_into_postgresl(df_final):
    # Chama a função para criar a conexão com o BD
    engine = connection()

    statment = """
        create table if not exists anp_sales (
        year_month varchar(7),
        uf varchar(20),
        product varchar(50),
        unit varchar(10),
        volume numeric(10,2),
        created_at timestamp
    );
    """
    # Cria a tabela se não existir
    with engine.connect() as conn:
        conn.execute(text(statment))

    # Transforma as colunas em lower case para fazer o insert no BD
    df_final.columns = [c.lower() for c in df_final.columns]

    # Faz a inserção no BD
    df_final.to_sql("anp_sales", engine, if_exists='append', index=False)

    t.log_info('Inserção banco de dados concluído')

