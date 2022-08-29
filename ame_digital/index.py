import pandas as pd


def main_dataframe():

    #df = pd.read_csv(r'C:\Users\Acer\Documents\python\desafio_big_data_enginner\bases\base_de_respostas_10k_amostra.csv')

    df = pd.read_csv('https://raw.githubusercontent.com/AmeDigital/challenge-data-engineer/master/base_de_respostas_10k_amostra.csv')

    df1 = df[['Respondent','Hobby','OpenSource','Country','CompanySize','CommunicationTools','LanguageWorkedWith','ConvertedSalary','OperatingSystem']]

    df1['LanguageWorkedWith'] = df1['LanguageWorkedWith'].str.split(';')
    df1 = df1.explode('LanguageWorkedWith').reset_index(drop=True)
    cols = list(df1.columns)
    cols.append(cols.pop(cols.index('Respondent')))
    df1 = df1[cols]

    df1['CommunicationTools'] = df1['CommunicationTools'].str.split(';')
    df1 = df1.explode('CommunicationTools').reset_index(drop=True)
    cols = list(df1.columns)
    cols.append(cols.pop(cols.index('Respondent')))
    df1 = df1[cols]

    df1['languege_rank'] = 0
    df1['communication_rank'] = 0
    df1['country_rank'] = 0
    df1['company_rank'] = 0
    df1['so_rank'] = 0

    df1['LanguageWorkedWith'] = df1['LanguageWorkedWith'].str.split(';')
    df1 = df1.explode('LanguageWorkedWith').reset_index(drop=True)
    cols = list(df1.columns)
    cols.append(cols.pop(cols.index('Respondent')))
    df1 = df1[cols]

    df1['CommunicationTools'] = df1['CommunicationTools'].str.split(';')
    df1 = df1.explode('CommunicationTools').reset_index(drop=True)
    cols = list(df1.columns)
    cols.append(cols.pop(cols.index('Respondent')))
    df1 = df1[cols]

    dfCT=df1['CommunicationTools'].unique()
    dfCT = pd.DataFrame(dfCT, columns=['tools'])
    dfCT.index = dfCT.index + 1
    dfCT['index'] = dfCT.index

    dfLW=df1['LanguageWorkedWith'].unique()
    dfLW = pd.DataFrame(dfLW, columns=['language'])
    dfLW.index = dfLW.index + 1
    dfLW['index'] = dfLW.index

    dfP=df1['Country'].unique()
    dfP = pd.DataFrame(dfP, columns=['pais'])
    dfP.index = dfP.index + 1
    dfP['index'] = dfP.index

    dfE=df1['CompanySize'].unique()
    dfE = pd.DataFrame(dfE, columns=['empresa'])
    dfE.index = dfE.index + 1
    dfE['index'] = dfE.index

    dfSO=df1['OperatingSystem'].unique()
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
    for row in df1.itertuples():
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
    df1['communication_rank'] = dfCTid['CTid']
    df1['languege_rank'] = dfLWid['LWid']
    df1['country_rank'] = dfP['Pid']
    df1['company_rank'] = dfE['Eid']
    df1['so_rank'] = dfSO['SOid']

    df1.dropna(inplace=True)

    df_language = df1[['Respondent','languege_rank','LanguageWorkedWith']]
    
    df_communication = df1[['Respondent','communication_rank','CommunicationTools']]
    
    df_operation_system = df1.groupby(['Respondent','so_rank'])['so_rank'].count().reset_index(name='count')
    df_operation_system = df_operation_system[['Respondent','so_rank']]

    df_company = df1.groupby(['Respondent','company_rank'])['company_rank'].count().reset_index(name='count')
    df_company = df_company[['Respondent','company_rank']]

    df_country = df1.groupby(['Respondent','country_rank'])['country_rank'].count().reset_index(name='count')
    df_country = df_country[['Respondent','country_rank']]

    df_final = df[['Respondent','Hobby','OpenSource','Country','CompanySize','ConvertedSalary','OperatingSystem']]
    df_final = pd.merge(df_final, df_operation_system,on='Respondent',how='inner')
    df_final = pd.merge(df_final, df_company,on='Respondent',how='inner')
    df_final = pd.merge(df_final, df_country,on='Respondent',how='inner')
    
    return df_final, df_language, df_communication