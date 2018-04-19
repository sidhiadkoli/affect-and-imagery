from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import RegexpTokenizer

class Utilities:
    tokenizer = RegexpTokenizer(r'\w+') 
    stop_words = set(stopwords.words('english'))
    
    stemmer = LancasterStemmer()
    lemmatizer = WordNetLemmatizer()

    def tokenize(sentence, remove_stop=false):
        token_list = tokenizer.tokenize(inp_sentence)
        if remove_stop :
            token_list = [word for word in token_list if word not in stop_words]

        return token_list

    def tokenize_stem(sentence, remove_stop=false):
        return [stemmer.stem(word) for word in tokenize(sentence, remove_stop)]

    def tokenize_lemmatize(sentence, remove_stop=false):
        return [lemmatizer.lemmatize(word) for word in tokenize(sentence, remove_stop)]

# Sentic wordnet suraj maharajan.
