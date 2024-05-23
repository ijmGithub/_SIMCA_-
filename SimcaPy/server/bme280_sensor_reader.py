import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280
from mongodb_connection import MongoDBConnection

# Inicializa I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Inicializa el sensor BME280
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# Configura la presión del nivel del mar para tu localización
bme280.sea_level_pressure = 1013.25

# Crear una instancia de MongoDBConnection para establecer la conexión con MongoDB
mongo_connection = MongoDBConnection(host='192.168.0.157', port=27017, db_name='SimcaDatabase')
mongo_connection.connect()  # Establecer la conexión con MongoDB

try:
    while True:
        temperature = bme280.temperature
        humidity = bme280.humidity
        pressure = bme280.pressure

        # Inserta los datos en MongoDB
        #mongo_connection.add_temperature(temperature)
        mongo_connection.add_humidity(humidity)
        mongo_connection.add_pressure(pressure)

        print(f"Temperature: {temperature:.2f} C")
        print(f"Humidity: {humidity:.2f} %")
        print(f"Pressure: {pressure:.2f} hPa")

        time.sleep(2)

except KeyboardInterrupt:
    print("Programa detenido por el usuario")

finally:
    mongo_connection.close()
