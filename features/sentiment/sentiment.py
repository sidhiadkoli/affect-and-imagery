import numpy as np
from senticnet.senticnet import SenticNet
#from ..helperScripts.utils import Utilities
from utils import Utilities

# To remove:
import json

class Sentiment:
    def __init__(self):
        self.sn = SenticNet()

    # Returns polarity intensity and the following sentic values:
    # pleasantness, attention, sensitivity, aptitude.
    def get_intensity_sentics(self, data, name):
        tokens = Utilities.tokenize_lemmatize(data, remove_stop=True)
        scores = []

        for t in tokens:
            try:
                #print(t)
                concept = self.sn.concept(t)
                #print(concept)
                sentics = concept["sentics"]
                scores.append([float(concept["polarity_intense"]), float(sentics["pleasantness"]), 
                    float(sentics["attention"]), float(sentics["sensitivity"]), float(sentics["aptitude"])])                
            except:
                pass

        # Get average score across all words.
        if len(scores) == 0:
            print("None ", name)
            return [0.0] * 5

        avgScore = []
        scores = np.array(scores).T
        #print(scores)

        for i in range(5):
            avgScore.append(np.average(scores[i]))

        return avgScore

if __name__ == "__main__":
    fin = open("../../data/dataCleaned.txt")
    reddit = json.load(fin)

    sen = Sentiment()
    sentiment = {}

    for r in reddit:
        #print(r["name"])
        sentiment[r["name"]] = sen.get_intensity_sentics(r["selftext"], r["name"])

    fout = open("sentiment.json", "w")
    json.dump(sentiment, fout)



