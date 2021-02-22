from graphene.types.scalars import String
from numpy import number
from NLP import BagOfWords, BagOfWordsEn, Lemmatization, Stemming, StemmingEn, StopWords, Naturalproc, LemmatizationEn, Tokenization, PosTagging, TFIDF
from emotion import TrainingModels
from FakeNews import TrainingModel
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
        model = TextModel


#----------------------------------
class Data(MongoengineObjectType):
    class Meta:
        description = "data"
        model = DataModel



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
        print(resultOp)
        user.save()
        return AddText(user=user)


class AddEmotion(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        content = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id, content):
        rs: number
        resultOp = TrainingModels.getResult("data/DTC.pkl" , content)
        if (resultOp[0] == 'Positive'):
            rs = 1
        else:
            rs = 0
        
        operation = OperationModel(
            nameOp="emt", dateOp=date.today(), resultOp=resultOp)
        newText = TextModel(
            content=content, dateCr=date.today(), emotion=rs, fakeNews=-1)

        user = UserModel.objects.get(pk=ObjectId(id))
        user.text.append(newText)
        for x in user.text:
            if(x['content'] == content):
                x.operation.append(operation)
        print(resultOp)
        user.save()
        return AddEmotion(user=user)


class AddFake(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        content = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id, content):
        rs = []
        resultOp = TrainingModel.getResult("data/Fake/knn.pkl", content)
        if (resultOp[0] == 1):
            rs = rs.append("1")
        else:
            rs = rs.append("0")

        operation = OperationModel(
            nameOp="emt", dateOp=date.today(), resultOp=rs)
        newText = TextModel(
            content=content, dateCr=date.today(), emotion=-1, fakeNews=resultOp[0])

        user = UserModel.objects.get(pk=ObjectId(id))
        user.text.append(newText)
        for x in user.text:
            if(x['content'] == content):
                x.operation.append(operation)
        # print(resultOp)
        user.save()
        return AddFake(user=user)


class Mutation(graphene.ObjectType):
    addUser = AddUser.Field()
    addText = AddText.Field()
    addEmotion = AddEmotion.Field()
    addFake = AddFake.Field()


class Query(graphene.ObjectType):
    users = graphene.List(User)
    data = graphene.List(Data, class_result=graphene.String())
    
    get_user = graphene.Field(User, email = graphene.String())
    get_his = graphene.Field(User, id=graphene.String())
    get_details = graphene.Field(Data, id = graphene.String())
    get_res = graphene.Field(User, id=graphene.String())


    def resolve_users(self, info):
        return list(UserModel.objects.all())
    
    def resolve_get_user(self, info, email):
       user = UserModel.objects.filter(email=email).first()
       return user

    def resolve_get_his(self, info, id):
       user = UserModel.objects.filter(id=id).first()
       return user

    def resolve_data(self, info):
        
        return list(DataModel.objects.filter(class_result="1").all())
    
    def resolve_get_details(self, info, id):
        return DataModel.objects.filter(id= id).first()

    def resolve_get_res(self, info, id):
        
        user = UserModel.objects.filter(id=id).first()
        
        return user
        


        
schema = graphene.Schema(query=Query, mutation=Mutation, types=[User, Operation, Text, Data])

# #---------execute nlp operation choosed by user---------


def nlp_Operation(text, operations):
    resultOp = []

    if 'Tokenization' in operations:
        resultOp = Tokenization.tokenizationProcess(text)
        text = ' '.join(resultOp)

    if 'Stop Words' in operations:
        resultOp = StopWords.deleteStopWords(text)
        text = ' '.join(resultOp)
        # Query.saveOperation(user_id, 'Stop_words', resultOp, originText)

    if 'Stop WordsEn' in operations:
        resultOp = StopWords.deleteStopWordsEn(text)
        text = ' '.join(resultOp)
        # Query.saveOperation(user_id, 'Stop_words', resultOp, originText)


    if 'Stemming' in operations:
        resultOp = Stemming.defineStemming(text)
        text = ' '.join(resultOp)
        # Query.saveOperation(user_id, 'Stemming', resultOp, originText)

    if 'StemmingEn' in operations:
        resultOp = StemmingEn.defineStemming(text)
        text = ' '.join(resultOp)

    if 'Lemmatization' in operations:
        resultOp = Lemmatization.getLemmatization(text)
        text = ' '.join(resultOp)
        #Query.saveOperation(user_id, 'Lemmatization', resultOp, originText)

    if 'LemmatizationEn' in operations:
        resultOp = LemmatizationEn.getLemmatization(text)
        text = ' '.join(resultOp)

    if 'Bag Of Words' in operations:
        resultOp = BagOfWords.getbagOfWords(text)
        text = ' '.join(resultOp)
        #Query.saveOperation(user_id, 'BagOfWords', resultOp, originText)
    
    if 'Bag Of WordsEn' in operations:
        resultOp = BagOfWordsEn.getbagOfWordsEn(text)
        # print(test)
        text = ' '.join(resultOp)

    if 'Pos Tagging' in operations:
        test = PosTagging.getpos(text)
        resultOp = ([str(i) for i in test])
        text = ' '.join(resultOp)

    if 'TF-IDF' in operations:
        test = [TFIDF.gettf(text)]
        resultOp = ([str(i) for i in test])
        text = ' '.join(resultOp)

     
    if 'nlp' in operations:
        resultOp = Naturalproc.getNlp(text)
        text = ' '.join(resultOp)
    return resultOp
