import socket
import random
import time
import datetime
from mongodb_connection import MongoDBConnection

# Server IP address and port to listen on
SERVER_IP = '192.168.0.164'
SERVER_PORT = 9999

# Specify the path to the MongoDB configuration file
mongod_conf_path = 'db/mongod.conf'

# Create an instance of MongoDBConnection to establish a connection to MongoDB
mongo_connection = MongoDBConnection(host='192.168.0.157', port=27017, db_name='SimcaDatabase')
mongo_connection.connect()  # Establecer la conexión con MongoDB

# Attempt to start the server in a loop until the port is available
server_socket = None
while server_socket is None:
    try:
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the specified IP address and port
        server_socket.bind((SERVER_IP, SERVER_PORT))

        # Bind the socket to the specified IP address and port
        server_socket.listen(1)
        print(f"Servidor en ejecución en {SERVER_IP}:{SERVER_PORT}...")
    except OSError as e:
        if e.errno == 98:  # Error "Address already in use"
            print(f"Puerto {SERVER_PORT} ya está en uso. Esperando 5 segundos...")
            time.sleep(5)
        else:
            raise

# Main server loop
while True:
    # Accept the incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")

    try:
        # Receive data from the client
        data = client_socket.recv(1024).decode('ascii')

        # Process the client's request
        if data == "GET_LIGHT_INTENSITY":
            # Retrieve ambient light intensity from the database
            light_intensity = mongo_connection.get_light_intensity()

          # Send the ambient light intensity to the client
            client_socket.send(str(light_intensity).encode('ascii'))
        elif data == "GET_PRESSURE":
            # Retrieve pressure from the database
            pressure = mongo_connection.get_pressure()
            # Send the pressure to the client
            client_socket.send(str(pressure).encode('ascii'))
        elif data == "GET_HUMIDITY":
            # Retrieve humidity from the database
            humidity = mongo_connection.get_humidity()
            # Send the humidity to the client
            client_socket.send(str(humidity).encode('ascii'))            
        elif data == "GET_DATE_TIME":
           # Retrieve current date and time from the database
            current_datetime = mongo_connection.get_current_datetime()

            # Send the current date and time to the client
            client_socket.send(current_datetime.encode('ascii'))
        elif data == "GET_TEMPERATURE":
            # Retrieve temperature from the database
            temperature = mongo_connection.get_temperature()
            # Send the temperature to the client
            client_socket.send(str(temperature).encode('ascii'))
        elif data == "GET_GAS_CONCENTRATION":
            # Retrieve gas concentration from the database
            gas_concentration = mongo_connection.get_gas_concentration()
            # Send the gas concentration to the client
            client_socket.send(str(gas_concentration).encode('ascii'))
        else:
            # Send an error message if an invalid request is received
            client_socket.send("Solicitud no válida".encode('ascii'))
    except Exception as e:
        print(f"Error al procesar la solicitud: {e}")
    finally:
        # Close the client socket
        client_socket.close()
