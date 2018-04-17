import json
from nltk.stem.lancaster import LancasterStemmer
from nltk import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk import FreqDist as freq
import numpy as np

"""with open('liwc.cat', 'r') as f:
	liwc_cat = f.read().splitlines()

liwc_json = {}
for i in range(1, 65):
	print i
	with open('dictionary/{}.csv'.format(i), 'r') as f:
		words = f.read().splitlines()
		for word in words:
			#print word
			#word = word.encode('utf-8')
			try :
				liwc_json[word][i-1] += 1
			except KeyError:
				liwc_json[word] = [0]*64
				liwc_json[word][i-1] = 1

print liwc_json
with open('liwc.json', 'w') as f:
	json.dump(liwc_json, f)"""

class liwc_score():
	def __init__(self):
		with open('liwc.json', 'r') as f:
			self.liwc = json.load(f)
		self.stemmer = LancasterStemmer()
		#self.stemmer = PorterStemmer()
		self.tokenizer = RegexpTokenizer(r'\w+')	
		self.stop_words = set(stopwords.words('english'))

	#Remove stopwords ? 
	def token_stemmer(self, inp_sentence, remove_stop = False):
		token_list = self.tokenizer.tokenize(inp_sentence)
		if remove_stop :
			token_list = [word for word in token_list if word not in self.stop_words] 
		stem_list = [self.stemmer.stem(word) for word in token_list]

		return stem_list

	def get_liwc_score(self, inp_sentence):
		stem_list = self.token_stemmer(inp_sentence)
		fdist = dict(freq(stem_list))

		liwc_vec = np.array([0]*64)
		count = 0.0
		for word in fdist.keys():
			try :
				#print self.liwc[word]
				liwc_vec += np.array( self.liwc[word] )*fdist[word]
				count += fdist[word]
			except KeyError:
				pass

		return liwc_vec/count

if __name__ == "__main__":
	with open('test', 'r') as f:
		inp_data = f.read()

	l = liwc_score()
	print l.get_liwc_score(inp_data)








