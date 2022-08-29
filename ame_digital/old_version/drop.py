import psycopg2

conn = psycopg2.connect(database="postgres",
                        user='user', password='password', 
                        host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

drop_empresa = """DROP TABLE if exists EMPRESA cascade;"""

drop_pais = """DROP TABLE if exists PAIS cascade;"""

drop_sistema_operacional = """DROP TABLE if exists SISTEMA_OPERACIONAL cascade;"""      

drop_ferramenta_comunicacao = """DROP TABLE if exists FERRAMENTA_COMUNIC cascade;"""

drop_linguagem_programacao = """DROP TABLE if exists LINGUAGEM_PROGRAMACAO cascade;"""

drop_respondente = """DROP TABLE if exists RESPONDENTE cascade;"""

drop_resp_usa_linguagem = """DROP TABLE if exists RESP_USA_LINGUAGEM cascade;"""

drop_resp_usa_ferramenta = """DROP TABLE if exists RESP_USA_FERRAMENTA cascade;"""


cursor.execute(drop_respondente)
cursor.execute(drop_resp_usa_linguagem)
cursor.execute(drop_resp_usa_ferramenta)
cursor.execute(drop_empresa)
cursor.execute(drop_pais)
cursor.execute(drop_sistema_operacional)
cursor.execute(drop_ferramenta_comunicacao)
cursor.execute(drop_linguagem_programacao)
conn.commit()
conn.close()