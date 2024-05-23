import socket
import random
import time
import datetime
from mongodb_connection import MongoDBConnection

# Dirección IP y puerto en el que escuchará el servidor
SERVER_IP = '192.168.0.164'
SERVER_PORT = 9999


# Especifica la ruta al archivo de configuración de MongoDB
mongod_conf_path = 'db/mongod.conf'

# Crear una instancia de MongoDBConnection para establecer la conexión con MongoDB
mongo_connection = MongoDBConnection(host='192.168.0.157', port=27017, db_name='SimcaDatabase')
mongo_connection.connect()  # Establecer la conexión con MongoDB

# Intentar iniciar el servidor en un bucle hasta que el puerto esté disponible
server_socket = None
while server_socket is None:
    try:
        # Crear un socket TCP/IP
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Enlazar el socket a la dirección IP y puerto especificados
        server_socket.bind((SERVER_IP, SERVER_PORT))

        # Escuchar conexiones entrantes (máximo 1 conexión en cola)
        server_socket.listen(1)
        print(f"Servidor en ejecución en {SERVER_IP}:{SERVER_PORT}...")
    except OSError as e:
        if e.errno == 98:  # Error "Address already in use"
            print(f"Puerto {SERVER_PORT} ya está en uso. Esperando 5 segundos...")
            time.sleep(5)
        else:
            raise

# Bucle principal del servidor
while True:
    # Aceptar la conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")

    try:
        # Recibir datos del cliente
        data = client_socket.recv(1024).decode('ascii')

        # Procesar la solicitud del cliente
        if data == "GET_LIGHT_INTENSITY":
            # Obtener la intensidad de luz ambiental desde la base de datos
            light_intensity = mongo_connection.get_light_intensity()
            # Simular la obtención de la intensidad de luz ambiental (valor aleatorio)
            #light_intensity = random.randint(100, 1000)  # Valor aleatorio entre 100 y 1000 lux
            # Enviar la intensidad de luz ambiental al cliente
            client_socket.send(str(light_intensity).encode('ascii'))
        elif data == "GET_PRESSURE":
            # Obtener la presión desde la base de datos
            pressure = mongo_connection.get_pressure()
            # Enviar la presión al cliente
            client_socket.send(str(pressure).encode('ascii'))
        elif data == "GET_HUMIDITY":
            # Obtener la humedad desde la base de datos
            humidity = mongo_connection.get_humidity()
            # Enviar la humedad al cliente
            client_socket.send(str(humidity).encode('ascii'))            
        elif data == "GET_DATE_TIME":
            # Obtener la fecha y hora actual desde la base de datos
            current_datetime = mongo_connection.get_current_datetime()
            # Enviar la fecha y hora actual al cliente

            # Obtener la fecha y hora actual
            # current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Enviar la fecha y hora actual al cliente
            client_socket.send(current_datetime.encode('ascii'))
        elif data == "GET_TEMPERATURE":
            # Obtener la temperatura desde la base de datos
            temperature = mongo_connection.get_temperature()
            # Simular la obtención de la temperatura del termopar tipo K (valor aleatorio)
            # temperature = random.uniform(0.0, 100.0)  # Temperatura aleatoria entre 0.0 y 100.0 grados Celsius
            # Enviar la temperatura al cliente
            client_socket.send(str(temperature).encode('ascii'))
        elif data == "GET_GAS_CONCENTRATION":
            # Obtener la concentración de gas desde la base de datos
            gas_concentration = mongo_connection.get_gas_concentration()
            # Simular la obtención de la concentración de gas medida por el MQ135 (valor aleatorio)
            # gas_concentration = random.uniform(0.0, 100.0)  # Concentración de gas aleatoria entre 0.0 y 100.0 %
            # Enviar la concentración de gas al cliente
            client_socket.send(str(gas_concentration).encode('ascii'))
        else:
            # Enviar un mensaje de error si se recibe una solicitud no válida
            client_socket.send("Solicitud no válida".encode('ascii'))
    except Exception as e:
        print(f"Error al procesar la solicitud: {e}")
    finally:
        # Cerrar el socket del cliente
        client_socket.close()
