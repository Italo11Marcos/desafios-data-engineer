import pandas as pd
import psycopg2

df2 = pd.read_csv(r'C:\Users\Acer\Documents\python\desafio_big_data_enginner\bases\base_de_respostas_10k_amostra.csv')

df2 = df2[df2['LanguageWorkedWith'].notna()]

progromacao = set()

linguagens_programacao = df2['LanguageWorkedWith'].str.split(';',expand=False)
for linguagem in linguagens_programacao:
    for l in linguagem:
        l.split(";")
        progromacao.add(l)

progromacao = list(progromacao)

conn = psycopg2.connect(database="postgres",
                        user='user', password='password', 
                        host='::1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

for i in range(len(progromacao)):
    cursor.execute("INSERT INTO linguagem_programacao (nome) VALUES ('{}')".format(progromacao[i]))


conn.commit()
conn.close()