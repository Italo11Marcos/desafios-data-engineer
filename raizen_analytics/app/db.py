import os
from sqlalchemy import create_engine

DB = os.getenv('POSTGRES_DB')
USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOST = os.getenv('POSTGRES_HOST')
PORT = os.getenv('POSTGRES_PORT')


def connection():
    return create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}')