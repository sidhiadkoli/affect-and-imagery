import json
import numpy as np
import os
from nltk import FreqDist as freq
from ..helperScripts.utils import Utilities

class liwc_score():
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path + '/liwc.json', 'r') as f:
            self.liwc = json.load(f)

    def get_liwc_score(self, inp_sentence):
        stem_list = Utilities.tokenize_stem(inp_sentence)
        fdist = dict(freq(stem_list))

        liwc_vec = np.array([0]*64)
        count = 0.0
        for word in fdist.keys():
            try:
                liwc_vec += np.array(self.liwc[word]) * fdist[word]
                count += fdist[word]
            except KeyError:
                pass

        return liwc_vec/count
