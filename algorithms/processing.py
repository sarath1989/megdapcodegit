from resemblyzer import preprocess_wav, VoiceEncoder
from pyannote.audio import Model, Inference
import log_file as log
import time
from file_util import app_config as conf

st = time.process_time()
encoder = VoiceEncoder()

config = conf.init()
model = Model.from_pretrained("pyannote/embedding", use_auth_token=config["SETTINGS"]["token"])
inference = Inference(model, window="whole")
dict_file = {}
sim_grp = []
diff_grp = []


def check_availability(from_idx, to_idx):
    global preprocess_f1, preprocess_f2, embedded_f1, embedded_f2
    if from_idx['filename'] not in dict_file.keys():
        embedded_f1 = embedding_inf(from_idx)
        preprocess_f1 = trim_silences(from_idx)
        dict_file[from_idx['filename']] = {'embedded':embedded_f1,'preprocess': preprocess_f1}
        log.logger.info(
            f"generating embedded and preprocess and updated on dictionary for file1 :{from_idx['filename']}")
    elif from_idx['filename'] in dict_file.keys():
        embedded_f1 = dict_file[from_idx['filename']]['embedded']
        preprocess_f1 = dict_file[from_idx['filename']]['preprocess']
        log.logger.info(f"fetching embedded and preprocess from dictionary for file1 :{from_idx['filename']}")
    if to_idx['filename'] not in dict_file.keys():
        embedded_f2 = embedding_inf(to_idx)
        preprocess_f2 = trim_silences(to_idx)
        dict_file[to_idx['filename']] = {'embedded':embedded_f2,'preprocess': preprocess_f2}
        log.logger.info(f"generating embedded and preprocess and updated on dictionary for file2 :{to_idx['filename']}")
    elif to_idx['filename'] in dict_file.keys():
        embedded_f2 = dict_file[to_idx['filename']]['embedded']
        preprocess_f2 = dict_file[to_idx['filename']]['preprocess']
        log.logger.info(f"fetching embedded and preprocess from dictionary for file2 :{from_idx['filename']}")
    preprocess_f2.update(preprocess_f1)
    # merge(preprocess_f1, preprocess_f2)
    return embedded_f1,embedded_f2,preprocess_f2


def trim_silences(idx):
    speaker_audio = {idx['filename']: [preprocess_wav(idx['fullpath'])]}
    return speaker_audio


def embedding_inf(idx):
    embedding = inference(idx['fullpath'])
    return embedding






