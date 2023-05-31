from functions import *

if __name__ == '__main__':

    path = 'vendas-combustiveis-m3.xlsx'

    df = read_xlsx(path)

    df = treat_dataframe(df)

    df = remove_acent(df)

    df = rename_df(df)

    df_final = transform_df(df)

    insert_into_postgresl(df_final)