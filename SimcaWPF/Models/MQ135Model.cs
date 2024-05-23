using SimcaWPF.Services;

namespace SimcaWPF.Models
{
    public class MQ135Model
    {
        private readonly MQ135Service _mq135Service;

        // Constructor que recibe una instancia del servicio MQ135Service
        public MQ135Model(MQ135Service mq135Service)
        {
            _mq135Service = mq135Service;
        }

        // Método para obtener la concentración de gas medida por el MQ135
        public double GetGasConcentration()
        {
            // Llamamos al método correspondiente del servicio para obtener la concentración de gas
            return _mq135Service.GetGasConcentration();
        }
    }
}
