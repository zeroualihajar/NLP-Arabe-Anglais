from graphene_mongo.types import MongoengineObjectType
from mongoengine import Document
from datetime import datetime
from typing import OrderedDict
# from ariadne import QueryType, MutationType

from mongoengine.fields import (
    DateTimeField,
    ReferenceField,
    StringField,
)

class Operation(Document):
    meta = {'collection': 'operation'}
    op = StringField()


class User(Document):
    meta = {'collection': 'user'}
    username = StringField()
    email = StringField()
    password = StringField()


class Historique(Document):
    meta = {'collection': 'historique'}

    text = StringField()
    result = StringField()
    dateCreation = DateTimeField(default=datetime.now)
    user = ReferenceField(User)
    operation = ReferenceField(Operation)


# mutation = MutationType()
# query = QueryType()

# @query.field("hello")
# def resolve_hello(_, info):
#     return "Hi there"


# @mutation.field("adduser")
# def resolve_order_user(_, info, email, password):
#     newUser = User(email, password)
#     users.append(newUser)
#     return newUser
