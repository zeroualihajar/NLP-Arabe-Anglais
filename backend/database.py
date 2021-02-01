from mongoengine import connect
from model import User


connect('DatabaseCollected', host='mongodb://localhost',
        port=27017, alias='default')



def init_db():
    user = User(username = 'hanae', email='hajar@gmail.com', password ='123')
    user.save()

    

