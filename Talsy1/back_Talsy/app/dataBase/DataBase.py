from pymongo  import MongoClient, errors

class mongo_instance:
    def __init__(self):
        self.uri = "mongodb+srv://mauroship951:<aEqr6>26iRn$.Md>@talsydatabase.niz5ajk.mongodb.net/?retryWrites=true&w=majority&appName=TalsyDataBase"
        self.client = None
        self.db = None

    def conectar(self):
        #"""Establece la conexión con MongoDB Atlas."""
        try:
            self.client = MongoClient(self.uri)
            print("Conexión exitosa a MongoDB Atlas")
            # Conectar a la base de datos y colección
            self.db = self.client["TalsyDataBase"]

        except errors.ConnectionFailure as e:
            print(f"Error al conectar a MongoDB Atlas: {e}")
            self.client = None

    def get_database(self, db_name="TalsyDataBase"):
        #"""Devuelve la base de datos especificada."""
        if self.client:
            self.db = self.client[db_name]
            print(f"Accediendo a la base de datos: {db_name}")
            return self.db
        else:
            print("No hay conexión activa.")
            return None
        
    
    def create_collection(self, collection_name: str, db_name="TalsyDataBase"):
        """Crea una colección en la base de datos especificada si no existe."""
        db = self.get_database(db_name)
        if db:
            if collection_name not in db.list_collection_names():
                collection = db.create_collection(collection_name)
                print(f"Colección '{collection_name}' creada.")
                return collection
            else:
                print(f"La colección '{collection_name}' ya existe.")
                return db[collection_name]  # Devuelve la colección existente
        return None
    
    def get_collection(self, collection_name: str, db_name="TalsyDataBase"):
        """Obtiene una colección de la base de datos especificada."""
        db = self.get_database(db_name)
        if db:
            collection = db[collection_name]
            if collection:
                print(f"Colección '{collection_name}' obtenida.")
                return collection
            else:
                print(f"No se encontró la colección '{collection_name}'.")
        return None



    def get_collections(self):
        """Retorna una lista de nombres de colecciones en la base de datos."""
        if self.db is not None:
            return self.db.list_collection_names()
        else:
            print("No se pudo acceder a la base de datos.")
            return []    
        

  

    def cerrar_conexion(self):
        #"""Cierra la conexión con MongoDB."""
        if self.client:
            self.client.close()
            print("Conexión cerrada")

# Uso de la clase
if __name__ == "__main__":
    # Reemplaza la contraseña en <aEqr6>26iRn$.Md con la contraseña correcta
    uri = "mongodb+srv://mauroship951:<aEqr6>26iRn$.Md>@talsydatabase.niz5ajk.mongodb.net/?retryWrites=true&w=majority&appName=TalsyDataBase"

    conexion = mongo_instance()
    conexion.conectar()
    conexion.get_database()
    conexion.get_collections()
    # Cerrar la conexión
    conexion.cerrar_conexion()
