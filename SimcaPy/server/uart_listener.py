import serial
import time
from mongodb_connection import MongoDBConnection

# Especifica la ruta al archivo de configuración de MongoDB
mongod_conf_path = 'db/mongod.conf'

# Crear una instancia de MongoDBConnection para establecer la conexión con MongoDB
mongo_connection = MongoDBConnection(host='192.168.0.157', port=27017, db_name='SimcaDatabase')
mongo_connection.connect()  # Establecer la conexión con MongoDB

# Configura el puerto serial
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600 ,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

try:
    # Bucle principal para escuchar y procesar datos desde el puerto serial
    while True:
        data = ser.readline().decode('ascii')  # Lee una línea desde el puerto serial
        if data:  # Si la línea no está vacía, imprímela
            print(data)

        # Procesar los datos recibidos y agregarlos a la base de datos
        if data:
            # Identificar el tipo de datos en función del prefijo
            if data.startswith("ADD_LIGHT_INTENSITY"):
                # Datos de intensidad de luz
                value = float(data.split(":")[1])
                mongo_connection.add_light_intensity(value)
                print("Intensidad de luz ambiental insertada correctamente en MongoDB")
            elif data.startswith("ADD_TEMPERATURE"):
                # Datos de temperatura
                value = float(data.split(":")[1])
                mongo_connection.add_temperature(value)
                print("Temperatura insertada correctamente en MongoDB")
            elif data.startswith("ADD_GAS_CONCENTRATION"):
                # Datos de concentración de gas
                value = float(data.split(":")[1])
                mongo_connection.add_gas_concentration(value)
                print("Concentración de gas insertada correctamente en MongoDB")
            elif data.startswith("ADD_DATE_TIME"):
                # Obtener la fecha y hora actual
                value = float(data.split(":")[1])
                mongo_connection.add_current_datetime(value)
                print("Fecha y hora actual insertada correctamente en MongoDB")
            else:
                print("Tipo de datos desconocido:", data)

            # Imprimir los datos recibidos para propósitos de depuración
            print("Datos recibidos:", data)

        # Esperar un breve periodo de tiempo antes de leer el próximo conjunto de datos
        time.sleep(0.1)

except KeyboardInterrupt:
    # Manejar la interrupción del teclado (Ctrl+C)
    print("Programa detenido por el usuario")

finally:
    # Cerrar el puerto serial y la conexión con la base de datos MongoDB
    ser.close()
    mongo_connection.close()
