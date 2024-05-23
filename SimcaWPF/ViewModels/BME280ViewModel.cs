using System;
using System.ComponentModel;
using System.Configuration;
using SimcaWPF.Models;
using SimcaWPF.Services;

namespace SimcaWPF.ViewModels
{
    public class BME280ViewModel : INotifyPropertyChanged
    {
        private readonly BME280Model _bme280Model;

        private double _temperature;
        private double _humidity;
        private double _pressure;

        // Propiedad para almacenar el valor de la temperatura
        public double Temperature
        {
            get { return _temperature; }
            set
            {
                if (_temperature != value)
                {
                    _temperature = value;
                    OnPropertyChanged("Temperature");
                }
            }
        }

        // Propiedad para almacenar el valor de la humedad
        public double Humidity
        {
            get { return _humidity; }
            set
            {
                if (_humidity != value)
                {
                    _humidity = value;
                    OnPropertyChanged("Humidity");
                }
            }
        }

        // Propiedad para almacenar el valor de la presión
        public double Pressure
        {
            get { return _pressure; }
            set
            {
                if (_pressure != value)
                {
                    _pressure = value;
                    OnPropertyChanged("Pressure");
                }
            }
        }

        // Constructor
        public BME280ViewModel()
        {
            // Leer la dirección IP y el puerto desde App.config
            string serverIpAddress = ConfigurationManager.AppSettings["ServerIpAddress"];
            int serverPort = int.Parse(ConfigurationManager.AppSettings["ServerPort"]);

            // Inicializa el servicio BME280Service
            var bme280Service = new BME280Service(serverIpAddress, serverPort); // Coloca la dirección IP y el puerto del servidor Python
            // Inicializa el modelo BME280Model con el servicio
            _bme280Model = new BME280Model(bme280Service);

            // Actualiza los valores de temperatura, humedad y presión
            UpdateSensorValues();
        }

        // Método para actualizar los valores del sensor llamando al modelo
        public void UpdateSensorValues()
        {
            //UpdateTemperature();
            UpdateHumidity();
            UpdatePressure();
        }

        // Método para actualizar el valor de la temperatura
        public void UpdateTemperature()
        {
            var tempData = _bme280Model.GetTemperatureData();
            Temperature = tempData;
        }

        // Método para actualizar el valor de la humedad
        public void UpdateHumidity()
        {
            var humidityData = _bme280Model.GetHumidityData();
            Humidity = humidityData;
        }

        // Método para actualizar el valor de la presión
        public void UpdatePressure()
        {
            var pressureData = _bme280Model.GetPressureData();
            Pressure = pressureData;
        }

        // Implementación de la interfaz INotifyPropertyChanged para notificar cambios en las propiedades
        public event PropertyChangedEventHandler PropertyChanged;
        protected virtual void OnPropertyChanged(string propertyName)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
