import configparser


def init():
    CONFIG = r'/home/ubuntu/megdapcodegit/audio_data/config.ini'
    config = configparser.ConfigParser()
    config.read(CONFIG)
    return config
