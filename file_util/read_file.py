import os
from pathlib import Path
import file_util.app_config as conf


config = conf.init()
base_path = config['SETTINGS']['basepath']


def fetch_file():
    files = {}
    for f in Path(base_path).glob("**/*.wav"):
        list_of_files = files.get(os.path.basename(os.path.dirname(f)), [])
        list_of_files.append({"filename": os.path.basename(f), "fullpath": f})
        files[os.path.basename(os.path.dirname(f))] = list_of_files
    return files

