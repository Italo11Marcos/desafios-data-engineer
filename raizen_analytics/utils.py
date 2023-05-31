import pandas as pd
from sqlalchemy import create_engine


def treat_dataframe(df):
    """
    Function that receives a Pandas DataFrame and performs the following treatments on its column names:
    - Replaces accents and special characters;
    - Converts all letters to uppercase;
    - Removes whitespaces and replaces them with underscores;
    - Check and set the correct column dtype.

    Args:
        df (pd.DataFrame): Pandas DataFrame to be processed.

    Returns:
        pd.DataFrame: Pandas DataFrame with the treated column names.
    """
    # Creates a dictionary to store translations of accents and special characters
    traducoes = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'ã': 'a', 'õ': 'o',
        'ñ': 'n', 'ç': 'c',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'Â': 'A', 'Ê': 'E', 'Î': 'I', 'Ô': 'O', 'Û': 'U',
        'À': 'A', 'È': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U',
        'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U',
        'Ã': 'A', 'Õ': 'O',
        'Ñ': 'N', 'Ç': 'C',
        '$': 'S', '.': '_', '%': 'PERCENT'
    }

    # Applies the treatments to the DataFrame columns
    df = df.rename(columns=lambda col: col.translate(str.maketrans(traducoes)).replace(' ', '_').upper())

    for column in df.columns:
        # Verifica se a coluna contém datas no formato 'yyyy-mm-dd' ou 'dd-mm-yyyy' e as converte para datetime no formato 'yyyy-mm-dd'
        if df[column].dtype == 'object' and (df[column].astype(str).str.contains('\d{2}-\d{2}-\d{4}').any()):
            df[column] = pd.to_datetime(df[column], errors='coerce', format='%d-%m-%Y').dt.strftime('%Y-%m-%d')
        elif df[column].dtype == 'object' and (df[column].astype(str).str.contains('\d{2}/\d{2}/\d{4}').any()):
            df[column] = pd.to_datetime(df[column], errors='coerce', format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
        elif df[column].dtype == 'object' and (df[column].astype(str).str.contains('\d{4}-\d{2}-\d{2}').any()):
            df[column] = pd.to_datetime(df[column], errors='coerce', format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
        elif df[column].dtype == 'object' and (df[column].astype(str).str.contains('\d{4}/\d{2}/\d{2}').any()):
            df[column] = pd.to_datetime(df[column], errors='coerce', format='%Y/%m/%d').dt.strftime('%Y-%m-%d')
        # Verifica se a coluna é booleana e converte para bool
        elif df[column].dtype == 'bool':
            df[column] = df[column].astype('bool')
        # Verifica se a coluna contém números e converte para float64
        elif pd.api.types.is_numeric_dtype(df[column]):
            if df[column].dtype == 'float64':
                df[column] = df[column].astype('float64')
            elif df[column].dtype == 'int64':
                df[column] = df[column].astype('int64')
            else:
                df[column] = pd.to_numeric(df[column], errors='coerce').astype('float64')

    return df



def connection():
    return create_engine('postgresql://airflow:airflow@localhost:5432/postgres')