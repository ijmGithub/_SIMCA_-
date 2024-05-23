using SimcaWPF.Services;

namespace SimcaWPF.Models
{
    public class BH1750Model
    {
        private readonly BH1750Service _bh1750Service;

        // Constructor que recibe una instancia del servicio BH1750Service
        public BH1750Model(BH1750Service bh1750Service)
        {
            _bh1750Service = bh1750Service;
        }

        // Método para obtener la intensidad de luz ambiental del sensor BH1750
        public double GetLightIntensity()
        {
            // Llamamos al método correspondiente del servicio para obtener la intensidad de luz ambiental
            return _bh1750Service.GetLightIntensity();
        }
    }
}
