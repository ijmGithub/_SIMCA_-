import datetime
from pymongo import MongoClient

class MongoDBConnection:
    /**
     * @brief Initializes MongoDBConnection with host, port, and database name.
     * @param host MongoDB server host address.
     * @param port MongoDB server port.
     * @param db_name MongoDB database name.
     */
    def __init__(self, host='192.168.0.157', port=27017, db_name='SimcaDatabase'):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None
        self.max_count = 10  # Maximum limit of documents

    /**
     * @brief Establishes a connection to MongoDB.
     */
    def connect(self):
        try:
            self.client = MongoClient(self.host, self.port)
            self.db = self.client[self.db_name]
            print("Conexión exitosa a MongoDB")
        except Exception as e:
            print(f"Error al conectar a MongoDB: {e}")

    /**
     * @brief Closes the connection to MongoDB.
     */
    def close(self):
        if self.client:
            self.client.close()

    /**
     * @brief Inserts ambient light intensity into the database.
     * @param value Ambient light intensity value.
     */
    def add_light_intensity(self, value):
        try:
            collection = self.db['light_intensity_collection']
            self.check_and_limit_documents(collection, value)
        except Exception as e:
            print(f"Error al insertar la intensidad de luz ambiental en MongoDB: {e}")

    /**
     * @brief Inserts sensor data into the database.
     * @param data Sensor data.
     */
    def add_sensor_data(self, data):
        try:
            collection = self.db['sensor_data_collection']
            self.check_and_limit_documents(collection, data)
        except Exception as e:
            print(f"Error al insertar los datos del sensor en MongoDB: {e}")

    /**
     * @brief Inserts temperature into the database.
     * @param value Temperature value.
     */
    def add_temperature(self, value):
        try:
            collection = self.db['temperature_collection']
            self.check_and_limit_documents(collection, value)
        except Exception as e:
            print(f"Error al insertar la temperatura en MongoDB: {e}")

    /**
     * @brief Inserts gas concentration into the database.
     * @param value Gas concentration value.
     */
    def add_gas_concentration(self, value):
        try:
            collection = self.db['gas_concentration_collection']
            self.check_and_limit_documents(collection, value)
        except Exception as e:
            print(f"Error al insertar la concentración de gas en MongoDB: {e}")
 
    /**
     * @brief Inserts current date and time into the database.
     * @param value Current date and time value.
     */
    def add_current_datetime(self, value):
        try:
            collection = self.db['datetime_collection']
            self.check_and_limit_documents(collection, value)
        except Exception as e:
            print(f"Error al insertar la fecha y hora actual en MongoDB: {e}")
    
    /**
     * @brief Inserts humidity into the database.
     * @param value Humidity value.
     */
    def add_humidity(self, value):
        try:
            collection = self.db['humidity_collection']
            self.check_and_limit_documents(collection, value)
        except Exception as e:
            print(f"Error al insertar la humedad en MongoDB: {e}")
    
    /**
     * @brief Inserts pressure into the database.
     * @param value Pressure value.
     */
    def add_pressure(self, value):
        try:
            collection = self.db['pressure_collection']
            self.check_and_limit_documents(collection, value)
        except Exception as e:
            print(f"Error al insertar la presión en MongoDB: {e}")

    /**
     * @brief Checks and limits the number of documents in a collection.
     * @param collection MongoDB collection.
     * @param data Data to insert into the collection.
     */
    def check_and_limit_documents(self, collection, data):
        count = collection.count_documents({})
        if count >= self.max_count:
            # If limit is reached, delete the oldest document
            oldest_document = collection.find_one_and_delete({}, sort=[('_id', 1)])
            print(f"Se ha eliminado el documento más antiguo: {oldest_document}")

        # Insert the new document
        collection.insert_one({'value': data})
        print("Dato insertado correctamente")            
    
    /**
     * @brief Retrieves ambient light intensity from the database.
     * @return Ambient light intensity value or None if not found.
     */    
    def get_light_intensity(self):
        try:
            if self.db is not None:
                # Retrieve ambient light intensity from the database
                result = self.db['light_intensity_collection'].find_one()
                if result:
                    # If document is found, get the value of 'value' field
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

    /**
     * @brief Retrieves current date and time from the database.
     * @return Current date and time value or None if not found.
     */
    def get_current_datetime(self):
        try:
            if self.db is not None:
                # Retrieve current date and time from the database
                result = self.db['datetime_collection'].find_one()
                if result:
                    # If document is found, get the value of 'value' field
                    current_datetime = result.get('value')
                    print(f"Fecha y hora actual recuperadas desde MongoDB: {current_datetime}")
                    return current_datetime
                else:
                    print("No se encontró ninguna fecha y hora en la base de datos.")
                    return None
            else:
                print("Error en MongoDB: La conexión no está establecida.")
                return None
        except Exception as e:
            print(f"Error al obtener la fecha y hora actual desde MongoDB: {e}")
            return None

    /**
     * @brief Retrieves temperature from the database.
     * @return Temperature value or None if not found.
     */
    def get_temperature(self):
        try:
            if self.db is not None:
                # Recupera la temperatura desde la base de datos
                result = self.db['temperature_collection'].find_one()
                if result:
                    # Si se encuentra el documento, obtén el valor del campo 'value'
                    temperature = result.get('value')
                    print(f"Temperatura recuperada desde MongoDB: {temperature}")
                    return temperature
                else:
                    print("No se encontró ninguna temperatura en la base de datos.")
                    return None
            else:
                print("Error en MongoDB: La conexión no está establecida.")
                return None
        except Exception as e:
            print(f"Error al obtener la temperatura desde MongoDB: {e}")
            return None


    /**
     * @brief Retrieves gas concentration from the database.
     * @return Gas concentration value or None if not found.
     */
    def get_gas_concentration(self):
        try:
            if self.db is not None:
                # Retrieve gas concentration from the database
                result = self.db['gas_concentration_collection'].find_one()
                if result:
                    # If document is found, get the value of 'value' field
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

    /**
     * @brief Retrieves humidity from the database.
     * @return Humidity value or None if not found.
     */
    def get_humidity(self):
        try:
            if self.db is not None:
                result = self.db['humidity_collection'].find_one()
                if result:
                    humidity = result.get('value')
                    print(f"Humedad recuperada desde MongoDB: {humidity}")
                    return humidity
                else:
                    print("No se encontró ninguna humedad en la base de datos.")
                    return None
            else:
                print("Error en MongoDB: La conexión no está establecida.")
                return None
        except Exception as e:
            print(f"Error al obtener la humedad desde MongoDB: {e}")
            return None

    /**
     * @brief Retrieves pressure from the database.
     * @return Pressure value or None if not found.
     */
    def get_pressure(self):
        try:
            if self.db is not None:
                result = self.db['pressure_collection'].find_one()
                if result:
                    pressure = result.get('value')
                    print(f"Presión recuperada desde MongoDB: {pressure}")
                    return pressure
                else:
                    print("No se encontró ninguna presión en la base de datos.")
                    return None
            else:
                print("Error en MongoDB: La conexión no está establecida.")
                return None
        except Exception as e:
            print(f"Error al obtener la presión desde MongoDB: {e}")
            return None

