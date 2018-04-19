import json
from nltk import FreqDist as freq
from ..helperScripts.utils import Utilities

class vad_score():
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path + '/warriner.json', 'r') as f:
            self.vad = json.load(f)

    def get_vad_score(self, inp_sentence):
        token_list = Utilities.tokenize_lemmatize(inp_sentence)
        fdist = dict(freq(token_list))

        v_sum = 0.0
        a_sum = 0.0
        d_sum = 0.0
        count = 0.0

        for word in fdist.keys():
            try:
                v_sum = self.vad[word]['v']*fdist[word]
                a_sum = self.vad[word]['a']*fdist[word]
                d_sum = self.vad[word]['d']*fdist[word]
                count += fdist[word]
            except KeyError:
                pass
                
        return (v_sum/count, a_sum/count, d_sum/count)