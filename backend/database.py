from mongoengine import connect
from model import User


connect('DatabaseCollected', host='mongodb://localhost',
        port=27017, alias='default')



def init_db():
    user = User(username = 'hanae', email='hajar@gmail.com', password ='123')
    user.save()
#     data = scrapping.dbSave(url='https://ar.hibapress.com/details-281066.html', className='main-content tie-col-md-8 tie-col-xs-12')


    

