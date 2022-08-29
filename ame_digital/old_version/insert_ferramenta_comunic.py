import pandas as pd
import psycopg2

import re

df2 = pd.read_csv(r'C:\Users\Acer\Documents\python\desafio_big_data_enginner\bases\base_de_respostas_10k_amostra.csv')

commuication_tools = df2['CommunicationTools'].str.split(';',expand=False)
comunic = set()
list_ferramentas = list()


for tool in commuication_tools:
    list_ferramentas.append(re.findall("\'(.*?)\'",str(tool)))
    for ferramenta in list_ferramentas:
        for f in ferramenta:
            f.split(";")
            comunic.add(f)
    list_ferramentas.clear()

comunic = list(comunic)

conn = psycopg2.connect(database="postgres",
                        user='user', password='password', 
                        host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

for i in range(len(comunic)):
    cursor.execute("INSERT INTO ferramenta_comunic (nome) VALUES ('{}')".format(comunic[i]))


conn.commit()
conn.close()
