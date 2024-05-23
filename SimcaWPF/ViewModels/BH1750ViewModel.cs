using System.ComponentModel;
using System.Configuration;
using SimcaWPF.Models;
using SimcaWPF.Services;

namespace SimcaWPF.ViewModels
{
    public class BH1750ViewModel : INotifyPropertyChanged
    {
        private readonly BH1750Model _bh1750Model;
        private double _luxValue;

        // Propiedad para almacenar el valor de la intensidad de luz ambiental
        public double LuxValue
        {
            get { return _luxValue; }
            set
            {
                if (_luxValue != value)
                {
                    _luxValue = value;
                    OnPropertyChanged("LuxValue");
                }
            }
        }

        // Constructor
        public BH1750ViewModel()
        {
            // Leer la dirección IP y el puerto desde App.config
            string serverIpAddress = ConfigurationManager.AppSettings["ServerIpAddress"];
            int serverPort = int.Parse(ConfigurationManager.AppSettings["ServerPort"]);

            // Inicializa el servicio BH1750Service
            var bh1750Service = new BH1750Service(serverIpAddress, serverPort); // Coloca la dirección IP y el puerto del servidor Python
            // Inicializa el modelo BH1750Model con el servicio
            _bh1750Model = new BH1750Model(bh1750Service);

            // Actualiza el valor de LuxValue
            UpdateLuxValue();
        }

        // Método para actualizar LuxValue llamando al modelo
        public void UpdateLuxValue()
        {
            LuxValue = _bh1750Model.GetLightIntensity();
        }

        // Implementación de la interfaz INotifyPropertyChanged para notificar cambios en las propiedades
        public event PropertyChangedEventHandler PropertyChanged;
        protected virtual void OnPropertyChanged(string propertyName)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
