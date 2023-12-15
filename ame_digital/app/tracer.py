import logging

class Tracer:

    def __init__(self, level=logging.INFO):
        self._format = f"%(asctime)s [%(levelname)s]: %(message)s"
        self._level = level

        logging.basicConfig(
            format=self._format,
            level=self._level,
            handlers=[
                logging.StreamHandler()
            ]
        )

    @staticmethod
    def log_debug(message):
        logging.debug(message)

    @staticmethod
    def log_info(message):
        logging.info(message)

    @staticmethod
    def log_error(message):
        logging.error(message)

    @staticmethod
    def log_warning(message):
        logging.warning(message)

    @staticmethod
    def log_critical(message):
        logging.critical(message)