using System;
using System.ComponentModel;
using System.Configuration;
using SimcaWPF.Models;
using SimcaWPF.Services;

namespace SimcaWPF.ViewModels
{
    public class MAX31855ViewModel : INotifyPropertyChanged
    {
        private readonly MAX31855Model _max31855Model;

        private double _temperature;

        // Propiedad para almacenar el valor de la temperatura del termopar tipo K
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

        // Constructor
        public MAX31855ViewModel()
        {
            // Leer la dirección IP y el puerto desde App.config
            string serverIpAddress = ConfigurationManager.AppSettings["ServerIpAddress"];
            int serverPort = int.Parse(ConfigurationManager.AppSettings["ServerPort"]);

            // Inicializa el servicio MAX31855Service
            var max31855Service = new MAX31855Service(serverIpAddress, serverPort);
            // Inicializa el modelo MAX31855Model con el servicio
            _max31855Model = new MAX31855Model(max31855Service);

            // Actualiza el valor de la temperatura del termopar tipo K
            UpdateTemperature();
        }

        // Método para actualizar el valor de la temperatura llamando al modelo
        public void UpdateTemperature()
        {
            Temperature = _max31855Model.GetTemperature();
        }

        // Implementación de la interfaz INotifyPropertyChanged para notificar cambios en las propiedades
        public event PropertyChangedEventHandler PropertyChanged;
        protected virtual void OnPropertyChanged(string propertyName)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
