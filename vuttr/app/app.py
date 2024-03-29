from fastapi import FastAPI

from settings import settings
from api.v1.api import api_router
from db_session import create_tables

from loguru import logger


app = FastAPI(title='Vuttr App')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':

    logger.info("Criando as tabelas")
    create_tables()
    
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)