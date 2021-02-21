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

    def dbSave(url, className, score):
        try:
            mongo = pymongo.MongoClient(host="localhost", port=27017, serverSelectionTimeoutMS=1000,)
            db = mongo.DatabaseCollected
            soup = scrapping.getDataFromURL(url)

            
            #----------------------get data from div-------------------
            content_link = ''
            test = soup.find('title')
            titre = test.text
            for article in soup.find_all('div', class_=className):
                # titre = article.h1.text
                try:
                    for art in article.find_all('p'):
                        content_link += ' '+art.text

                except Exception as e:
                    content_link = None

            #--------------------save data in table------------------
            mydata = {"url": url, "title": titre, "content": content_link, "score": score, "class_result": 1}

            dbResponse = db.data.insert_one(mydata)
            print(dbResponse.inserted_id)

            return Response(
            response=json.dumps({"message": "data saved", "id": f"{dbResponse.inserted_id}"}), status=200, mimetype="application/json")
        except Exception as ex:
            print(ex)



    def dbSaveFake(url, title, text, score):
        try:
          mongo = pymongo.MongoClient(
              host="localhost",
              port=27017,
              serverSelectionTimeoutMS=1000,
          )
          db = mongo.DatabaseCollected
          
        #--------------------save data in table------------------
          mydata = {"url": url, "title": title,"content": text, "score": score, "class_result": 0}
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
    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282841.html',
    #                  className='entry-content entry clearfix', score=2)
    #  scrapping.dbSaveFake(url='https://www.bbc.com/arabic/vert-fut-55701643',title="جرعة واحدة تعطي المناعة المطلوبة للوقاية",text="جرعة واحدة تعطي المناعة المطلوبة للوقاية", score=4)
    #  scrapping.dbSaveFake(url='fakeNews', title="زجاجة منظف خزان الأسماك تحتوي على دواء وقائي ضد كورونا",
    #                  text="زجاجة منظف خزان الأسماك تحتوي على دواء وقائي ضد كورونا", score=1)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282894.html',
    #                  className='entry-content entry clearfix', score=2)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282882.html',
    #                  className='entry-content entry clearfix', score=2)
    #  scrapping.dbSaveFake(url='fakeNews', title="اللقاحات المضادة للالتهاب الرئوي تحمي من فيروس كورونا", text="اللقاحات المضادة للالتهاب الرئوي تحمي من فيروس كورونا", score=1)
    #  scrapping.dbSaveFake(url='fakeNews', title=" الأطفال شبه محصنين من COVID-19", text=" الأطفال شبه محصنين من COVID-19", score=1)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282797.html',
    #                      className='entry-content entry clearfix', score=2)


    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282791.html',
    #                   className='entry-content entry clearfix', score=2)
    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282782.html',
    #                   className='entry-content entry clearfix', score=2)
    #  scrapping.dbSaveFake(url='fakeNews', title="عقار هيدروكسى كلوروكين المضاد للملاريا كان علاجًا لـ COVID-19",
    #                  text="عقار هيدروكسى كلوروكين المضاد للملاريا كان علاجً لـ COVID-19", score=1)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282762.html',
    #                   className='entry-content entry clearfix', score=2)
    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282756.html',
    #                   className='entry-content entry clearfix', score=2)
    #  scrapping.dbSaveFake(url='fakeNews', title="تناول الثوم يحمي من كورونا",
    #                  text="الثوم يقي من عدوى كورونا المستجد.", score=1)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282750.html',
    #                   className='entry-content entry clearfix', score=2)
    #  scrapping.dbSaveFake(url='fakeNews', title="كل مرض يأتى من الصين", text="كل مرض يأتى من الصين", score=1)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282698.html',
    #                   className='entry-content entry clearfix', score=3)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282690.html',
    #                   className='entry-content entry clearfix', score=3)
    #  scrapping.dbSaveFake(url='fakeNews', title="لا يمكن أخذ لقاحي الإنفلونزا وكورونا في العام ذاته", text="لا يمكن أخذ لقاحي الإنفلونزا وكورونا في العام ذاته ", score=1)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282662.html',
    #                   className='entry-content entry clearfix', score=3)
    #  scrapping.dbSaveFake(url='fakeNews', title="يحتوي روبوتات تسجل المعلومات",
    #                  text="اللقاحات المطورة ضد كورونا، تحوي جسيمات نانوية هي روبوتات أو أجهزة كمبيوتر صغيرة يمكن أن تسجل بيانات الإنسان الحيوية.", score=1)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282640.html',
    #                   className='entry-content entry clearfix', score=3)
    #  scrapping.dbSaveFake(url='fakeNews', title="فيروس كورونا غير موجود",
    #                  text="فيروس كورونا غير موجود، وأن طائرة بدون طيار أسقطت الأحد، فيما كانت تنشر مسحوقا أبيض يتسبب بجفاف الرئتين.", score=1)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282588.html',
    #                   className='entry-content entry clearfix', score=3)
    #  scrapping.dbSaveFake(url='fakeNews', title="شرب الكلور قد يقتل الفيروس", text="شرب الكلور قد يقتل الفيروس", score=1)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282573.html',
    #                   className='entry-content entry clearfix', score=3)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282527.html',
    #                   className='entry-content entry clearfix', score=3)
    #  scrapping.dbSaveFake(url='fakeNews', title="شبكات الجيل الخامس للمحمول تنقل الفيروس",
    #                  text="يمكن للفيروسات الانتقال عبر موجات الراديو /شبكات الجوال", score=1)
    #  scrapping.dbSaveFake(url='fakeNews', title="البنصر الطويل هو درع ضد كورونا", text="البنصر الطويل هو درع ضد كورونا",score=1)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282506.html',
    #                   className='entry-content entry clearfix', score=3)
    #  scrapping.dbSaveFake(url='fakeNews', title="يسبب العقم لدى النساء",
    #                  text="مدير الأبحاث في فايزر.. اللقاح يسبب العقم عند النساء حسبما جاء على لسان رئيس شركة فايزر السابق لأبحاث الجهاز التنفسي الطبيب مايكل ييدون", score=1)

    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282494.html',
    #                   className='entry-content entry clearfix', score=3)
    #  scrapping.dbSave(url='https://ar.hibapress.com/details-282385.html',
    #                   className='entry-content entry clearfix', score=3)
    #  scrapping.dbSaveFake(url='fakeNews', title="شرب الكحول عالي التركيز يمكن أن يطهر الجسم ويقتل الفيروس",
    #                  text="شرب الكحول عالي التركيز يمكن أن يطهر الجسم ويقتل الفيروس", score=1)

     scrapping.dbSaveFake(url='fakeNews', title="حبس أنفاسك لمدة 10 ثوانٍ أو أكثر دون السعال أو الشعور بعدم الراحة تدل على عدم إصابتك بكورونا", text="حبس أنفاسك لمدة 10 ثوانٍ أو أكثر دون السعال أو الشعور بعدم الراحة تدل على عدم إصابتك بكورونا", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-282373.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="البعوض ينقل العدوى",
                         text="روج البعض أن عدوى كورونا تتم من خلال لدغات البعوض",score=1)
     scrapping.dbSaveFake(url='fakeNews', title= "حتاج الشخص الذي تلقى اللقاح للعزل",
                     text="حتاج الشخص الذي تلقى اللقاح للعزل",score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281963.html',
                          className='entry-content entry clearfix', score=3)

     scrapping.dbSave(url='https://ar.hibapress.com/details-282506.html',
                      className='entry-content entry clearfix', score=3)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281611.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="يغير اللقاح الجين الوراثي للشخص",
                     text="يغير أو يتفاعل اللقاح مع الجين الوراثي", score=1)

     scrapping.dbSaveFake(url='fakeNews', title=" تقنية الهاتف المحمول 5G هي المسؤولة بطريقة أو بأخرى عن الفيروس",
                     text=" تقنية الهاتف المحمول 5G هي المسؤولة بطريقة أو بأخرى عن الفيروس", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281564.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="الفيروس التاجى تم إنشاؤه فى المختبر", text="الفيروس التاجى تم إنشاؤه فى المختبر",score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281554.html',
                      className='entry-content entry clearfix', score=3)


     scrapping.dbSave(url='https://ar.hibapress.com/details-281540.html',
                      className='entry-content entry clearfix', score=3)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281509.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="يغير الحمض النووي للإنسان",
                     text="اللقاحات التي تعتمد على الحمض النووي الريبي RNA، مثل التي طورها تحالف بيونتك-فايزر وموديرنا، ستحدث تغييرا جذريا في الحمض النووي للإنسان DNA", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281490.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="تغيير الحمض النووي لمتلقّي اللقاح",
                         text="ولعلّ من أكثر الشائعات عن اللقاحات المضادّة لفيروس كورونا المستجدّ أنها تحتوي على مواد جينيّة تؤدّي إلى تغيير الحمض النووي للإنسان.",score=1)
     scrapping.dbSaveFake(url='fakeNews', title="إمكانية شرب الكحول المطهر للجلد لعلاج فيروس كورونا",
                     text="إمكانية شرب الكحول المطهر للجلد لعلاج فيروس كورونا", score=1)
     scrapping.dbSaveFake(url='fakeNews', title="ابتلاع المطهرات لمحاربة كورونا بعد تصريحات ترامب",
                     text="تكهن الرئيس ترامب بعدد من العلاجات الأخرى بجانب هيدروكسي كلوروكوين، ففي أواخر أبريل، رأى أن الأشعة فوق البنفسجية يمكن أن تحييد الفيروس وكذلك اقترح حقن المواد المطهرة كعلاج لفيروس كورونا،", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281487.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281484.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="تناول الميثانول كعلاج لفيروس كورون", text="تناول الميثانول كعلاج لفيروس كورون",score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281450.html',
                          className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="كورونا ينتقل من خلال لدغات البعوض",
                     text="هناك معلومات أو أدلة تشير إلى أن الفيروس التاجي الجديد يمكن أن ينتقل عن طريق البعوض.",score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281420.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title=
    "الأطباء الإيطاليين عصوا قانون منظمة الصحة العالمية بمنع تشريح جثث موتى كورونا، حيث اكتشفوا أنه ليس فيروسًا ولكن ما يسببه بكتيريا تسبب الوفاة وتكوين جلطات الدم، وأن طريقة العلاج هي المضادات الحيوية ومضادات التخثر مثل: الأسبرين وأن علاجه لا يحتاج لأجهزة تنفس صناعي أو عناية مركزة.",
    text="فيروس كورونا ليس سوى تخثر منتشر داخل الأوعية الدموية", score=1)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281416.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title=" الأقنعة تؤدى إلى إصابة الأشخاص بالمرض", text=" الأقنعة تؤدى إلى إصابة الأشخاص بالمرض", score=1)
     scrapping.dbSaveFake(url='fakeNews', title= "إيطاليا استطاعت هزيمة فيروس كورونا أو كوفيد 19",text='إيطاليا استطاعت هزيمة فيروس كورونا أو كوفيد 19' ,score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281389.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="بيض الدواجن ملوث بفيروس كورونا", text="بيض الدواجن ملوث بفيروس كورونا", score=1)

     scrapping.dbSaveFake(url='fakeNews', title="يحتوي خلايا أجنة مجهضة", text="",score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281387.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281348.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="عقم وخلايا أجنّة مجهضة",
                         text=" لقاح أسترازينيكا/أوكسفورد يحتوي على خلايا أم آر سي-5، وهي خلايا من أجنّة بشريّة.", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281353.html',
                          className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="الفيروس التاجي غير موجود", text="الفيروس التاجي غير موجود", score=1)
     scrapping.dbSaveFake(url='fakeNews', title="كورونا سلاح بيولوجي تموله مؤسسة بيل وميليندا جيتس لزيادة مبيعات اللقاحات",
                     text="كورونا سلاح بيولوجي تموله مؤسسة بيل وميليندا جيتس لزيادة مبيعات اللقاحات", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281335.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281288.html',
                      className='entry-content entry clearfix', score=3)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281312.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281344.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="تناول الثوم يمنع الإصابة بكورونا",
                         text="تناول الثوم يمنع الإصابة بكورونا", score=1)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281251.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281258.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="يغير اللقاح الجين الوراثي للشخص",
                     text="يغير أو يتفاعل اللقاح مع الجين الوراثي",score=0)
     scrapping.dbSaveFake(url='fakeNews', title="التباعد الاجتماعي غير فعال", text="التباعد الاجتماعي غير فعال", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281280.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281238.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="من سبق له الإصابة بـكوفيد-19 لا يأخذ اللقاح",
                     text="من سبق له الإصابة بـكوفيد-19 لا يأخذ اللقاح", score=0)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281249.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='https://alghad.com/%D9%87%D9%84-%D9%8A%D9%86%D8%AA%D9%82%D9%84-%D9%81%D9%8A%D8%B1%D9%88%D8%B3-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-%D9%85%D9%86-%D8%AE%D9%84%D8%A7%D9%84-%D8%A7%D9%84%D8%AD%D8%B0%D8%A7%D8%A1%D8%9F/',title="يمكن أن ينتشر فيروس كوفيد-19 بواسطة الأحذية",
                      text="يمكن أن ينتشر فيروس كوفيد-19 بواسطة الأحذية" ,score=0)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281248.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='https://arabicpost.me/%d8%aa%d8%ad%d9%84%d9%8a%d9%84%d8%a7%d8%aa/2020/03/09/%d9%86%d8%b5%d8%a7%d8%a6%d8%ad-%d8%aa%d8%a8%d8%af%d9%88-%d8%b7%d8%a8%d9%8a%d8%a9-%d8%aa%d8%ae%d8%a8%d8%b1%d9%83-%d8%a3%d9%86%d9%87%d8%a7-%d8%a7%d9%84%d8%ad%d9%84-%d8%a7%d9%84%d9%85%d8%b9%d8%ac%d8%b2/',title="الثوم",text="انتشرت رسائل كثيرة عبر موقع فيسبوك توصي بتناول الثوم لمنع الإصابة بفيروس كورونا." , score=5)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281229.html',
                          className='entry-content entry clearfix', score=3)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281233.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='https://old.sfda.gov.sa/ar/mobile/Pages/viewarticle.aspx?url=/ar/drug/awareness/news/Pages/about_antibiotics.aspx',title="المضادات الحيوية تقضي على الفيروس",
                          text="يجب استخدام المضادات الحيوية في مقاومة الفيروس؛", score=1)
     scrapping.dbSaveFake(url='https://honna.elwatannews.com/news/details/2090734/13-%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A9-%D9%85%D9%87%D9%85%D8%A9-%D8%B9%D9%86-%D9%81%D9%8A%D8%B1%D9%88%D8%B3-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-%D9%8A%D9%86%D8%AA%D9%82%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D9%85%D9%86%D8%A7%D8%B7%D9%82-%D8%B0%D8%A7%D8%AA-%D8%A7%D9%84%D9%85%D9%86%D8%A7%D8%AE-%D8%A7%D9%84%D8%AD%D8%A7%D8%B1-%D9%88%D8%A7%D9%84%D8%B1%D8%B7%D8%A8',title=" لا يمكن أن ينتقل الفيروس في المناطق ذات المناخ الحار والرطب",
    text=" لا يمكن أن ينتقل الفيروس في المناطق ذات المناخ الحار والرطب", score=0)
     scrapping.dbSaveFake(url='fakeNews',title="رش الكحول أو الكلور في جميع أنحاء الجسم يقتل كورونا",text="ن رش الكحول أو الكلور في جميع أنحاء الجسم يقتل الفيروسات التي دخلت جسمك", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281236.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',
    title="لا يحتاج الشخص الذي سبق وأصيب بكورونا إلى اللقاح", text="لا يحتاج الشخص الذي سبق وأصيب بكورونا إلى اللقاح", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281196.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews', title="فضة صالحة للشرب" ,
                         text="يشجع البعض على استخدام ما يعرف بـالفضة الغروية، وهي جزيئات صغيرة من الفضة في سائل، لمواجهة فيروس كورونا." , score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281206.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281205.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',title="شرب المياه كل 15 دقيقة",
                         text="نقلت إحدى المنشورات على فيسبوك نصيحة من طبيب ياباني يوصي بشرب المياه كل 15 دقيقة لطرد أي فيروس قد يدخل الفم.",score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281160.html',
                          className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',title="شرب المياه كل 15 دقيقة", text="كورونا لا يصيب الشباب", score=1)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281163.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281181.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url="https://www.alarabiya.net/medicine-and-health/2020/12/11/%D8%A3%D9%82%D9%86%D8%B9%D8%A9-%D8%A7%D9%84%D9%88%D8%AC%D9%87-%D8%A7%D9%84%D8%A8%D9%84%D8%A7%D8%B3%D8%AA%D9%8A%D9%83%D9%8A%D8%A9-%D9%84%D8%A7-%D8%AA%D8%AD%D9%85%D9%8A-%D9%85%D9%86-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-"
        ,title=" الأقنعة لا تحمي",text="لعل هذا هو أكثر الاعتقادات الخاطئة إثارة للجدل والتسييس على الإطلاق. ففي وقت مبكر من الوباء، قيل لنا إن الأقنعة ليست مهمة بالنسبة لمن هم ليسوا على اتصال وثيق بالمرضى.",score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281010.html',
                          className='entry-content entry clearfix', score=3)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281027.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',title="مؤامرة معقّدة",
                         text="ظهرت على مواقع التواصل الاجتماعي باللغات الهولندية والألمانية والفرنسية والسلوفاكية والإسبانية، إضافة إلى العربية، قصّة معقّدة عن علاقة خفيّة بين مختبر ووهان في الصين، الذي تتهمه شائعات بـتصنيع الفيروس، وشركات إنتاج اللقاح وشركات التأمين وبعض أثرياء العالم، بما يوحي بوجود مؤامرة متشعّبة الأطراف تمتدّ خيوطها في أرجاء القارات الخمس.", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281030.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',title="الحرارة وتجنب الآيس كريم",
                         text="هناك الكثير من النصائح التي تشير إلى أنّ الحرارة المرتفعة تقتل الفيروس - ولهذا يوجد توصيات بشرب الماء الساخن والاستحمام بمياه ساخنة أو باستخدام مجفف الشعر. وتدّعي إحدى المنشورات التي تداولها العشرات من مستخدمي وسائل التواصل الإجتماعي في بلدان مختلفة - ونُسبت زورا إلى منظمة يونيسيف، أنّ شرب الماء الساخن والتعرض لأشعة الشمس سيقتل الفيروس - ويقول المنشور إنه يجب تجنب أكل الآيس كريم.", score=1)
     scrapping.dbSaveFake(url='fakeNews',title="البرد والثلج يقتلان الفيروس",
                         text=" البرد يقتل فيروس كورونا المستجد أو غيره من الفيروسات الأخرى.", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281072.html',
                              className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',
        title="كورونا والشباب",
        text="منذ بداية 2020، كثر الحديث عن أن كبار السن هم الأكثر عرضة لمضاعفات شديدة من الفيروس، وأن الشباب محصنون ضده.",score=1)
     scrapping.dbSaveFake(url='fakeNews',title="لا يمكن التعافي من كورونا وستصاب به مدى الحياة",
                         text="لا يمكن التعافي من كورونا وستصاب به مدى الحياة", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281117.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',title="الجميع سيحصل على لقاح هذا الشتاء",
                         text="مع بعض التوقعات المتفائلة التي تقول إن اللقاح سيكون متوفرا في شهر أكتوبر، غير أن الخبراء يقولون إنه حتى لو كان ذلك صحيحا، وحصل لقاح على إذن استخدام طارئ أو موافقة صريحة في خريف هذا العام، فلا توجد طريقة مادية لتوفر جرعات كافية على الفور للجميع." ,score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281129.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',title="نقل العدوى عن طريق الطرود",
                         text="يعرض استلام الطرود إلى العدوى وانتقال الفيروس", score=0)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281133.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',title="شرب المياه كل 15 دقيقة",
                         text="نقلت إحدى المنشورات على فيسبوك نصيحة من طبيب ياباني يوصي بشرب المياه كل 15 دقيقة لطرد أي فيروس قد يدخل الفم.", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281141.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',title="الفيروس مثل الإنفلونزا", text="الفيروس يشبة الإنفلوانزا", score=1)
     scrapping.dbSave(url='https://ar.hibapress.com/details-281151.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',
            title="الاستحمام بالماء الساخن يمنع الإصابة بفيروس كورونا الجديد", text=" يمنعك الاستحمام بالماء الساخن من التقاط عدوى كورونا",score=1)

       #----------------------- lakom ------------------------------------
     scrapping.dbSave(url='https://lakome2.com/covid19/218403/',
                      className='entry-content entry clearfix', score=4)
     scrapping.dbSaveFake(url='fakeNews',title="الإصابة تكون فقط عبر اتصال وثيق بشخص مصاب",
                         text="من بين 61 عضوا  في أحد الفرق الموسيقية في كنيسة بواشنطن، كان هناك شخص  واحد فقط يعاني من أعراض الفيروس، وبعد 2.5 ساعة من التدريب في يومين منفصلين، أصيب 87% من المجموعة بالمرض" , score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281151.html',
                          className='col-lg-8 no-p-r', score=3)
     scrapping.dbSaveFake(url='fakeNews',title="فيروس كورونا ليس سوى تخثر منتشر داخل الأوعية الدموية",
                         text="فيروس كورونا ليس سوى تخثر منتشر داخل الأوعية الدموية", score=0)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281151.html',
                      className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',title="معقم اليدين المصنوع منزلياً",
                         text="في إيطاليا، التي تعد حاليا أحد النقاط الساخنة للفيروس، أدت المخاوف من تفشي المرض إلى اختفاء معقمات اليدين من المتاجر. وبعد انتشار تقارير عن نقص كميات معقم اليدين في المتاجر، انتشرت وصفات لصنع المعقم في المنزل على وسائل التواصل الاجتماعي.",score=1)

     scrapping.dbSaveFake(url='fakeNews',title="الجميع سيحصل على لقاح هذا الشتاء",
                             text="مع بعض التوقعات المتفائلة التي تقول إن اللقاح سيكون متوفرا في شهر أكتوبر، غير أن الخبراء يقولون إنه حتى لو كان ذلك صحيحا، وحصل لقاح على إذن استخدام طارئ أو موافقة صريحة في خريف هذا العام، فلا توجد طريقة مادية لتوفر جرعات كافية على الفور للجميع.", score=1)

     scrapping.dbSave(url='https://ar.hibapress.com/details-281151.html',
                          className='entry-content entry clearfix', score=3)
     scrapping.dbSaveFake(url='fakeNews',title="الحل المعجزة",
                     text="يزعم نجم موقع يوتيوب جوردان ساثر، الذي لديه آلاف المتابعين عبر منصات مختلفة على مواقع التواصل الاجتماعي، أنّ ثاني أكسيد الكلور وهو عامل تبييض يستخدم في مواد التنظيف وتبييض الأقمشة والبقع، يساعد على التخلص من فيروس كورونا.", score=1)



