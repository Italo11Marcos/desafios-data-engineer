import pandas as pd
import psycopg2

conn = psycopg2.connect(database="postgres",
                        user='user', password='password', 
                        host='::1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = """CREATE TABLE EMPREGADO (\
        emp_id int,
        employee_name varchar(20),\
        employee_email varchar(30));
      """

cursor.execute(sql)
conn.commit()
conn.close()