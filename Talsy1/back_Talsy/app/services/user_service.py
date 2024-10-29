# back_Talsy/app/services/user_service.py

from back_Talsy.app.dataBase.DataBase import MongoDB

class UserService:
    def __init__(self):
        # Instancia del cliente de MongoDB
        self.mongo_instance = MongoDB('mongodb+srv://mauroship951:aEqr6>26iRn$.Md@talsydatabase.niz5ajk.mongodb.net/?retryWrites=true&w=majority&appName=TalsyDataBase')

        # Crear o acceder a la colección 'users'
        self.collection = self.mongo_instance.create_collection("Mauro")

    def add_user(self, user_data):
        """Agrega un nuevo usuario a la colección."""
        if self.collection:
            result = self.collection.insert_one(user_data)
            print(f"Usuario agregado con ID: {result.inserted_id}")
            return result.inserted_id
        else:
            print("Error: No se pudo acceder a la colección 'users'.")
            return None
