
#******************************************_Tokenization_**********************************
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag_sents
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from num2words import num2words
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import string
import unicodedata as ud
from nltk import word_tokenize
from nltk.tag import UnigramTagger

class Tokenization():
    def getData(self):
        pass

    def tokenizationProcess(example_sent):

        tokens = word_tokenize(example_sent)
        return tokens

#*******************************************_Stop words_**********************************


class StopWords():

    #---------- arabic
    def deleteStopWords(example_sent):
        stopwords_list = stopwords.words('arabic')
        word_tokens = Tokenization.tokenizationProcess(example_sent)
        filtered_sentence = []
        for w in word_tokens:
            if w not in stopwords_list:
                filtered_sentence.append(w)
        return filtered_sentence

    #---------- english
    def deleteStopWordsEn(example_sent):
        stopwords_list = stopwords.words('english')
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


class StemmingEn():
    def getData(self):
        pass

    def defineStemming(example_sent):
        word_tokens = Tokenization.tokenizationProcess(example_sent)
        filtered_sentence = []
        ps = PorterStemmer()
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


class LemmatizationEn():

    def getLemmatization(example_sent):
        lemmatizer = WordNetLemmatizer()
        word_tokens = Tokenization.tokenizationProcess(example_sent)
        lemmatized = []
        for word in word_tokens:
            lemmatized.append(nltk.ISRIStemmer().suf32(word))
        
        return lemmatized

        

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
        return bag_of_words


class BagOfWordsEn():

    def getbagOfWords(example_sent):
        vect = CountVectorizer()
        bag_of_words = vect.transform(example_sent).toarray()

        return bag_of_words


#********************************************PS Tagging****************************************
class PosTagging():

    def getpos(example_sent):
        stop_words = set(stopwords.words('arabic'))
        tokens = sent_tokenize(example_sent)
        for i in tokens:

            word_list = nltk.word_tokenize(i)
            word_list = [word for word in word_list if not word in stop_words]
            pos = nltk.pos_tag(word_list)
        return pos

#********************************************TFIDF****************************************
class TFIDF():

    def gettf(example_sent):
        tokens = word_tokenize(example_sent)
        tfidf = TfidfVectorizer(tokenizer=tokens, stop_words=stopwords.words('english'))
        return tfidf




#******************************************_remove_numbers_**********************************


class Number():
    def num_to_text(self, text):
          out = ''
          for s in text.split():
              if s.isdigit():
                  out = out + num2words(int(s), lang='ar')+' '
              else:
                   out = out + s + ' '
          return out[:-1]


#******************************************_remove_diacritics_********************************


class Diacriticts():
    def __init__(self):
        self.arabic_diacritics = re.compile("""
                                ّ    | # Tashdid
                                َ    | # Fatha
                                ً    | # Tanwin Fath
                                ُ    | # Damma
                                ٌ    | # Tanwin Damm
                                ِ    | # Kasra
                                ٍ    | # Tanwin Kasr
                                ْ    | # Sukun
                                ـ     # Tatwil/Kashida
                            """, re.VERBOSE)

    def remove_diacritics(self, text):
        text = re.sub(self.arabic_diacritics, '', text)
        return text

#******************************************_remove_diacritics_********************************


class clean():
    def tfdif_doc(self, doc):
        vectorizer = TfidfVectorizer()
        return vectorizer.fit_transform(doc)
    
    #---------clean data---------
    def nlp_Operation(text, operations):
        if 'Stop_words' in operations:
            resultOp = StopWords.deleteStopWords(text)
            text = ' '.join(resultOp)

        if 'Stemming' in operations:
            resultOp = Stemming.defineStemming(text)
            text = ' '.join(resultOp)

        if 'Lemmatization' in operations:
            resultOp = Lemmatization.getLemmatization(text)
            text = ' '.join(resultOp)

        if 'BagOfWords' in operations:
            resultOp = BagOfWords.getbagOfWords(text)
            text = ' '.join(resultOp)
        return resultOp

class Naturalproc():
    def getNlp(content):
        # -----------------------------------------_FilteredData_-----------------------------------------
        content = StopWords.deleteStopWords(content)
        content = Punctuation.removePunctuations(' '.join(content))
        content = Stemming.defineStemming(content)
        return content
    


#if __name__ == '__main__':
#    Stemming.defineStemming(self=0)