#----------------------------منظمة الصحة العالمية-----------------------------
     scrapping.dbSave(url='https://www.who.int/ar/emergencies/diseases/novel-coronavirus-2019/advice-for-public/q-a-coronaviruses',
                     className='rtl post-template-default single single-post postid-282841 single-format-standard tie-js boxed-layout wrapper-has-shadow block-head-3 magazine1 is-mobile is-header-layout-2 has-header-below-ad sidebar-left has-sidebar post-layout-2 narrow-title-narrow-media is-standard-format has-mobile-share hide_banner_header hide_banner_top hide_banner_bottom hide_sidebars hide_footer hide_breadcrumbs hide_read_more_buttons hide_share_post_top hide_share_post_bottom hide_post_newsletter hide_post_authorbio hide_back_top_button', score=5)
    
     scrapping.dbSave(url='https://www.unicef.org/ar/%D9%85%D8%A7-%D9%8A%D9%84%D8%B2%D9%85%D9%83-%D9%85%D8%B9%D8%B1%D9%81%D8%AA%D9%87-%D8%A8%D8%B4%D8%A3%D9%86-%D9%84%D9%82%D8%A7%D8%AD%D8%A7%D8%AA-%D9%83%D9%88%D9%81%D9%8A%D8%AF-19/%D9%81%D9%8A%D8%B1%D9%88%D8%B3-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7',
                          className='field paragraph field_component_text_content  odd-t text_long', score=5)

    #--------------------- Fake news -------------------------------
    #-------------------- url : https://www.alhurra.com/health/2021/02/06/%D8%AF%D8%B1%D8%A7%D8%B3%D8%A9-%D8%A7%D9%84%D8%A3%D8%B7%D9%81%D8%A7%D9%84-%D8%A7%D9%84%D8%B0%D9%8A%D9%86-%D8%AA%D9%84%D9%82%D9%88%D8%A7-%D9%84%D9%82%D8%A7%D8%AD-%D8%A7%D9%84%D8%A5%D9%86%D9%81%D9%84%D9%88%D9%86%D8%B2%D8%A7-%D8%A3%D9%82%D9%84-%D8%B9%D8%B1%D8%B6%D8%A9-%D9%84%D9%84%D8%A5%D8%B5%D8%A7%D8%A8%D8%A9-%D8%A8%D8%A3%D8%B9%D8%B1%D8%A7%D8%B6-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-%D8%A7%D9%84%D8%B4%D8%AF%D9%8A%D8%AF%D8%A9
     scrapping.dbSave(url='https://www.aljazeera.net/news/healthmedicine/2020/3/11/%D9%83%D9%8A%D9%81-%D8%AA%D8%B9%D8%B2%D8%B2-%D8%AC%D9%87%D8%A7%D8%B2-%D8%A7%D9%84%D9%85%D9%86%D8%A7%D8%B9%D8%A9-%D9%84%D8%AF%D9%8A%D9%83-%D9%84%D8%AA%D8%AC%D9%86%D8%A8-%D9%81%D9%8A%D8%B1%D9%88%D8%B3',
                          className='wysiwyg wysiwyg--all-content', score=5)

     scrapping.dbSaveFake(url='https://arabic.cnn.com/health/article/2020/11/15/winter-will-be-hard-biontech-vaccine-breakthrough-ceo-says',title="الحل المعجزة",
                     text="يزعم نجم موقع يوتيوب جوردان ساثر، الذي لديه آلاف المتابعين عبر منصات مختلفة على مواقع التواصل الاجتماعي، أنّ ثاني أكسيد الكلور وهو عامل تبييض يستخدم في مواد التنظيف وتبييض الأقمشة والبقع، يساعد على التخلص من فيروس كورونا.",score=1)
     scrapping.dbSave(
    url='https://www.unicef.org/morocco/ar/%D9%85%D8%B1%D8%B6-%D9%81%D9%8A%D8%B1%D9%88%D8%B3-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-19-covid/%D9%82%D8%B5%D8%B5',
    className='field paragraph field_component_text_content  odd-t text_long', score=5)


