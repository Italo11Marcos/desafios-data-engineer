import psycopg2

conn = psycopg2.connect(database="postgres",
                        user='user', password='password', 
                        host='::1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

teste = dict()
teste['sql'] = """CREATE TABLE EMPREGADO (\
        emp_id int,
        employee_name varchar(20),\
        employee_email varchar(30));
      """
teste['drop_empresa'] = """DROP TABLE if exists EMPREGADO cascade;"""

for key in teste:
    cursor.execute(teste[key])

conn.commit()
conn.close()