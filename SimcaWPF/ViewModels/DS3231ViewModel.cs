using System;
using System.ComponentModel;
using System.Configuration;
using System.Threading.Tasks;
using SimcaWPF.Models;
using SimcaWPF.Services;

namespace SimcaWPF.ViewModels
{
    public class DS3231ViewModel : INotifyPropertyChanged
    {
        private readonly DS3231Model _ds3231Model;

        private DateTime _currentDateTime;

        // Propiedad para almacenar la fecha y hora actual del DS3231
        public DateTime CurrentDateTime
        {
            get { return _currentDateTime; }
            set
            {
                if (_currentDateTime != value)
                {
                    _currentDateTime = value;
                    OnPropertyChanged("CurrentDateTime");
                }
            }
        }

        // Constructor
        public DS3231ViewModel()
        {
            // Leer la dirección IP y el puerto desde App.config
            string serverIpAddress = ConfigurationManager.AppSettings["ServerIpAddress"];
            int serverPort = int.Parse(ConfigurationManager.AppSettings["ServerPort"]);

            // Inicializa el servicio DS3231Service
            var ds3231Service = new DS3231Service(serverIpAddress, serverPort); // dirección_ip_raspberry_pi y puerto_servidor_python.
            // Inicializa el modelo DS3231Model con el servicio
            _ds3231Model = new DS3231Model(ds3231Service);

            // Actualiza la fecha y hora del DS3231
            UpdateDateTime();
        }

        // Método para actualizar la fecha y hora del DS3231 llamando al modelo
        public async void UpdateDateTime()
        {
            try
            {
                // Llama al método correspondiente del modelo para obtener la fecha y hora actual
                CurrentDateTime = await _ds3231Model.GetCurrentDateTime();
            }
            catch (Exception ex)
            {
                // Maneja cualquier error que ocurra al obtener la fecha y hora
                // Puedes mostrar un mensaje de error o realizar alguna otra acción de manejo de errores aquí
                Console.WriteLine($"Error al obtener la fecha y hora del DS3231: {ex.Message}");
            }
        }

        // Implementación de la interfaz INotifyPropertyChanged para notificar cambios en las propiedades
        public event PropertyChangedEventHandler PropertyChanged;
        protected virtual void OnPropertyChanged(string propertyName)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
