import configparser

config = configparser.RawConfigParser()
config.read('Backend\Config\configurations.ini')


class ReadConfig:

    @staticmethod
    def get_EmailID():
        return config.get('credentials', 'EmailID')

    @staticmethod
    def get_Password():
        return config.get('credentials', 'Password')

    @staticmethod
    def get_URL():
        return config.get('Environment', 'URL1')
