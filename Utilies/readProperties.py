import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'url')
        return url

    @staticmethod
    def get_user_name():
        username = config.get('common info', 'user_name')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
