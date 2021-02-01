import requests
from bs4 import BeautifulSoup
from flask import Flask, Response, request
import pymongo
import json
import csv


class scrapping():

    #**********************************_collecte data from moroccan press_***************************
    def getDataFromURL(url):
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        return soup

    #*****************************************_save data in csv file_********************************
    def fileSave(fileName, url, className):
        csv_file = open(fileName+'.csv', 'w', encoding="utf-8")
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['titre', 'content_link'])
        soup = scrapping.getDataFromURL(url)
        content_link = []
        for article in soup.find_all('div', class_=className):

            titre = article.h1.text

            try:
                for art in article.findAll('p'):
                    content_link += ' ' + art.text

            except Exception as e:
                content_link = None

            csv_writer.writerow([titre, content_link])

        csv_file.close()

    # *******************************************_save data in MongoDB_*********************************

    def dbSave(url, className):
        try:
          mongo = pymongo.MongoClient(
              host="localhost",
              port=27017,
              serverSelectionTimeoutMS=1000,
          )
          db = mongo.DatabaseCollected
          soup = scrapping.getDataFromURL(url)

          #----------------------get data from div-------------------
          content_link = ''
          for article in soup.find_all('div', class_=className):

              titre = article.h1.text

              try:

                  for art in article.findAll('p'):
                      content_link += ' '+art.text

              except Exception as e:
                  content_link = None

              #--------------------save data in table------------------
              mydata = {"url": url, "title": titre,
                        "content_link": content_link}
              dbResponse = db.mydata.insert_one(mydata)
              print(dbResponse.inserted_id)

          return Response(
              response=json.dumps(
                  {"message": "data saved", "id": f"{dbResponse.inserted_id}"}),
              status=200,
              mimetype="application/json"
          )
        except Exception as ex:
          print(ex)


if(__name__ == '__main__'):
    scrapping.dbSave(url='https://ar.hibapress.com/details-281066.html',
                     className='main-content tie-col-md-8 tie-col-xs-12')
