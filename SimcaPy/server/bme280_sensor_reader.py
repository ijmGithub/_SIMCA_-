import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280
from mongodb_connection import MongoDBConnection

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the BME280 sensor
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# Configure the sea level pressure for your location
bme280.sea_level_pressure = 1013.25

# Create an instance of MongoDBConnection to establish a connection to MongoDB
mongo_connection = MongoDBConnection(host='192.168.0.157', port=27017, db_name='SimcaDatabase')
mongo_connection.connect()  # Establecer la conexión con MongoDB

try:
    while True:
        # Read temperature, humidity, and pressure from BME280 sensor
        temperature = bme280.temperature
        humidity = bme280.humidity
        pressure = bme280.pressure

        # Insert data into MongoDB
        #mongo_connection.add_temperature(temperature)
        mongo_connection.add_humidity(humidity)
        mongo_connection.add_pressure(pressure)

        # Print sensor data
        print(f"Temperature: {temperature:.2f} C")
        print(f"Humidity: {humidity:.2f} %")
        print(f"Pressure: {pressure:.2f} hPa")

        # Wait for 2 seconds before reading the sensor again
        time.sleep(2)

except KeyboardInterrupt:
    print("Programa detenido por el usuario")

finally:
    # Close the connection to MongoDB
    mongo_connection.close()
