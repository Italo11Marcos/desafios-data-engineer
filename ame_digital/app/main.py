import logging

from db_session import create_tables
from insert import *
from tracer import Tracer


if __name__ == '__main__':
    t = Tracer(logging.DEBUG)
    t.log_info("Criando as tabelas")
    create_tables()
    t.log_info("Inserindo dados")
    insert_so()
    insert_pais()
    insert_empresa()
    insert_ferramenta_comunic()
    insert_linguagem_programacao()
    insert_respondente()
    insert_resp_usa_ferramenta()
    insert_resp_usa_linguagem()
    t.log_info("Fim")