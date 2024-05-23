using SimcaWPF.Services;

namespace SimcaWPF.Models
{
    public class MAX31855Model
    {
        private readonly MAX31855Service _max31855Service;

        // Constructor que recibe una instancia del servicio MAX31855Service
        public MAX31855Model(MAX31855Service max31855Service)
        {
            _max31855Service = max31855Service;
        }

        // Método para obtener la temperatura del termopar tipo K
        public double GetTemperature()
        {
            // Llamamos al método correspondiente del servicio para obtener la temperatura
            return _max31855Service.GetTemperatureFromServer();
        }
    }
}
