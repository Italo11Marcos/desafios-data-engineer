import pandas as pd
import psycopg2

df2 = pd.read_csv(r'C:\Users\Acer\Documents\python\desafio_big_data_enginner\bases\base_de_respostas_10k_amostra.csv')

empresas = df2['CompanySize'].unique()

conn = psycopg2.connect(database="postgres",
                        user='user', password='password', 
                        host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

for i in range(len(empresas)):
    cursor.execute("INSERT INTO empresa (tamanho) VALUES ('{}')".format(empresas[i]))

conn.commit()
conn.close()


    