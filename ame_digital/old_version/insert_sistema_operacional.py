import pandas as pd
import psycopg2

df2 = pd.read_csv(r'C:\Users\Acer\Documents\python\desafio_big_data_enginner\bases\base_de_respostas_10k_amostra.csv')

#print(df2['OperatingSystem'])

#print(df2['Country'].unique())

so = df2['OperatingSystem'].unique()

conn = psycopg2.connect(database="postgres",
                        user='user', password='password', 
                        host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

for i in range(len(so)):
    cursor.execute("INSERT INTO sistema_operacional (nome) VALUES ('{}')".format(so[i]))


conn.commit()
conn.close()


    