
from pymongo  import MongoClient, errors
from ...app.dataBase.DataBase import mongo_instance
from ...app.models.user_model import User
from bson import ObjectId

class UserService:
        
    def __init__(self):
        mongo_instance()
        self.collection = mongo_instance.create_collection(self,'users')
    