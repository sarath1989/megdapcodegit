import numpy as np
from scipy.spatial.distance import cdist
from resemblyzer import VoiceEncoder

encoder = VoiceEncoder()


def distance_calculation(embedding1, embedding2):
    distance = cdist(embedding1, embedding2, metric="cosine")[0, 0]
    similarity_distance = 1 - distance
    return similarity_distance


def comparison(speaker_wavs, from_idx, to_idx):
    from_cmp_embed = np.array([encoder.embed_utterance(list(speaker_wavs[from_idx['filename']])[0])])
    to_cmp_embed = np.array([encoder.embed_utterance(list(speaker_wavs[to_idx['filename']])[0])])
    utt_sim_matrix = np.inner(from_cmp_embed, to_cmp_embed)
    return utt_sim_matrix
