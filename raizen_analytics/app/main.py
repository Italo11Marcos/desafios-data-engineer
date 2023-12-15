import pathlib

from functions import *
from tracer import Tracer


if __name__ == '__main__':

    t = Tracer()

    t.log_info('Iniciando')

    t.log_info('Fazendo a leitura do arquivo')
    df = read_xlsx(pathlib.Path('vendas-combustiveis-m3.xlsx'))

    t.log_info('Tratando os dados')
    df = remove_acent(df)
    df = rename_df(df)
    df_final = transform_df(df)
    t.log_info('Tratamento finalizado')

    t.log_info('Inserindo os dados')
    insert_into_postgresl(df_final)

    t.log_info('Finalizando')