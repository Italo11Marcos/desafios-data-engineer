from db_session import create_session
from index import treat_database

from models.respondente import Respondente, RespUsaFerramenta, RespUsaLinguagem
from models.ferramenta_comunicacao import FerramentaComunicacao
from models.sistema_operacional import SistemaOperacional
from models.pais import Pais
from models.empresa import Empresa
from models.linguagem_programacao import LinguagemProgramacao

df_final, df_language, df_communication = treat_database()


def insert_so() -> None:
    sistemas_operacionais = dict(zip(df_final['OperatingSystemId'], df_final['OperatingSystem']))
    with create_session() as session:
        for id in sistemas_operacionais:
            sistema_operacional: SistemaOperacional = SistemaOperacional(id=id, nome=sistemas_operacionais[id])
            session.add(sistema_operacional)
            session.commit()


def insert_pais() -> None:
    paises = dict(zip(df_final['CountryId'], df_final['Country']))
    with create_session() as session:
        for id in paises:
            pais: Pais = Pais(id=id, nome=paises[id])
            session.add(pais)
            session.commit()


def insert_empresa() -> None:
    empresas = dict(zip(df_final['CompanySizeId'], df_final['CompanySize']))
    with create_session() as session:
        for id in empresas:
            empresa: Empresa = Empresa(id=id, tamanho=empresas[id])
            session.add(empresa)
            session.commit()


def insert_ferramenta_comunic() -> None:
    ferramentas_comunicacao = dict(zip(df_communication['CommunicationToolsId'], df_communication['CommunicationTools']))
    with create_session() as session:
        for id in ferramentas_comunicacao:
            ferramenta: FerramentaComunicacao = FerramentaComunicacao(id=id, nome=ferramentas_comunicacao[id])
            session.add(ferramenta)
            session.commit()


def insert_linguagem_programacao() -> None:
    linguagem_programacao = dict(zip(df_language['LanguageWorkedWithId'], df_language['LanguageWorkedWith']))
    with create_session() as session:
        for id in linguagem_programacao:
            programacao: LinguagemProgramacao = LinguagemProgramacao(id=id, nome=linguagem_programacao[id])
            session.add(programacao)
            session.commit()


def insert_respondente() -> None:
    with create_session() as session:
        for row in df_final.itertuples():
            respondente: Respondente = Respondente(id=row.Respondent,
                                                nome=row.RespondentName,
                                                contrib_open_source=row.OpenSource,
                                                programa_hobby=row.Hobby,
                                                salario=row.ConvertedSalary,
                                                sistema_operacional_id=row.OperatingSystemId,
                                                pais_id=row.CountryId,
                                                empresa_id=row.CompanySizeId
                                        )
            session.add(respondente)
            session.commit()


def insert_resp_usa_ferramenta() -> None:
    with create_session() as session:
        resp_usa_ferramenta = dict(zip(df_communication['Respondent'], df_communication['CommunicationToolsId']))
        for id in resp_usa_ferramenta:
            resp_ferramenta: RespUsaFerramenta = RespUsaFerramenta(ferramenta_comunic_id=resp_usa_ferramenta[id],
                                                                   respondente_id=id)
            session.add(resp_ferramenta)
            session.commit()


def insert_resp_usa_linguagem() -> None:
    with create_session() as session:
        resp_usa_linguagem = dict(zip(df_language['Respondent'], df_language['LanguageWorkedWithId']))
        for id in resp_usa_linguagem:
            resp_linguagem: RespUsaLinguagem = RespUsaLinguagem(linguagem_programacao_id=resp_usa_linguagem[id],
                                                                respondente_id=id)
            session.add(resp_linguagem)
            session.commit()