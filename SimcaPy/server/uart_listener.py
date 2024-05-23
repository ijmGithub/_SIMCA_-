import serial
import time
from mongodb_connection import MongoDBConnection

# Specify the path to the MongoDB configuration file
mongod_conf_path = 'db/mongod.conf'

# Create an instance of MongoDBConnection to establish a connection to MongoDB
mongo_connection = MongoDBConnection(host='192.168.0.157', port=27017, db_name='SimcaDatabase')
mongo_connection.connect()  # Establecer la conexión con MongoDB

# Configure the serial port
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600 ,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

try:
    # Main loop to listen and process data from the serial port
    while True:
        data = ser.readline().decode('ascii')  # Read a line from the serial port
        if data:  # If the line is not empty, print it
            print(data)

        # Process the received data and add it to the database
        if data:
            # Identify the type of data based on the prefix
            if data.startswith("ADD_LIGHT_INTENSITY"):
                # Light intensity data
                value = float(data.split(":")[1])
                mongo_connection.add_light_intensity(value)
                print("Intensidad de luz ambiental insertada correctamente en MongoDB")
            elif data.startswith("ADD_TEMPERATURE"):
                # Temperature data
                value = float(data.split(":")[1])
                mongo_connection.add_temperature(value)
                print("Temperatura insertada correctamente en MongoDB")
            elif data.startswith("ADD_GAS_CONCENTRATION"):
                # Gas concentration data
                value = float(data.split(":")[1])
                mongo_connection.add_gas_concentration(value)
                print("Concentración de gas insertada correctamente en MongoDB")
            elif data.startswith("ADD_DATE_TIME"):
                # Get the current date and time
                value = float(data.split(":")[1])
                mongo_connection.add_current_datetime(value)
                print("Fecha y hora actual insertada correctamente en MongoDB")
            else:
                print("Tipo de datos desconocido:", data)

            # Print the received data for debugging purposes
            print("Datos recibidos:", data)

        # Wait a short period of time before reading the next set of data
        time.sleep(0.1)

except KeyboardInterrupt:
     Handle keyboard interruption (Ctrl+C)
    print("Programa detenido por el usuario")

finally:
    # Close the serial port and the MongoDB connection
    ser.close()
    mongo_connection.close()
