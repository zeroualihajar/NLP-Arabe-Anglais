from NLP import BagOfWords, Lemmatization, Stemming, StopWords
import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from datetime import date
from bson import ObjectId

from models import User as UserModel
from models import Operation as OperationModel
from models import Text as TextModel
from models import Data as DataModel




#----------------------------------
class User(MongoengineObjectType):
    class Meta:
        description = "user"
        model = UserModel


#----------------------------------
class Operation(MongoengineObjectType):
    class Meta:
        description = "operation"
        model = OperationModel


#----------------------------------
class Text(MongoengineObjectType):
    class Meta:
        description = "text"
        model = DataModel


#----------------------------------
class Data(MongoengineObjectType):
    class Meta:
        description = "data"
        model = TextModel



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



class AddText(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        content = graphene.String(required=True)
        nameOp = graphene.String(required=True)
        resultOp = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id, content,  nameOp):

        resultOp = nlp_Operation(content, nameOp)
        operation = OperationModel(nameOp=nameOp, dateOp=date.today(), resultOp=resultOp)
        newText = TextModel(content=content, dateCr=date.today(),emotion=-1, fakeNews=-1)

        user = UserModel.objects.get(pk=ObjectId(id))
        user.text.append(newText)
        for x in user.text:
            if(x['content'] == content):
                x.operation.append(operation)
            
        user.save()
        return AddText(user=user)


class Mutation(graphene.ObjectType):
    addUser = AddUser.Field()
    #addOp = AddOp.Field()
    addText = AddText.Field()


class Query(graphene.ObjectType):
    users = graphene.List(User)
    get_user = graphene.Field(User, email = graphene.String())


    def resolve_users(self, info):
        return list(UserModel.objects.all())
    
    def resolve_get_user(self, info, email):
       user = UserModel.objects.filter(email=email).first()
       return user

    
    
    

   
    


#schema = graphene.Schema(query=Query, types=[Operation, User, Historique])
schema = graphene.Schema(query=Query, mutation=Mutation, types=[User, Operation, Text, Data])

# #---------execute nlp operation choosed by user---------
def nlp_Operation(text, operations):
    
    if 'Stop_words' in operations:
        resultOp = StopWords.deleteStopWords(text)
        #text = ' '.join(resultOp)
        # Query.saveOperation(user_id, 'Stop_words', resultOp, originText)

    if 'Stemming' in operations:
        resultOp = Stemming.defineStemming(text)
        #text = ' '.join(resultOp)
        # Query.saveOperation(user_id, 'Stemming', resultOp, originText)

    if 'Lemmatization' in operations:
        resultOp = Lemmatization.getLemmatization(text)
        #text = ' '.join(resultOp)
        #Query.saveOperation(user_id, 'Lemmatization', resultOp, originText)

    if 'BagOfWords' in operations:
        resultOp = BagOfWords.getbagOfWords(text)
        #text = ' '.join(resultOp)
        #Query.saveOperation(user_id, 'BagOfWords', resultOp, originText)
    return resultOp
