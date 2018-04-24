from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import RegexpTokenizer

class Utilities:
    tokenizer = RegexpTokenizer(r'\w+') 
    stop_words = set(stopwords.words('english'))
    
    stemmer = LancasterStemmer()
    lemmatizer = WordNetLemmatizer()

    def tokenize(sentence, remove_stop=False):
        token_list = Utilities.tokenizer.tokenize(sentence)
        token_list = [word.lower() for word in token_list]
        if remove_stop :
            token_list = [word for word in token_list if word not in Utilities.stop_words]

        return token_list

    def tokenize_stem(sentence, remove_stop=False):
        return [Utilities.stemmer.stem(word) for word in Utilities.tokenize(sentence, remove_stop)]

    def tokenize_lemmatize(sentence, remove_stop=False):
        return [Utilities.lemmatizer.lemmatize(word) for word in Utilities.tokenize(sentence, remove_stop)]
