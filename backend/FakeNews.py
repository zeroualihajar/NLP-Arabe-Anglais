import pickle

import nltk
import numpy as np
import pandas as pd
import pymongo
from mongoengine import connect
from sklearn import metrics, preprocessing
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.metrics import plot_confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

from NLP import clean

#dataset = pd.read_csv('data/arabic-sentiment.csv')
#print(dataset['Sentiment'].value_counts())


#     # *********************** get data from database ******************** #
# def getDataFromDB():

#     try:

#         # --- Connection to Mongodb --- #
#         mongo = pymongo.MongoClient(
#             host="localhost",
#             port=27017,
#             serverSelectionTimeoutMS=1000,
#         )
#         db = mongo.DatabaseCollected

#         # --- Connection to our database --- #
#         connect('DatabaseCollected', host='mongodb://localhost', alias='default')

#         # --- Getting data from data collection (table) --- #
#         cursor = db['data'].find()

#         ids = []  # Array to store ids
#         title = ' '  # Variable to store temporary the title of each row
#         content = ' '  # Variable to store temporary the content of each row
#         scores = []  # Array to store the scores
#         classes = []  # Array to store classes
#         combined_title_content = []  # Array to store combined title and content of each row

#         # --- collect data --- #
#         for document in cursor:
#             ids.append(str(document['_id']))
#             title = document['title']
#             content = document['content']
#             combine = title + " " + content
#             combined_title_content.append(combine)
#             scores.append(document['score'])
#             classes.append(document['class_result'])

#         # --- Put collected information into a Json form (keys: ids, values: combined_title_content) --- #
#         content_by_id = {}
#         for i, eid in enumerate(ids):
#             content_by_id[eid] = combined_title_content[i]
#         print("content_by_id ", len(content_by_id)," score ",len(scores), "class_result", len(classes))
#         return {'content': content_by_id, 'score': scores, 'class_result': classes}

#     except Exception as ex:
#       print(ex)

# # --- Function to put our collected data into a pandas DataFrame --- #
# def putDataInDataFrame(string_text):
#     data_df = pd.DataFrame.from_dict(string_text).transpose()
#     data_df.columns = ['content']
#     data_df = data_df.sort_index()
#     return data_df

#     #****************Convert Column to DataFrame **********************#
# def convertToDf(column_title, df):
#     data = getDataFromDB()[column_title]
#     return df.from_dict(data).transpose()


# --- Training models class (KNN, DT, ANN, NB, SVM) --- #
class TrainingModel:
    # --------------------------- Get columns --------------------------#
    #dataFrame = pd.DataFrame.from_dict(getDataFromDB()['Feed']).transpose()
    #dataFrame.columns = ['Feed']
    #data_df = dataFrame.sort_index()
    # ct = getDataFromDB()
    # print(getDataFromDB())
    
    # d = {"content": getDataFromDB()['content']}
    # dataFrame = pd.DataFrame(data=d)
    # print("dataFrame ", len(dataFrame))
    # dataFrame['score'] = getDataFromDB()['score']
    # dataFrame['class_result'] = getDataFromDB()['class_result']

    # # ------------------ Clean dataframe using nlp class ----------------#
    # operation = ['Stop_words', 'Stemming']
    # dataFrame['content'] = dataFrame['content'].apply(lambda x: ' ' .join(clean.nlp_Operation(x, ['Stop_words', 'Stemming'])))
    # le = LabelEncoder()
    # y = dataFrame["class_result"].astype('int')
    # x = dataFrame.drop(columns= ["class_result"])

    # X_train,X_test,y_train,y_test = train_test_split(dataFrame["content"], y, test_size=0.2, random_state=42)

    # #-----------------------------DecisionTreeClassifier-------------------------#

    # pipe = Pipeline([('vect', CountVectorizer()),
    #                  ('tfidf', TfidfTransformer()),
    #                  ('model', DecisionTreeClassifier(criterion= 'entropy',
    #                                            max_depth = 20,
    #                                            splitter='best',
    #                                            random_state=42))])
    # # Fitting the model
    # model = pipe.fit(X_train, y_train)
    # # Accuracy
    # prediction = model.predict(X_test)
    # print("DecisionTreeClassifier accuracy: {}%".format(round(accuracy_score(y_test, prediction)*100,2)))
    # pickle.dump(model, open('data/Fake/DTC.pkl', 'wb'))

    # #----------------------------------------knn--------------------------------#
    # pipe = Pipeline([('vect', CountVectorizer()),
    #                  ('tfidf', TfidfTransformer()),
    #                  ('model', KNeighborsClassifier(n_neighbors=5) )])
    # # Fitting the model
    # model = pipe.fit(X_train, y_train)
    # # Accuracy
    # prediction = model.predict(X_test)
    # print("KNeighborsClassifier accuracy: {}%".format(round(accuracy_score(y_test, prediction)*100,2)))
    # pickle.dump(model, open('data/Fake/knn.pkl', 'wb'))

    # #----------------------------------------Ann----------------------------------#
    # Ann = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
    # pipe = Pipeline([('vect', CountVectorizer()),
    #                 ('tfidf', TfidfTransformer()),
    #                 ('model', SVC() )])
    # Ann=pipe.fit(X_train, y_train.ravel())
    # pickle.dump(Ann, open('data/Fake/Ann.pkl', 'wb'))
    # y_pred = Ann.predict(X_test)
    # print("Ann accuracy: {}%".format(round(accuracy_score(y_test, prediction)*100,2)))
    # conf_matrix = plot_confusion_matrix(Ann, X_test, y_test,
    #                                 cmap=plt.cm.Blues)
    # plt.show()

    # #----------------------------------------svm-----------------------------------#
    # from sklearn.svm import SVC
    # pipe = Pipeline([('vect', CountVectorizer()),
    #                 ('tfidf', TfidfTransformer()),
    #                 ('model', SVC() )])
    # # Fitting the model
    # model = pipe.fit(X_train, y_train)
    # # Accuracy
    # prediction = model.predict(X_test)
    # print("SVM accuracy: {}%".format(round(accuracy_score(y_test, prediction)*100,2)))
    # pickle.dump(model, open('data/Fake/svm.pkl', 'wb'))

    # #----------------------------------------nb------------------------------------#
    # #pipe = Pipeline([('vect', CountVectorizer()),
    # #                 ('tfidf', TfidfTransformer()),
    # #                 ('model', GaussianNB())])
    # ## Fitting the model
    # #model = pipe.fit(X_train, y_train)
    # ## Accuracy
    # #prediction = model.predict(X_test)
    # #print("nb accuracy: {}%".format(round(accuracy_score(y_test, prediction) * 100, 2)))
    # #pickle.dump(model, open('data/nb.pkl', 'wb'))

    #===================== check if text is positive or negative ==================#
    def getResult(pathModel, text):
        loaded_model = pickle.load(open(pathModel, 'rb'))
        operation = ['Stop_words', 'Stemming']
        text = ' '.join(clean.nlp_Operation(text, operation))
        prediction = loaded_model.predict([text])
        print(prediction)
        return prediction


# TrainingModel.getResult(
    # 'data/Fake/knn.pkl', 'مسحة طبية أجريت للاعبي البطولة  للكشف عن كورونا')
