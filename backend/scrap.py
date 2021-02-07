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

    # def dbSave(url, className, class):
    #     try:
    #       mongo = pymongo.MongoClient(
    #           host="localhost",
    #           port=27017,
    #           serverSelectionTimeoutMS=1000,
    #       )
    #       db = mongo.DatabaseCollected
    #       soup = scrapping.getDataFromURL(url)

    #       #----------------------get data from div-------------------
    #       content_link = ''
    #       test = soup.find('title')
    #       titre = test.text
    #       for article in soup.find_all('div', class_=className):

    #           #titre = article.h1.text
    #           try:

    #               for art in article.find_all('p'):
    #                   content_link += ' '+art.text

    #           except Exception as e:
    #               content_link = None

    #           #--------------------save data in table------------------
    #           mydata = {"url": url, "title": titre,"content": content_link, "language": "arabic", "class": class}
    #           dbResponse = db.data.insert_one(mydata)
    #           print(dbResponse.inserted_id)

    #           return Response(
    #           response=json.dumps(
    #               {"message": "data saved", "id": f"{dbResponse.inserted_id}"}),
    #           status=200,
    #           mimetype="application/json"
    #       )
    #     except Exception as ex:
    #       print(ex)



    def dbSaveFake(title, text):
        try:
          mongo = pymongo.MongoClient(
              host="localhost",
              port=27017,
              serverSelectionTimeoutMS=1000,
          )
          db = mongo.DatabaseCollected
          
        #--------------------save data in table------------------
          mydata = {"url": "", "title": title,"content": text, "language": "arabic", "class": '0'}
          dbResponse = db.data.insert_one(mydata)
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

    #----------------------------hibapress-----------------------------
    # scrapping.dbSave(url='https://ar.hibapress.com/details-282841.html',
    #                  className='entry-content entry clearfix', class='1')
    
    # scrapping.dbSave(url='https://ar.hibapress.com/details-282894.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282882.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282797.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282791.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282782.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282762.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282756.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282750.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282698.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282690.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282662.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282640.html',
    #                  className='entry-content entry clearfix', class='1')
    
    # scrapping.dbSave(url='https://ar.hibapress.com/details-282588.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282573.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282527.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282506.html',
    #                  className='entry-content entry clearfix', class='1')


    # scrapping.dbSave(url='https://ar.hibapress.com/details-282494.html',
    #                  className='entry-content entry clearfix', class='1')


    # scrapping.dbSave(url='https://ar.hibapress.com/details-282385.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282373.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-281963.html',
    #                  className='entry-content entry clearfix', class='1')

    # scrapping.dbSave(url='https://ar.hibapress.com/details-282506.html',
    #                  className='entry-content entry clearfix', class='1')





    #----------------------------منظمة الصحة العالمية-----------------------------
    # scrapping.dbSave(url='https://www.who.int/ar/emergencies/diseases/novel-coronavirus-2019/advice-for-public/q-a-coronaviruses',
    #                 className='rtl post-template-default single single-post postid-282841 single-format-standard tie-js boxed-layout wrapper-has-shadow block-head-3 magazine1 is-mobile is-header-layout-2 has-header-below-ad sidebar-left has-sidebar post-layout-2 narrow-title-narrow-media is-standard-format has-mobile-share hide_banner_header hide_banner_top hide_banner_bottom hide_sidebars hide_footer hide_breadcrumbs hide_read_more_buttons hide_share_post_top hide_share_post_bottom hide_post_newsletter hide_post_authorbio hide_back_top_button', class='1')
    


    #--------------------- Fake news -------------------------------
    #-------------------- url : https://www.alhurra.com/health/2021/02/06/%D8%AF%D8%B1%D8%A7%D8%B3%D8%A9-%D8%A7%D9%84%D8%A3%D8%B7%D9%81%D8%A7%D9%84-%D8%A7%D9%84%D8%B0%D9%8A%D9%86-%D8%AA%D9%84%D9%82%D9%88%D8%A7-%D9%84%D9%82%D8%A7%D8%AD-%D8%A7%D9%84%D8%A5%D9%86%D9%81%D9%84%D9%88%D9%86%D8%B2%D8%A7-%D8%A3%D9%82%D9%84-%D8%B9%D8%B1%D8%B6%D8%A9-%D9%84%D9%84%D8%A5%D8%B5%D8%A7%D8%A8%D8%A9-%D8%A8%D8%A3%D8%B9%D8%B1%D8%A7%D8%B6-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-%D8%A7%D9%84%D8%B4%D8%AF%D9%8A%D8%AF%D8%A9

    # scrapping.dbSaveFake(
    #    "كورونا والشباب", "منذ بداية 2020، كثر الحديث عن أن كبار السن هم الأكثر عرضة لمضاعفات شديدة من الفيروس، وأن الشباب محصنون ضده.")

    # scrapping.dbSaveFake(
        # " الأقنعة لا تحمي", "لعل هذا هو أكثر الاعتقادات الخاطئة إثارة للجدل والتسييس على الإطلاق. ففي وقت مبكر من الوباء، قيل لنا إن الأقنعة ليست مهمة بالنسبة لمن هم ليسوا على اتصال وثيق بالمرضى.")

    # scrapping.dbSaveFake("الإصابة تكون فقط عبر اتصال وثيق بشخص مصاب",
                        #  "من بين 61 عضوا  في أحد الفرق الموسيقية في كنيسة بواشنطن، كان هناك شخص  واحد فقط يعاني من أعراض الفيروس، وبعد 2.5 ساعة من التدريب في يومين منفصلين، أصيب 87% من المجموعة بالمرض")
    
    # scrapping.dbSaveFake("الفيروس مثل الإنفلونزا", "الفيروس يشبة الإنفلوانزا")
    # scrapping.dbSaveFake("الجميع سيحصل على لقاح هذا الشتاء", "مع بعض التوقعات المتفائلة التي تقول إن اللقاح سيكون متوفرا في شهر أكتوبر، غير أن الخبراء يقولون إنه حتى لو كان ذلك صحيحا، وحصل لقاح على إذن استخدام طارئ أو موافقة صريحة في خريف هذا العام، فلا توجد طريقة مادية لتوفر جرعات كافية على الفور للجميع.")


    #------------------- url : https://www.dw.com/ar/%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA-%D8%AE%D8%A7%D8%B7%D8%A6%D8%A9-%D8%B9%D9%86-%D9%81%D9%8A%D8%B1%D9%88%D8%B3-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-%D9%82%D8%AF-%D8%AA%D9%83%D9%84%D9%91%D9%81-%D8%A7%D9%84%D9%86%D8%A7%D8%B3-%D8%AD%D9%8A%D8%A7%D8%AA%D9%87%D9%85/a-52945428
    # scrapping.dbSaveFake("خوف من البضائع الصينية", "وأوضح تجار تجزئة في نيودلهي لوكالة فرانس برس إنهم خزنوا سلعاً صينية مثل المسدسات البلاستيك والشعر المستعار من بين أمور أخرى تم استيرادها من أجل مهرجان "هولي" في وقت سابق من هذا الشهر.

                        #  وقال فيبين نيجهاوان من "جمعية الألعاب الهندية": "المعلومات الخاطئة عن المنتجات الصينية التي تزعم أن هذه السلع قد تنقل فيروس كورونا، تسببت في انخفاض مبيعات المنتجات المخصصة للمهرجان. لقد شهدنا انخفاضاً في المبيعات بحوالي 40 % مقارنة بالعام السابق".")

    scrapping.dbSaveFake("", "")

    scrapping.dbSaveFake("", "")

    scrapping.dbSaveFake("", "")

    scrapping.dbSaveFake("", "")

    scrapping.dbSaveFake("", "")

    scrapping.dbSaveFake("", "")



