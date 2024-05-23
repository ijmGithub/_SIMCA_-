using SimcaWPF.Services;
using System;
using System.Threading.Tasks;

namespace SimcaWPF.Models
{
    public class DS3231Model
    {
        private readonly DS3231Service _ds3231Service;

        // Constructor que recibe una instancia del servicio DS3231Service
        public DS3231Model(DS3231Service ds3231Service)
        {
            _ds3231Service = ds3231Service;
        }

        // Método para obtener la fecha y hora actual del DS3231
        public async Task<DateTime> GetCurrentDateTime()
        {
            // Llamamos al método correspondiente del servicio para obtener la fecha y hora actual
            return await _ds3231Service.GetCurrentDateTime();
        }
    }
}
