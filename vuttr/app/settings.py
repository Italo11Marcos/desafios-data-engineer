import os

from pydantic_settings import BaseSettings

DB=os.getenv('POSTGRES_DB')
USER=os.getenv('POSTGRES_USER')
PASSWORD=os.getenv('POSTGRES_PASSWORD')
HOST=os.getenv('POSTGRES_HOST')
PORT=os.getenv('POSTGRES_PORT')


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    #DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()