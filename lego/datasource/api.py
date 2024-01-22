import pandas as pd
import requests
import zipfile
import pathlib
import datetime
from io import BytesIO
from loguru import logger


class APICollector:

    def __init__(self, aws):
        """
        Inicia uma instancia da APICollector
        :param aws: Objeto representando conexão com AWS para upload de arquivos
        """
        self._aws = aws
        self._buffer = None
        return

    def start(self, url, folder, filename):
        """
        Inicia o download dos dados, transformação e o upload
        :param url: URL a qual se pretende buscar os dados
        :param folder: Pasta local onde os arquivos vão ser salvos
        :param filename: O nome do arquivo a ser processado
        :return: True se o processo for sucesso, False, caso contrário
        """
        self.getData(url, folder)
        response = self.transformData(folder, filename)
        response = self.convertToParquet(response)

        if self._buffer is not None:
            upload_filename = self.fileName(filename)
            logger.info(f'Filename will be saved: {upload_filename}')
            self._aws.upload_file(response, upload_filename)
            return True
        else:
            return False

    def getData(self, url, folder):
        """
        Busca os dados na URL especificada e salva na pasta local
        :param url: URL a qual se pretende buscar os dados
        :param folder: Pasta local onde os arquivos vão ser salvos
        :return:
        """
        try:
            logger.info(f"Requesting: {url}")
            r = requests.get(url, timeout=3)
            r.raise_for_status()
            zip_file = BytesIO(r.content)
            # Open the zip file
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(folder)
        except requests.exceptions.HTTPError as errh:
            logger.debug("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            logger.debug("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            logger.debug("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            logger.debug("OOps: Something Else", err)

    def transformData(self, folder, filename):
        """
        Le o arquivo CSV da pasta local, transforma em um
        arquivo pd.DataFrame e adiciona uma coluna timestamp
        :param folder: Pasta local onde os arquivo está salvo
        :param filename: Nome do arquivo que será tratado
        :return: pd.DataFrame com os dados tratados
        """
        logger.info(f"Lendo df: {filename}")
        pathfile = pathlib.Path(folder, filename)
        df = pd.read_csv(pathfile, sep=',')
        df = df.rename(columns=str.lower)
        df['extracted_at'] = self.dataAtual()
        logger.info("Tratamento finalizado")
        return df

    def convertToParquet(self, response):
        """
        Converte o pd.DataFrame fornecido para o formato Parquet e armazena-o num buffer BytesIO
        :param response: pd.DataFrame tratado
        :return: BytesIO com os dados .parquet se for bem sucedido. None, caso contrário
        """
        self._buffer = BytesIO()
        try:
            response.to_parquet(self._buffer)
            return self._buffer
        except:
            logger.error("Erro ao transformar o DF em parquet")
            self._buffer = None

    def dataAtual(self):
        """
        :return: Devolve a data e a hora atuais em formato ISO, excluindo milissegundos
        """
        data_atual = datetime.datetime.now().isoformat()
        return data_atual.split(".")[0]

    def fileName(self, filename):
        """
        :param filename: Nome do arquivo para servir de base
        :return: Retorna o nome do arquivo para ser salvo no bucket, contendo a data atual
        """
        filename = filename.split(".csv")[0]
        data_atual = self.dataAtual().replace(":", "-")
        return f"raw/{filename}_{data_atual}.parquet"
