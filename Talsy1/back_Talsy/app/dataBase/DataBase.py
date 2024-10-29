# back_Talsy/app/dataBase/DataBase.py

from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri: str):
        self.client = MongoClient(uri)
        self.db = None

    def get_database(self, db_name="TalsyDataBase"):
        """Devuelve la base de datos especificada."""
        if self.client:
            self.db = self.client[db_name]
            print(f"Accediendo a la base de datos: {db_name}")
            return self.db
        else:
            print("No hay conexión activa.")
            return None

    def create_collection(self, collection_name: str, db_name="TalsyDataBase"):
        """Crea una colección si no existe."""
        db = self.get_database(db_name)
        if db is not None :
            if collection_name not in db.list_collection_names():
                collection = db.create_collection(collection_name)
                print(f"Colección '{collection_name}' creada.")
                return collection
            else:
                print(f"La colección '{collection_name}' ya existe.")
                return db[collection_name]
        return None
