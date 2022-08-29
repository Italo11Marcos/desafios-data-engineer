import pandas as pd
import psycopg2
from sqlalchemy import create_engine

df1 = pd.read_csv(r'C:\Users\Acer\Documents\python\desafio_big_data_enginner\bases\base_de_respostas_10k_amostra.csv')

paises = df1['Country'].unique()

conn = psycopg2.connect(database="postgres",
                        user='user', password='password', 
                        host='::1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

for i in range(len(paises)):
    cursor.execute("INSERT INTO pais (nome) VALUES ('{}')".format(paises[i]))

conn.commit()
conn.close()


    