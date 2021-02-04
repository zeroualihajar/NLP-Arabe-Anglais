from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import qalsadi.lemmatizer
from nltk.stem.isri import ISRIStemmer
from tashaphyne.stemming import ArabicLightStemmer
from flask import Flask
from flask_restful import Resource, Api, reqparse

# app = Flask(__name__)
# api = Api(app)


parser = reqparse.RequestParser()


class Tokenization(Resource):

    def get(self, text):
        tokens = nltk.word_tokenize(text)
        return {"After Tokenization": tokens}


class StopWords(Resource):

    def get(self, text):
        sw = stopwords.words('arabic')
        tokens = nltk.word_tokenize(text)
        stopped_tokens = [i for i in tokens if not i in sw]

        return {"Stop Words": stopped_tokens}


class Lemmatization(Resource):

    def get(self, text):
        lemmer = qalsadi.lemmatizer.Lemmatizer()
        lem = lemmer.lemmatize_text(text)
        return {"Lemmatization": lem}


class Stemming(Resource):

    def get(self, text):
        ArListem = ArabicLightStemmer()
        list_Stemming = []

        tokens = nltk.word_tokenize(text)
        for word in tokens:
            stem = ArListem.light_stem(word)
            list_Stemming.append(ArListem.get_stem())
        return {"Stemming": list_Stemming}


class Pos(Resource):

    def get(self, text):
        PosTokens = []
        tokens = nltk.word_tokenize(text)
        for word in tokens:
            after = nltk.pos_tag(tokens)
            PosTokens.append(after)
        return {"POS  ": PosTokens}


# api.add_resource(Tokenization, "/tokenization/<string:text>")
# api.add_resource(StopWords, "/stopWords/<string:text>")
# api.add_resource(Lemmatization, "/lemmatization/<string:text>")
# api.add_resource(Stemming, "/stemming/<string:text>")
# api.add_resource(Pos, "/posTag/<string:text>")


# if __name__ == '__main__':
#     app.run(debug=True)
