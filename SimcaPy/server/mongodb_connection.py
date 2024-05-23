import datetime
from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, host='192.168.0.157', port=27017, db_name='SimcaDatabase'):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None
        self.max_count = 10  # Límite máximo de documentos

    def connect(self):
        try:
            self.client = MongoClient(self.host, self.port)
            self.db = self.client[self.db_name]
            print("Conexión exitosa a MongoDB")
        except Exception as e:
            print(f"Error al conectar a MongoDB: {e}")

    def close(self):
        if self.client:
            self.client.close()

    # Método para insertar la intensidad de luz ambiental en la base de datos
    def add_light_intensity(self, value):
        try:
            collection = self.db['light_intensity_collection']
            self.check_and_limit_documents(collection, value)
        except Exception as e:
            print(f"Error al insertar la intensidad de luz ambiental en MongoDB: {e}")

    # Método para insertar datos del sensor en la base de datos
    def add_sensor_data(self, data):
        try:
            collection = self.db['sensor_data_collection']
            self.check_and_limit_documents(collection, data)
        except Exception as e:
            print(f"Error al insertar los datos del sensor en MongoDB: {e}")

    # Método para insertar la temperatura en la base de datos
    def add_temperature(self, value):
        try:
            collection = self.db['temperature_collection']
            self.check_and_limit_documents(collection, value)
        except Exception as e:
            print(f"Error al insertar la temperatura en MongoDB: {e}")

    # Método para insertar la concentración de gas en la base de datos
    def add_gas_concentration(self, value):
        try:
            collection = self.db['gas_concentration_collection']
            self.check_and_limit_documents(collection, value)
        except Exception as e:
            print(f"Error al insertar la concentración de gas en MongoDB: {e}")
 
    # Método para insertar la fecha y hora actual en la base de datos
    def add_current_datetime(self, value):
        try:
            collection = self.db['current_datetime_collection']
            self.check_and_limit_documents(collection, value)
        except Exception as e:
            print(f"Error al insertar la fecha y hora actual en MongoDB: {e}")


    # Método para verificar y limitar la cantidad de documentos en una colección
    def check_and_limit_documents(self, collection, data):
        count = collection.count_documents({})
        if count >= self.max_count:
            # Si se alcanza el límite, se elimina el documento más antiguo
            oldest_document = collection.find_one_and_delete({}, sort=[('_id', 1)])
            print(f"Se ha eliminado el documento más antiguo: {oldest_document}")

        # Inserta el nuevo documento
        collection.insert_one({'value': data})
        print("Dato insertado correctamente")            
    
    def get_light_intensity(self):
        try:
            if self.db is not None:
                # Recupera la intensidad de luz ambiental desde la base de datos
                result = self.db['light_intensity_collection'].find_one()
                if result:
                    # Si se encuentra el documento, obtén el valor del campo 'value'
                    light_intensity = result.get('value')
                    print(f"Intensidad de luz ambiental recuperada desde MongoDB: {light_intensity}")
                    return light_intensity
                else:
                    print("No se encontró ninguna intensidad de luz ambiental en la base de datos.")
                    return None
            else:
                print("Error en MongoDB: La conexión no está establecida.")
                return None
        except Exception as e:
            print(f"Error al obtener la intensidad de luz ambiental desde MongoDB: {e}")
            return None


    # Método para obtener los datos del sensor desde la base de datos
    def get_sensor_data(self):
        try:
            # Aquí implementa la lógica para recuperar los datos del sensor desde la base de datos
            # Por ejemplo:
            # sensor_data = self.db['sensor_data_collection'].find_one()
            # Donde 'sensor_data_collection' es el nombre de la colección donde se almacenan los datos del sensor.
            # En este ejemplo, se supone que hay un solo documento en la colección que contiene los datos del sensor.
            # Si necesitas lógica más compleja para recuperar estos datos, adapta este método según tus necesidades.
            sensor_data = {
                'temperature': 25.5,  # Ejemplo de temperatura
                'humidity': 50.0,      # Ejemplo de humedad
                'pressure': 1013.25   # Ejemplo de presión
            }
            return sensor_data
        except Exception as e:
            print(f"Error al obtener los datos del sensor desde MongoDB: {e}")
            return None

    # Método para obtener la fecha y hora actual desde la base de datos
    def get_current_datetime(self):
        try:
            # Aquí implementa la lógica para recuperar la fecha y hora actual desde la base de datos
            # Por ejemplo:
            # current_datetime = self.db['datetime_collection'].find_one()['datetime']
            # Donde 'datetime_collection' es el nombre de la colección donde se almacena la fecha y hora.
            # En este ejemplo, se supone que hay un solo documento en la colección que contiene la fecha y hora.
            # Si necesitas lógica más compleja para recuperar estos datos, adapta este método según tus necesidades.
            current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return current_datetime
        except Exception as e:
            print(f"Error al obtener la fecha y hora actual desde MongoDB: {e}")
            return None

    # Método para obtener la temperatura desde la base de datos
    def get_temperature(self):
        try:
            # Aquí implementa la lógica para recuperar la temperatura desde la base de datos
            # Por ejemplo:
            # temperature = self.db['temperature_collection'].find_one()['value']
            # Donde 'temperature_collection' es el nombre de la colección donde se almacena la temperatura.
            # 'value' es el campo que contiene el valor de la temperatura.
            # En este ejemplo, se supone que hay un solo documento en la colección que contiene el valor de la temperatura.
            temperature = 25.0  # Ejemplo de valor fijo            # Si necesitas lógica más compleja para recuperar estos datos, adapta este método según tus necesidades.

            return temperature
        except Exception as e:
            print(f"Error al obtener la temperatura desde MongoDB: {e}")
            return None    

    # Método para obtener la concentración de gas desde la base de datos
    def get_gas_concentration(self):
        try:
            if self.db is not None:
                # Recupera la concentración de gas desde la base de datos
                result = self.db['gas_concentration_collection'].find_one()
                if result:
                    # Si se encuentra el documento, obtén el valor del campo 'value'
                    gas_concentration = result.get('value')
                    print(f"Concentración de gas recuperada desde MongoDB: {gas_concentration}")
                    return gas_concentration
                else:
                    print("No se encontró ninguna concentración de gas en la base de datos.")
                    return None
            else:
                print("Error en MongoDB: La conexión no está establecida.")
                return None
        except Exception as e:
            print(f"Error al obtener la concentración de gas desde MongoDB: {e}")
            return None
       

# Ejemplo de uso:
# connection = MongoDBConnection(host='localhost', port=27017, db_name='mydatabase')
# connection.connect()
# light_intensity = connection.get_light_intensity()
# print(f"Intensidad de luz ambiental: {light_intensity}")
# connection.close()
