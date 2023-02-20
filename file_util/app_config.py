import configparser


def init():
    CONFIG = r'C:\Users\Dhanyashree M\PycharmProject\audio_project\config.ini'
    config = configparser.ConfigParser()
    config.read(CONFIG)
    return config
