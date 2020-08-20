import logging


class custom_logger:

    @staticmethod
    def cust_log():
        logging.basicConfig(filename='Backend//Logs//application.log',
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
