import numpy as np
from scipy.spatial.distance import cdist
from resemblyzer import VoiceEncoder

encoder = VoiceEncoder()
dict_utt = {}


def distance_calculation(embedding1, embedding2):
    distance = cdist(embedding1, embedding2, metric="cosine")[0, 0]
    similarity_distance = 1 - distance
    return similarity_distance


def comparison(speaker_wavs, from_idx, to_idx):
    global from_cmp_utt, to_cmp_utt
    if from_idx['filename'] not in dict_utt.keys():
        from_cmp_utt = np.array([encoder.embed_utterance(list(speaker_wavs[from_idx['filename']])[0])])
        dict_utt[from_idx['filename']] = {'file_utt': from_cmp_utt}
        print(dict_utt)
    elif from_idx['filename'] in dict_utt.keys():
        from_cmp_utt = dict_utt[from_idx['filename']]['file_utt']
    if to_idx['filename'] not in dict_utt.keys():
        to_cmp_utt = np.array([encoder.embed_utterance(list(speaker_wavs[to_idx['filename']])[0])])
        dict_utt[to_idx['filename']] = {'file_utt': to_cmp_utt}
    elif to_idx['filename'] in dict_utt.keys():
        to_cmp_utt = dict_utt[from_idx['filename']]['file_utt']
    utt_sim_matrix = np.inner(from_cmp_utt, to_cmp_utt)
    return utt_sim_matrix
