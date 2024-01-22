from loguru import logger
from datasource.api import APICollector
from aws.client import S3Client

logger.add("file_{time}.log", format="{name} {message}", rotation="5 MB")

if __name__ == "__main__":

    logger.info("Iniciando")
    # Variáveis necessárias para a execução
    url = 'https://maven-datasets.s3.amazonaws.com/LEGO+Sets/LEGO+Sets.zip'
    folder = 'download_files'
    filename = 'lego_sets.csv'

    # Instanciando s3Client
    aws = S3Client()

    APICollector(aws).start(url, folder, filename)
    logger.info("Finalizado")