#------------------- url : https://www.dw.com/ar/%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA-%D8%AE%D8%A7%D8%B7%D8%A6%D8%A9-%D8%B9%D9%86-%D9%81%D9%8A%D8%B1%D9%88%D8%B3-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-%D9%82%D8%AF-%D8%AA%D9%83%D9%84%D9%91%D9%81-%D8%A7%D9%84%D9%86%D8%A7%D8%B3-%D8%AD%D9%8A%D8%A7%D8%AA%D9%87%D9%85/a-52945428
#     scrapping.dbSaveFake("خوف من البضائع الصينية", "وأوضح تجار تجزئة في نيودلهي لوكالة فرانس برس إنهم خزنوا سلعاً صينية مثل المسدسات البلاستيك والشعر المستعار من بين أمور أخرى تم استيرادها من أجل مهرجان هولي في وقت سابق من هذا الشهر.
# وقال فيبين نيجهاوان منجمعية الألعاب الهندية: "المعلومات الخاطئة عن المنتجات الصينية التي تزعم أن هذه السلع قد تنقل فيروس كورونا، تسببت في انخفاض مبيعات المنتجات المخصصة للمهرجان. لقد شهدنا انخفاضاً في المبيعات بحوالي 40 % مقارنة بالعام السابق".")

    #----------------- url : https://www.bbc.com/arabic/science-and-tech-51787845






    # #-------------- url : https://factuel.afp.com/ar/Rumeurs%20Vaccin%20Corona%2012-20 ----------------
    




    # #--------------- url : https://al-ain.com/article/rumors-corona-mosquitoes-transmit-infection





    # #---------------- url : https://www.youm7.com/story/2020/4/20/%D9%83%D9%8A%D9%81-%D8%B1%D8%AF%D8%AA-%D8%A7%D9%84%D8%B5%D8%AD%D8%A9-%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85%D9%8A%D8%A9-%D8%B9%D9%84%D9%89-10-%D8%B4%D8%A7%D8%A6%D8%B9%D8%A7%D8%AA-%D8%AD%D9%88%D9%84-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7/4735033





    # #---------------- url : https://arabic.cnn.com/health/article/2021/02/08/covid-19-vaccine-rumors






    # #------------------ url : https://www.alhurra.com/coronavirus/2020/12/14/%D9%84%D8%A7-%D8%AA%D8%B5%D8%AF%D9%82%D9%87%D8%A7-4-%D8%B4%D8%A7%D8%A6%D8%B9%D8%A7%D8%AA-%D9%84%D9%82%D8%A7%D8%AD-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7




    # #---------------- url : https://www.who.int/ar/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters?gclid=Cj0KCQiAgomBBhDXARIsAFNyUqN1wTofrInTKRrNUZuF4MRDalhx7dyP4Vv676bbVIY-kVu9i28z5xMaAhXKEALw_wcB#antibiotics

    #------------------ url : https://www.skynewsarabia.com/world/1348070-%D8%A7%D9%84%D8%B9%D9%86%D9%81-%D9%8A%D8%AC%D8%AA%D8%A7%D8%AD-%D9%82%D8%B1%D9%8A%D8%A9-%D9%85%D9%83%D8%B3%D9%8A%D9%83%D9%8A%D8%A9-%D9%88%D8%A7%D9%84%D8%B3%D8%A8%D8%A8-%D8%B4%D8%A7%D9%8A%D9%94%D8%B9%D8%A7%D8%AA-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7

    #------------------ url : https://al-ain.com/article/rumor-war-spoils-plan-coexist-corona-5-tools

    #------------------ url : https: // www.youm7.com/story/2020/5/29/%D9 %85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA-%D8%AE%D8%A7%D8%B7%D8%A6%D8%A9-%D8%B9%D9%86-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-%D9%82%D8%AF-%D8%AA%D9%83%D9%84%D9%81%D9%83-%D8%AD%D9%8A%D8%A7%D8%AA%D9%83-%D8%B4%D8%B1%D8%A8-%D8%A7%D9%84%D9%83%D8%AD%D9%88%D9%84-%D8%B3%D8%A8%D8%A8/4795925

    #------------------ url : https: // www.youm7.com/story/2020/8/12/%D9 %81%D9%8A%D8%B3-%D8%A8%D9%88%D9%83-%D9%8A%D8%B2%D9%8A%D9%84-22-5-%D9%85%D9%84%D9%8A%D9%88%D9%86-%D9%85%D9%86%D8%B4%D9%88%D8%B1-%D9%8A%D8%AD%D8%AA%D9%88%D9%89-%D8%B9%D9%84%D9%89-%D8%AE%D8%B7%D8%A7%D8%A8/4924659

    #------------------ url : https://www.youm7.com/story/2020/8/11/%D8%A7%D9%86%D8%AA%D8%B4%D8%B1%D8%AA-%D9%81%D9%89-87-%D8%AF%D9%88%D9%84%D8%A9-%D8%B4%D8%A7%D8%A6%D8%B9%D8%A7%D8%AA-%D8%AD%D9%88%D9%84-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-%D8%A3%D8%AF%D8%AA-%D9%84%D9%88%D9%81%D9%8A%D8%A7%D8%AA-%D9%88%D8%A5%D8%B5%D8%A7%D8%A8%D8%A7%D8%AA/4922930






    #------------------ url : https://www.youm7.com/story/2020/5/23/%D8%AE%D8%A8%D8%B1-%D8%BA%D9%8A%D8%B1-%D8%B5%D8%AD%D9%8A%D8%AD-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7-%D9%84%D9%8A%D8%B3-%D9%81%D9%8A%D8%B1%D9%88%D8%B3-%D9%84%D9%83%D9%86%D9%87-%D8%A8%D9%83%D8%AA%D9%8A%D8%B1%D9%8A%D8%A7-%D8%AA%D8%B3%D8%A8%D8%A8-%D8%AA%D8%AC%D9%84%D8%B7/4790023



    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")
    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")
    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

#     # scrapping.dbSaveFake("", "")
    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")
    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")
    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")
    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")
    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")
    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")
    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

    # scrapping.dbSaveFake("", "")

