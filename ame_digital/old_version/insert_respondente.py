import pandas as pd
import psycopg2

from math import isnan

df2 = pd.read_csv(r'C:\Users\Acer\Documents\python\desafio_big_data_enginner\bases\base_de_respostas_10k_amostra.csv')

df3 = df2[['Respondent','Hobby','OpenSource','Country','CompanySize','CommunicationTools','LanguageWorkedWith','ConvertedSalary','OperatingSystem']]

df3['LanguageWorkedWith'] = df3['LanguageWorkedWith'].str.split(';')
df3 = df3.explode('LanguageWorkedWith').reset_index(drop=True)
cols = list(df3.columns)
cols.append(cols.pop(cols.index('Respondent')))
df3 = df3[cols]

df3['CommunicationTools'] = df3['CommunicationTools'].str.split(';')
df3 = df3.explode('CommunicationTools').reset_index(drop=True)
cols = list(df3.columns)
cols.append(cols.pop(cols.index('Respondent')))
df3 = df3[cols]

df3['languege_rank'] = 0
df3['communication_rank'] = 0
df3['country_rank'] = 0
df3['company_rank'] = 0
df3['so_rank'] = 0

dfCT=df3['CommunicationTools'].unique()
dfCT = pd.DataFrame(dfCT, columns=['tools'])
dfCT.index = dfCT.index + 1
dfCT['index'] = dfCT.index

dfLW=df3['LanguageWorkedWith'].unique()
dfLW = pd.DataFrame(dfLW, columns=['language'])
dfLW.index = dfLW.index + 1
dfLW['index'] = dfLW.index

dfP=df3['Country'].unique()
dfP = pd.DataFrame(dfP, columns=['pais'])
dfP.index = dfP.index + 1
dfP['index'] = dfP.index

dfE=df3['CompanySize'].unique()
dfE = pd.DataFrame(dfE, columns=['empresa'])
dfE.index = dfE.index + 1
dfE['index'] = dfE.index

dfSO=df3['OperatingSystem'].unique()
dfSO = pd.DataFrame(dfSO, columns=['so'])
dfSO.index = dfSO.index + 1
dfSO['index'] = dfSO.index


def get_id_communication_tools(tool):
    return list(dfCT.loc[dfCT['tools'] == tool]['index'])

def get_id_language_worked(language):
    return list(dfLW.loc[dfLW['language'] == language]['index'])

def get_id_pais(pais):
    return list(dfP.loc[dfP['pais'] == pais]['index'])

def get_id_empresa(empresa):
    return list(dfE.loc[dfE['empresa'] == empresa]['index'])

def get_id_so(so):
    return list(dfSO.loc[dfSO['so'] == so]['index'])

communication_tools_id = []
language_worked_id = []
country_id = []
empresa_id = []
so_id = []

for row in df3.itertuples():
    communication_tools_id.append(get_id_communication_tools(row.CommunicationTools))
    language_worked_id.append(get_id_language_worked(row.LanguageWorkedWith))
    country_id.append(get_id_pais(row.Country))
    empresa_id.append(get_id_empresa(row.CompanySize))
    so_id.append(get_id_so(row.OperatingSystem))

dfCTid = pd.DataFrame(communication_tools_id, columns = ['CTid'])
dfLWid = pd.DataFrame(language_worked_id, columns = ['LWid'])
dfP = pd.DataFrame(country_id, columns = ['Pid'])
dfE = pd.DataFrame(empresa_id, columns=['Eid'])
dfSO = pd.DataFrame(so_id, columns=['SOid'])
df3['communication_rank'] = dfCTid['CTid']
df3['languege_rank'] = dfLWid['LWid']
df3['country_rank'] = dfP['Pid']
df3['company_rank'] = dfE['Eid']
df3['so_rank'] = dfSO['SOid']

df3.dropna(inplace=True)

conn = psycopg2.connect(database="postgres",
                        user='user', password='password', 
                        host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

for row in df3.itertuples():
    hobby = 1 if row.Hobby == 'Yes' else 0
    opensource = 1 if row.OpenSource == 'Yes' else 0
    if not row.ConvertedSalary or isnan(row.ConvertedSalary):
        salary = 0.0
    else:
        salary = round((row.ConvertedSalary * 3.81) / 12, 2)
    nome = 'respondente_{}'.format(row.Respondent)
    cursor.execute("INSERT INTO respondente (nome, contrib_open_source, programa_hobby, salario, sistema_operacional_id, pais_id, empresa_id) \
                    VALUES ('{}','{}','{}','{}',{},{},{})".format(nome, hobby, opensource, salary, row.so_rank, row.country_rank, row.company_rank))


conn.commit()
conn.close()


    