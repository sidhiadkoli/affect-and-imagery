import json
from nltk import FreqDist as freq
from ..helperScripts.utils import Utilities

class vad_score():
    def __init__(self):
        with open('warriner.json', 'r') as f:
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


if __name__ == "__main__":
    with open('test', 'r') as f:
        inp_data = f.read()

    l = vad_score()
    print(l.get_vad_score(inp_data))

"""with open('warriner.csv', 'r') as f:
    vad_raw = f.read().splitlines()

vad_json = {}
for i in vad_raw[1:]:
    i = i.split(",")
    item = {}
    item['v'] = float(i[2])
    item['a'] = float(i[5])
    item['d'] = float(i[8])
    vad_json[i[1]] = item

with open('warriner.json', 'w') as f:
    json.dump(vad_json, f)"""