using System;
using System.ComponentModel;
using System.Configuration;
using SimcaWPF.Models;
using SimcaWPF.Services;

namespace SimcaWPF.ViewModels
{
    public class MQ135ViewModel : INotifyPropertyChanged
    {
        private readonly MQ135Model _mq135Model;

        private double _gasConcentration;

        // Propiedad para almacenar la concentración de gas medida por el MQ-135
        public double GasConcentration
        {
            get { return _gasConcentration; }
            set
            {
                if (_gasConcentration != value)
                {
                    _gasConcentration = value;
                    OnPropertyChanged(nameof(GasConcentration));
                }
            }
        }

        // Constructor
        public MQ135ViewModel()
        {
            // Leer la dirección IP y el puerto desde App.config
            string serverIpAddress = ConfigurationManager.AppSettings["ServerIpAddress"];
            int serverPort = int.Parse(ConfigurationManager.AppSettings["ServerPort"]);

            // Inicializa el servicio MQ135Service con la dirección IP y el puerto del servidor
            var mq135Service = new MQ135Service(serverIpAddress, serverPort); // Ejemplo de dirección IP y puerto
            // Inicializa el modelo MQ135Model con el servicio
            _mq135Model = new MQ135Model(mq135Service);

            // Actualiza la concentración de gas medida por el MQ135
            UpdateGasConcentration();
        }

        // Método para actualizar la concentración de gas llamando al modelo
        public void UpdateGasConcentration()
        {
            GasConcentration = _mq135Model.GetGasConcentration();
        }

        // Implementación de la interfaz INotifyPropertyChanged para notificar cambios en las propiedades
        public event PropertyChangedEventHandler PropertyChanged;
        protected virtual void OnPropertyChanged(string propertyName)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
