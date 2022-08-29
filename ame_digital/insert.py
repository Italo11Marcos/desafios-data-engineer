from db_session import create_session

from models.respondente import Respondente, RespUsaFerramenta, RespUsaLinguagem
from models.ferramenta_comunicacao import FerramentaComunicacao
from models.sistema_operacional import SistemaOperacional
from models.pais import Pais
from models.empresa import Empresa
from models.linguagem_programacao import LinguagemProgramacao

from index import main_dataframe

from math import isnan

df_final, df_language, df_communication = main_dataframe()

def insert_so() -> None:
    sistemas_operacionais = list(df_final['OperatingSystem'].unique())
    with create_session() as session:
        for so in sistemas_operacionais:
            sistema_operacional: SistemaOperacional = SistemaOperacional(nome=so)
            session.add(sistema_operacional)
            session.commit()

def insert_pais() -> None:
    paises = list(df_final['Country'].unique())
    with create_session() as session:
        for p in paises:
            pais: Pais = Pais(nome=p)
            session.add(pais)
            session.commit()

def insert_empresa() -> None:
    empresas = list(df_final['CompanySize'].unique())
    with create_session() as session:
        for e in empresas:
            empresa: Empresa = Empresa(tamanho=e)
            session.add(empresa)
            session.commit()

def insert_ferramenta_comunic() -> None:
    ferramentas_comunicacao = list(df_communication['CommunicationTools'].unique())
    with create_session() as session:
        for f in ferramentas_comunicacao:
            ferramenta: FerramentaComunicacao = FerramentaComunicacao(nome=f)
            session.add(ferramenta)
            session.commit()

def insert_linguagem_programacao() -> None:
    linguagem_programacao = list(df_language['LanguageWorkedWith'].unique())
    with create_session() as session:
        for f in linguagem_programacao:
            programacao: LinguagemProgramacao = LinguagemProgramacao(nome=f)
            session.add(programacao)
            session.commit()

def insert_respondente() -> None:
    with create_session() as session:
        for row in df_final.itertuples():
            hobby = 1 if row.Hobby == 'Yes' else 0
            opensource = 1 if row.OpenSource == 'Yes' else 0
            if not row.ConvertedSalary or isnan(row.ConvertedSalary):
                salary = 0.0
            else:
                salary = round((row.ConvertedSalary * 3.81) / 12, 2)
            nome = 'respondente_{}'.format(row.Respondent)
            sorank = 4 if row.so_rank > 4 else row.so_rank
            companyrank = 8 if row.country_rank > 8 else row.country_rank
            countryrank = 114 if row.country_rank > 114 else row.country_rank
            respondente: Respondente = Respondente(id=row.Respondent,
                                            nome=nome,
                                            contrib_open_source=opensource,
                                            programa_hobby=hobby,
                                            salario=salary,
                                            sistema_operacional_id=sorank,
                                            pais_id=countryrank, 
                                            empresa_id=companyrank
                                        )
            session.add(respondente)
            session.commit()

def insert_resp_usa_ferramenta() -> None:
    with create_session() as session:
        for row in df_communication.itertuples():
            communication_rank = 11 if row.communication_rank > 11 else row.communication_rank
            resp_ferramenta: RespUsaFerramenta = RespUsaFerramenta(ferramenta_comunic_id=communication_rank,
                                               respondente_id=row.Respondent)
            session.add(resp_ferramenta)
            session.commit()

def insert_resp_usa_linguagem() -> None:
    with create_session() as session:
        for row in df_language.itertuples():
            languege_rank = 38 if row.languege_rank > 38 else row.languege_rank
            resp_linguagem: RespUsaLinguagem = RespUsaLinguagem(linguagem_programacao_id=languege_rank,
                                               respondente_id=row.Respondent)
            session.add(resp_linguagem)
            session.commit()

if __name__ == '__main__':
    insert_so()
    insert_pais()
    insert_empresa()
    insert_ferramenta_comunic()
    insert_linguagem_programacao()
    insert_respondente()
    insert_resp_usa_ferramenta()
    insert_resp_usa_linguagem()