
#******************************************_Tokenization_**********************************
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import string
import unicodedata as ud
from nltk import word_tokenize


class Tokenization():
    def getData(self):
        pass

    def tokenizationProcess(example_sent):

        tokens = word_tokenize(example_sent)
        return tokens

#*******************************************_Stop words_**********************************


class StopWords():
    def deleteStopWords(example_sent):
        stopwords_list = stopwords.words('arabic')
        word_tokens = Tokenization.tokenizationProcess(example_sent)
        filtered_sentence = []
        for w in word_tokens:
            if w not in stopwords_list:
                filtered_sentence.append(w)
        return filtered_sentence


#********************************************_stemming_****************************************

class Stemming():
    def getData(self):
        pass

    def defineStemming(example_sent):
        word_tokens = Tokenization.tokenizationProcess(example_sent)
        filtered_sentence = []
        ps = nltk.ISRIStemmer()
        for w in word_tokens:
            filtered_sentence.append(ps.stem(w))
        return filtered_sentence

#***************************************_Lemmatization_****************************************


class Lemmatization():

    def getLemmatization(example_sent):
        word_tokens = Tokenization.tokenizationProcess(example_sent)
        filtered_sentence = []

        for w in word_tokens:
            filtered_sentence.append(nltk.ISRIStemmer().suf32(w))
        return filtered_sentence

#*****************************************_punctuation_************************************


class Punctuation():
    def removePunctuations(example_sent):
        file = open("test.txt", 'w', encoding="utf-8")
        words = ''.join(
            c for c in example_sent if not ud.category(c).startswith('P'))
        file.write(words)
        file.close()
        return words


#******************************************_bag_of_words_**********************************


class BagOfWords():

    def getbagOfWords(example_sent):
        vect = CountVectorizer()
        bag_of_words = vect.transform(example_sent)

        print(format(bag_of_words.toarray()))


#if __name__ == '__main__':
#    Stemming.defineStemming(self=0)
