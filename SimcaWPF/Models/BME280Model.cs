using SimcaWPF.Services;
using static SimcaWPF.Services.BME280Service;

namespace SimcaWPF.Models
{
    public class BME280Model
    {
        private readonly BME280Service _bme280Service;

        // Constructor que recibe una instancia del servicio BME280Service
        public BME280Model(BME280Service bme280Service)
        {
            _bme280Service = bme280Service;
        }

        // Método para obtener los datos del sensor BME280 (temperatura, humedad y presión)
        public SensorData GetSensorData()
        {
            // Llamamos al método correspondiente del servicio para obtener los datos del sensor
            return _bme280Service.GetSensorData();
        }

        public double GetTemperatureData()
        {
            return _bme280Service.GetTemperatureData();
        }

        public double GetHumidityData()
        {
            return _bme280Service.GetHumidityData();
        }

        public double GetPressureData()
        {
            return _bme280Service.GetPressureData();
        }
    }
}