import logging
import os.path
import time


class custom_logger:
    def __init__(self):
        """
            Initializes the logger object.
                * Spcefied the log file path.
                * Sepcified the log format
                * Specified the log level
        """

        # Create logger
        self.logger = logging.getLogger()

        self.logger.setLevel(logging.DEBUG)

        # Create handler，to write logs
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath(
            '.')) + '\\nopCommerceFramework\\Backend\\Logs\\'
        log_name = log_path + rq + '.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # Output format of the handler
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # Adding handler to logger object
        self.logger.addHandler(fh)

    def getlog(self):
        return self.logger
        # self.logger.removeHandler(fh)
