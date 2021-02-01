import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from graphene.relay import Node
from model import Operation as OperationModel
from model import User as UserModel
from model import Historique as HistoriqueModel


class Operation(MongoengineObjectType):
    class Meta:
        description = "operation"
        model = OperationModel
        interfaces = (Node,)


class User(MongoengineObjectType):
    class Meta:
        description = "user"
        model = UserModel


class Historique(MongoengineObjectType):
    class Meta:
        description = "historique"
        model = HistoriqueModel
        interfaces = (Node,)


class AddUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, username, email, password):
        user = UserModel(username=username, email=email, password=password)
        user.save()
        return AddUser(user=user)


class Login(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(lambda: User)
    def mutate(self, info, email, password):
        user = UserModel(username ="", email=email, password=password)
        user = user.findUnique({email: email})
        return Login(user = user)

class Mutation(graphene.ObjectType):
    addUser = AddUser.Field()
    login = Login.Field()

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return list(UserModel.objects.all())


schema = graphene.Schema(query=Query, types=[Operation, User, Historique])
schema = graphene.Schema(query=Query, mutation=Mutation, types=[Operation, User, Historique])
