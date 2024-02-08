import configparser

read_config = configparser.RawConfigParser()
read_config.read("sample_framework/configuration/config.ini")


class ReadConfig:
    @staticmethod
    def get_url():
        url = read_config.get("common info", "url")
        return url

    @staticmethod
    def get_username():
        username = read_config.get("common info", "username")
        return username

    @staticmethod
    def get_password():
        password = read_config.get("common info", "password")
        return password

