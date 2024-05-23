import time
import smbus2
from mongodb_connection import MongoDBConnection

class DS3231:
    def __init__(self, bus=0, address=0x68):
        self.bus = smbus2.SMBus(bus)
        self.address = address

    def _bcd_to_dec(self, bcd):
        return (bcd // 16) * 10 + (bcd % 16)

    def _dec_to_bcd(self, dec):
        return (dec // 10) * 16 + (dec % 10)

    def read_time(self):
        data = self.bus.read_i2c_block_data(self.address, 0x00, 7)
        seconds = self._bcd_to_dec(data[0])
        minutes = self._bcd_to_dec(data[1])
        hours = self._bcd_to_dec(data[2])
        day = self._bcd_to_dec(data[3])
        date = self._bcd_to_dec(data[4])
        month = self._bcd_to_dec(data[5])
        year = self._bcd_to_dec(data[6]) + 2000
        return {
            'seconds': seconds,
            'minutes': minutes,
            'hours': hours,
            'day': day,
            'date': date,
            'month': month,
            'year': year
        }

    def set_time(self, seconds, minutes, hours, day, date, month, year):
        data = [
            self._dec_to_bcd(seconds),
            self._dec_to_bcd(minutes),
            self._dec_to_bcd(hours),
            self._dec_to_bcd(day),
            self._dec_to_bcd(date),
            self._dec_to_bcd(month),
            self._dec_to_bcd(year - 2000)
        ]
        self.bus.write_i2c_block_data(self.address, 0x00, data)

if __name__ == "__main__":
        # Crear una instancia de MongoDBConnection para establecer la conexión con MongoDB
    mongo_connection = MongoDBConnection(host='192.168.0.157', port=27017, db_name='SimcaDatabase')
    mongo_connection.connect()  # Establecer la conexión con MongoDB
    
    # Inicializa el sensor DS3231 en el bus I2C 1 (predeterminado en RPi)
    rtc = DS3231()

    # Establece la hora (si es necesario)
    #rtc.set_time(0, 29, 17, 19, 5, 19, 2024)  # Set the time to 15:30:00 on May 10, 2024

    try:
        while True:
            # Lee la hora actual del DS3231
            current_time = rtc.read_time()
            current_time_str = f"{current_time['year']}-{current_time['month']:02}-{current_time['date']:02} " \
                               f"{current_time['hours']:02}:{current_time['minutes']:02}:{current_time['seconds']:02}"

            # Inserta la fecha y hora actuales en MongoDB
            mongo_connection.add_current_datetime(current_time_str)

            print(f"Current Time: {current_time_str}")

            time.sleep(2)

    except KeyboardInterrupt:
        print("Programa detenido por el usuario")

    finally:
        mongo_connection.close()
