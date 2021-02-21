from datetime import datetime
from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, ObjectIdField
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField, IntField, FloatField, ListField
)

POST_STATUS = ('pending', 'published', 'deleted', 'draft')


class Operation(EmbeddedDocument):
    meta = {'collection': 'operation'}
    nameOp = StringField()
    resultOp = ListField(StringField())
    dateOp = DateTimeField(default=datetime.now)


class Text(EmbeddedDocument):
    title = StringField()
    content = StringField(required=True)
    type = StringField()
    dateCr = DateTimeField(default=datetime.now)
    emotion = IntField(default=-1)
    fakeNews = IntField(default=-1)
    operation = ListField(EmbeddedDocumentField(Operation))


class User(Document):
    meta = {'collection': 'user'}
    username = StringField()
    email = StringField(required=True)
    password = StringField(required=True)
    text = ListField(EmbeddedDocumentField(Text))
    status = StringField(choices=POST_STATUS)


class Data(Document):
    meta = {'collection': 'data'}
    title = StringField(required=True)
    url = StringField(required=True)
    content = StringField(required=True)
    language = StringField(required=True)
    score = FloatField(required=True)
    class_result = FloatField(required=True)
    operation = ListField(EmbeddedDocumentField(Operation))
