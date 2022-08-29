import psycopg2

conn = psycopg2.connect(database="postgres",
                        user='user', password='password', 
                        host='localhost', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

create_empresa = """CREATE TABLE EMPRESA (\
        id serial,
        tamanho varchar(100),
        PRIMARY KEY(id)
        );
      """

create_pais = """CREATE TABLE PAIS (\
        id serial,
        nome varchar(100),
        PRIMARY KEY(id)
        );
      """

create_sistema_operacional = """CREATE TABLE SISTEMA_OPERACIONAL (\
        id serial,
        nome varchar(100),
        PRIMARY KEY(id)
        );
      """      

create_ferramenta_comunicacao = """CREATE TABLE FERRAMENTA_COMUNIC (\
        id serial,
        nome varchar(100),
        PRIMARY KEY(id)
        );
      """

create_linguagem_programacao = """CREATE TABLE LINGUAGEM_PROGRAMACAO (\
        id serial,
        nome varchar(100),
        PRIMARY KEY(id)
        );
      """

create_respondente = """CREATE TABLE RESPONDENTE (\
        id serial,
        nome varchar(100),
        contrib_open_source smallint,
        programa_hobby smallint,
        salario decimal,
        sistema_operacional_id int,
        pais_id int,
        empresa_id int,
        PRIMARY KEY(id),
        CONSTRAINT fk_sistema_operacional
            FOREIGN KEY(sistema_operacional_id)
                REFERENCES SISTEMA_OPERACIONAL(id)
                ON DELETE CASCADE,
        CONSTRAINT fk_pais
            FOREIGN KEY(pais_id)
                REFERENCES PAIS(id)
                ON DELETE CASCADE,
        CONSTRAINT fk_empresa
            FOREIGN KEY(empresa_id)
                REFERENCES EMPRESA(id)
                ON DELETE CASCADE
        );
      """

create_resp_usa_linguagem = """CREATE TABLE RESP_USA_LINGUAGEM (\
        respondente_id int,
        linguagem_programacao_id int,
        momento smallint,
        CONSTRAINT fk_respondente
            FOREIGN KEY(respondente_id)
                REFERENCES RESPONDENTE(id)
                ON DELETE CASCADE,
        CONSTRAINT fk_linguagem_programacao
            FOREIGN KEY(linguagem_programacao_id)
                REFERENCES LINGUAGEM_PROGRAMACAO(id)
                ON DELETE CASCADE
        );
      """

create_resp_usa_ferramenta = """CREATE TABLE RESP_USA_FERRAMENTA (\
        ferramenta_comunic_id int,
        respondente_id int,
        CONSTRAINT fk_respondente
            FOREIGN KEY(respondente_id)
                REFERENCES RESPONDENTE(id)
                ON DELETE CASCADE,
        CONSTRAINT fk_ferramenta_comunic
            FOREIGN KEY(ferramenta_comunic_id)
                REFERENCES FERRAMENTA_COMUNIC(id)
                ON DELETE CASCADE        
        );
      """


cursor.execute(create_empresa)
cursor.execute(create_pais)
cursor.execute(create_sistema_operacional)
cursor.execute(create_ferramenta_comunicacao)
cursor.execute(create_linguagem_programacao)
cursor.execute(create_respondente)
cursor.execute(create_resp_usa_linguagem)
cursor.execute(create_resp_usa_ferramenta)
conn.commit()
conn.close()