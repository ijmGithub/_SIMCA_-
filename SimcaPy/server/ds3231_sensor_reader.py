import time
import smbus2
from mongodb_connection import MongoDBConnection

class DS3231:
    /**
     * @brief Initializes the DS3231 class with I2C bus and address.
     * @param bus I2C bus number (default 0).
     * @param address I2C address of DS3231 (default 0x68).
     */
    def __init__(self, bus=0, address=0x68):
        self.bus = smbus2.SMBus(bus)
        self.address = address

    /**
     * @brief Converts BCD (Binary Coded Decimal) to decimal.
     * @param bcd BCD value to convert.
     * @return Decimal value.
     */
    def _bcd_to_dec(self, bcd):
        return (bcd // 16) * 10 + (bcd % 16)

    /**
     * @brief Converts decimal to BCD (Binary Coded Decimal).
     * @param dec Decimal value to convert.
     * @return BCD value.
     */
    def _dec_to_bcd(self, dec):
        return (dec // 10) * 16 + (dec % 10)

    /**
     * @brief Reads the current time from the DS3231 module.
     * @return Dictionary containing the current time components (seconds, minutes, hours, day, date, month, year).
     */
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

    /**
     * @brief Sets the time on the DS3231 module.
     * @param seconds Seconds value (0-59).
     * @param minutes Minutes value (0-59).
     * @param hours Hours value (0-23).
     * @param day Day of the week (1-7).
     * @param date Date of the month (1-31).
     * @param month Month of the year (1-12).
     * @param year Year (four digits).
     */
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
    /**
     * @brief Main program loop to read time from DS3231 and store it in MongoDB.
     */
       
    # Create an instance of MongoDBConnection to establish a connection to MongoDB   
    mongo_connection = MongoDBConnection(host='192.168.0.157', port=27017, db_name='SimcaDatabase')
    mongo_connection.connect()  # Establish the connection to MongoDB
    
    # Initialize the DS3231 sensor on the I2C bus 1 (default on RPi))
    rtc = DS3231()

    try:
        while True:
            # Read the current time from the DS3231
            current_time = rtc.read_time()
            current_time_str = f"{current_time['year']}-{current_time['month']:02}-{current_time['date']:02} " \
                               f"{current_time['hours']:02}:{current_time['minutes']:02}:{current_time['seconds']:02}"

            # Insert the current date and time into MongoDB
            mongo_connection.add_current_datetime(current_time_str)

            print(f"Current Time: {current_time_str}")

            time.sleep(2)

    except KeyboardInterrupt:
        print("Programa detenido por el usuario")

    finally:
        mongo_connection.close()
